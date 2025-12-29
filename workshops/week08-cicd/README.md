# Workshop 8: 🚀 CD &amp; Go Live

## 📋 Overview
| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | Complete CI/CD Pipeline |

---

## 💻 CP1: CD Stages (2%)

### Jenkinsfile
```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps { sh 'pytest' }
        }
        stage('Build') {
            steps { sh 'docker build -t taskflow .' }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop taskflow-app || true'
                sh 'docker rm taskflow-app || true'
                sh 'docker run -d --name taskflow-app -p 8000:8000 taskflow'
            }
        }
        stage('Health Check') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:8000/health'
            }
        }
    }
}
```

---

## 💻 CP2: Environment Config (2%)

### .env.example
```
DB_HOST=localhost
DB_PASSWORD=secret
SECRET_KEY=your-key
```

---

## 💻 CP3: Test Pipeline (2%)

1. Push code to GitHub
2. Watch Jenkins build
3. Verify deployment

---

## 💻 CP4: Documentation (2%)

Update README.md with:
- Quick start
- API docs link
- CI/CD info

```bash
git add . &amp;&amp; git commit -m "Complete CI/CD" &amp;&amp; git push
```

---

## 🎉 Phase 1 Complete!

You built:
- ✅ FastAPI REST API
- ✅ SQLAlchemy + MSSQL
- ✅ Bootstrap Frontend
- ✅ Jinja2 Templates
- ✅ Session Auth
- ✅ Docker Deployment
- ✅ pytest Testing
- ✅ Jenkins CI/CD

**Congratulations! 🎊**

---

[📖 Extended →](../../docs/extended/week08-devops.md)
