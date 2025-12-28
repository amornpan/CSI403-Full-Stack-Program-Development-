# Lab 08: Jenkins CD + Deployment

**Week 9 | 8%**

## 🎯 Objectives

- สร้าง CD Pipeline ใน Jenkins
- Auto Build Docker Image
- Auto Deploy to Local Docker
- Health Check หลัง Deploy

---

## 💻 Part 1: Complete Jenkinsfile (CI/CD)

### 1.1 Update Jenkinsfile

```groovy
// Jenkinsfile - Complete CI/CD Pipeline
pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'taskflow'
        CONTAINER_NAME = 'taskflow-app'
        APP_PORT = '8000'
        NETWORK_NAME = 'taskflow-network'
    }
    
    stages {
        // ===== CI STAGES =====
        
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Code checked out from ${env.GIT_BRANCH}"
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-cov
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=app --cov-report=xml -v --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                }
                failure {
                    echo '❌ Tests failed! Stopping pipeline.'
                }
            }
        }
        
        // ===== CD STAGES =====
        
        stage('Build Docker Image') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                    sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
                }
                echo "✅ Docker image built: ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
        
        stage('Stop Old Container') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    sh """
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    """
                }
                echo "✅ Old container removed"
            }
        }
        
        stage('Deploy New Container') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    sh """
                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            --network ${NETWORK_NAME} \
                            -p ${APP_PORT}:8000 \
                            -e DATABASE_URL="\${DATABASE_URL}" \
                            -e SECRET_KEY="\${SECRET_KEY}" \
                            --restart unless-stopped \
                            ${IMAGE_NAME}:latest
                    """
                }
                echo "✅ New container deployed"
            }
        }
        
        stage('Health Check') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    sh '''
                        echo "Waiting for app to start..."
                        sleep 15
                        
                        # Health check
                        for i in 1 2 3 4 5; do
                            if curl -f http://localhost:${APP_PORT}/health; then
                                echo "✅ App is healthy!"
                                exit 0
                            fi
                            echo "Attempt $i failed, retrying..."
                            sleep 5
                        done
                        
                        echo "❌ Health check failed!"
                        exit 1
                    '''
                }
            }
        }
        
        stage('Cleanup Old Images') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                sh '''
                    # Keep only last 3 images
                    docker images ${IMAGE_NAME} --format "{{.ID}} {{.Tag}}" | \
                        grep -v latest | \
                        sort -t- -k2 -n -r | \
                        tail -n +4 | \
                        awk '{print $1}' | \
                        xargs -r docker rmi || true
                '''
                echo "✅ Old images cleaned up"
            }
        }
    }
    
    post {
        success {
            echo '''
            ╔═══════════════════════════════════════════╗
            ║  🎉 CI/CD Pipeline Completed Successfully! ║
            ║                                           ║
            ║  🌐 App: http://localhost:8000            ║
            ║  📄 Docs: http://localhost:8000/docs      ║
            ╚═══════════════════════════════════════════╝
            '''
        }
        failure {
            echo '''
            ╔═══════════════════════════════════════════╗
            ║  ❌ Pipeline Failed!                       ║
            ║                                           ║
            ║  Check logs for details.                  ║
            ╚═══════════════════════════════════════════╝
            '''
            script {
                // Rollback: restart old container if exists
                sh """
                    docker start ${CONTAINER_NAME}-backup || true
                """
            }
        }
        always {
            cleanWs()
        }
    }
}
```

---

## 💻 Part 2: Jenkins Credentials

### 2.1 Add Database URL Credential

1. Jenkins Dashboard → Manage Jenkins → Credentials
2. Add Credentials:
   - Kind: Secret text
   - ID: `database-url`
   - Secret: `mssql+pyodbc://sa:YourPassword@db:1433/taskflow?driver=ODBC+Driver+17+for+SQL+Server`

### 2.2 Add Secret Key Credential

1. Add Credentials:
   - Kind: Secret text
   - ID: `secret-key`
   - Secret: `your-super-secret-key`

### 2.3 Update Jenkinsfile to Use Credentials

```groovy
environment {
    IMAGE_NAME = 'taskflow'
    CONTAINER_NAME = 'taskflow-app'
    DATABASE_URL = credentials('database-url')
    SECRET_KEY = credentials('secret-key')
}
```

---

## 💻 Part 3: Webhook Setup (Optional)

### 3.1 GitHub Webhook

1. GitHub repo → Settings → Webhooks
2. Add webhook:
   - Payload URL: `http://YOUR_JENKINS_URL/github-webhook/`
   - Content type: `application/json`
   - Events: Push events

### 3.2 Jenkins Job Configuration

1. Build Triggers:
   - ✅ GitHub hook trigger for GITScm polling

---

## 💻 Part 4: Test the Pipeline

### 4.1 Manual Trigger

1. Jenkins Dashboard → taskflow-ci → Build Now
2. ดู Console Output

### 4.2 Auto Trigger (via Push)

```bash
# Make a change
echo "# Test" >> README.md
git add .
git commit -m "Test CI/CD pipeline"
git push origin main
```

### 4.3 Verify Deployment

```bash
# Check container running
docker ps | grep taskflow-app

# Test endpoints
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/docs
```

---

## 💻 Part 5: Pipeline Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    JENKINS CI/CD PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐                  │
│   │ Checkout │──▶│ Install  │──▶│   Test   │                  │
│   └──────────┘   │   Deps   │   │ (pytest) │                  │
│                  └──────────┘   └────┬─────┘                  │
│                                      │                         │
│                                      ▼                         │
│                              Tests Pass? ──▶ No ──▶ ❌ FAIL    │
│                                      │                         │
│                                     Yes                        │
│                                      ▼                         │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐                  │
│   │  Build   │──▶│   Stop   │──▶│  Deploy  │                  │
│   │  Image   │   │   Old    │   │   New    │                  │
│   └──────────┘   └──────────┘   └────┬─────┘                  │
│                                      │                         │
│                                      ▼                         │
│                              ┌──────────────┐                  │
│                              │ Health Check │                  │
│                              └──────┬───────┘                  │
│                                     │                          │
│                                     ▼                          │
│                              Healthy? ──▶ No ──▶ 🔄 Rollback   │
│                                     │                          │
│                                    Yes                         │
│                                     ▼                          │
│                              ┌──────────────┐                  │
│                              │   Cleanup    │                  │
│                              │ Old Images   │                  │
│                              └──────────────┘                  │
│                                     │                          │
│                                     ▼                          │
│                              🎉 SUCCESS!                       │
│                              App: http://localhost:8000        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📤 Submission

### Checklist

- [ ] Complete Jenkinsfile (CI + CD)
- [ ] Test → Build → Deploy → Health Check stages
- [ ] Credentials configured
- [ ] Pipeline runs successfully
- [ ] App deploys and works
- [ ] Health check passes
- [ ] Screenshot ของ Pipeline

### Git Commands

```bash
git checkout -b feature/lab08-jenkins-cd
git add .
git commit -m "Lab 8: Jenkins CD - Complete CI/CD pipeline"
git push -u origin feature/lab08-jenkins-cd
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| Jenkinsfile (CI stages) | 2% |
| Jenkinsfile (CD stages) | 2% |
| Health Check | 1.5% |
| Rollback / Error handling | 1% |
| Pipeline runs successfully | 1% |
| Documentation | 0.5% |
| **รวม** | **8%** |

---

## 🎉 Summary

เมื่อจบ Lab นี้ นักศึกษาจะมี:

```
✅ Complete TaskFlow Application
   ├── FastAPI Backend
   ├── MSSQL Database
   ├── Jinja2 Frontend
   └── Full CRUD Operations

✅ Docker Environment
   ├── Dockerfile
   ├── docker-compose.yml
   └── Multi-container setup

✅ CI/CD Pipeline
   ├── Automated Tests
   ├── Automated Build
   ├── Automated Deploy
   └── Health Checks

🚀 Push → Test → Build → Deploy → Live!
```

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 9

---

## 🎓 Ready for Phase 2: Group Project!

สัปดาห์หน้า (Week 10) จะเริ่ม Group Project
- จัดทีม 4-5 คน
- เลือกโปรเจค
- เขียน G1: Project Proposal
