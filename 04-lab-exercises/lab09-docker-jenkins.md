# Lab 09: Docker + Jenkins Pipeline - Assessment Lab 2

**Week 9 | Assessment Lab | 5%**

## 🎯 Objectives
- สร้าง Dockerfile สำหรับ FastAPI Application
- ใช้ Docker Compose สำหรับ Multi-container Setup
- สร้าง Jenkins Pipeline (Jenkinsfile)
- เข้าใจ CI/CD Workflow

## ⚠️ Important: This is an Assessment Lab

งานนี้เก็บคะแนน **5%** ของคะแนนรวม

### Submission Requirements:
- **Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ของสัปดาห์ที่ 9
- **Submit via:** GitHub Repository ของกลุ่ม
- **Folder:** `lab2-docker-pipeline/`

### Grading Rubric:
| Criteria | Points |
|----------|:------:|
| Dockerfile (multi-stage build) | 1.5% |
| docker-compose.yml (multi-service) | 1.5% |
| Jenkinsfile (complete pipeline) | 1.5% |
| Documentation & README | 0.5% |
| **Total** | **5%** |

---

## 📋 Assignment Overview

สร้าง Docker และ CI/CD Setup สำหรับ Loan Management System:

### Required Files:
1. `Dockerfile` - Multi-stage build
2. `docker-compose.yml` - App + Database + Adminer
3. `Jenkinsfile` - CI/CD Pipeline
4. `.dockerignore` - Ignore files
5. `README.md` - Documentation

---

## 💻 Part 1: Dockerfile (1.5%)

สร้าง `Dockerfile`:

```dockerfile
# ============================================
# Stage 1: Builder
# ============================================
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ============================================
# Stage 2: Production
# ============================================
FROM python:3.11-slim as production

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Expose port
EXPOSE ${PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile Requirements Checklist:
- ✅ Multi-stage build (builder + production)
- ✅ Non-root user
- ✅ Health check
- ✅ Environment variables
- ✅ Proper layer caching

---

## 💻 Part 2: Docker Compose (1.5%)

สร้าง `docker-compose.yml`:

```yaml
version: '3.8'

services:
  # ============================================
  # FastAPI Application
  # ============================================
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
    container_name: loan-api
    ports:
      - "${APP_PORT:-8000}:8000"
    environment:
      - DATABASE_URL=${DATABASE_URL:-sqlite:///./data/loan.db}
      - SECRET_KEY=${SECRET_KEY:-change-me-in-production}
      - DEBUG=${DEBUG:-false}
    volumes:
      - app-data:/app/data
    depends_on:
      db:
        condition: service_healthy
    networks:
      - loan-network
    restart: unless-stopped

  # ============================================
  # Microsoft SQL Server
  # ============================================
  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    container_name: loan-db
    ports:
      - "${DB_PORT:-1433}:1433"
    environment:
      - ACCEPT_EULA=Y
      - MSSQL_SA_PASSWORD=${DB_PASSWORD:-YourStrong@Password123}
      - MSSQL_PID=Express
    volumes:
      - mssql-data:/var/opt/mssql
    networks:
      - loan-network
    healthcheck:
      test: /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "${DB_PASSWORD:-YourStrong@Password123}" -Q "SELECT 1" -C || exit 1
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 30s
    restart: unless-stopped

  # ============================================
  # Database Admin UI
  # ============================================
  adminer:
    image: adminer:latest
    container_name: loan-adminer
    ports:
      - "${ADMINER_PORT:-8080}:8080"
    environment:
      - ADMINER_DEFAULT_SERVER=db
    networks:
      - loan-network
    depends_on:
      - db
    restart: unless-stopped

# ============================================
# Volumes
# ============================================
volumes:
  app-data:
    driver: local
  mssql-data:
    driver: local

# ============================================
# Networks
# ============================================
networks:
  loan-network:
    driver: bridge
```

### Docker Compose Requirements Checklist:
- ✅ 3+ services (app, db, adminer)
- ✅ Health checks
- ✅ Environment variables
- ✅ Named volumes
- ✅ Custom network
- ✅ Depends on with condition

---

## 💻 Part 3: Jenkinsfile (1.5%)

สร้าง `Jenkinsfile`:

```groovy
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'loan-api'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    options {
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()
    }
    
    stages {
        // Stage 1: Checkout
        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
                
                script {
                    env.GIT_COMMIT_SHORT = sh(
                        script: 'git rev-parse --short HEAD',
                        returnStdout: true
                    ).trim()
                }
                
                echo "Building commit: ${env.GIT_COMMIT_SHORT}"
            }
        }
        
        // Stage 2: Build
        stage('Build') {
            steps {
                echo '🔨 Building Docker image...'
                sh '''
                    docker build \
                        -t ${DOCKER_IMAGE}:${DOCKER_TAG} \
                        -t ${DOCKER_IMAGE}:latest \
                        .
                '''
            }
        }
        
        // Stage 3: Test
        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh '''
                    docker run --rm \
                        -e TESTING=true \
                        ${DOCKER_IMAGE}:${DOCKER_TAG} \
                        python -m pytest tests/ -v --tb=short || true
                '''
            }
        }
        
        // Stage 4: Code Quality
        stage('Code Quality') {
            parallel {
                stage('Lint') {
                    steps {
                        echo '🔍 Running linter...'
                        sh '''
                            docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} \
                                python -m flake8 app/ --count --statistics || true
                        '''
                    }
                }
                
                stage('Security') {
                    steps {
                        echo '🔒 Security scan...'
                        sh '''
                            docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} \
                                pip check || true
                        '''
                    }
                }
            }
        }
        
        // Stage 5: Deploy Staging
        stage('Deploy Staging') {
            when {
                branch 'develop'
            }
            steps {
                echo '🚀 Deploying to staging...'
                sh '''
                    docker-compose -f docker-compose.yml down || true
                    docker-compose -f docker-compose.yml up -d
                '''
            }
        }
        
        // Stage 6: Deploy Production
        stage('Deploy Production') {
            when {
                branch 'main'
            }
            steps {
                echo '🚀 Deploying to production...'
                input message: 'Deploy to production?', ok: 'Deploy'
                
                sh '''
                    docker-compose -f docker-compose.prod.yml down || true
                    docker-compose -f docker-compose.prod.yml up -d
                '''
            }
        }
    }
    
    post {
        always {
            echo '🧹 Cleaning up...'
            sh 'docker image prune -f || true'
        }
        
        success {
            echo '✅ Pipeline completed successfully!'
        }
        
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
```

### Jenkinsfile Requirements Checklist:
- ✅ 5+ stages
- ✅ Parallel stages
- ✅ Conditional deployment
- ✅ Manual approval for production
- ✅ Post actions

---

## 💻 Part 4: Supporting Files

### 4.1 .dockerignore
```
# Git
.git
.gitignore

# Python
__pycache__
*.pyc
*.pyo
venv/
.venv/
*.egg-info/
.pytest_cache/
.coverage

# IDE
.vscode/
.idea/

# Docker
Dockerfile*
docker-compose*.yml

# CI/CD
Jenkinsfile

# Docs
*.md
docs/

# Local
.env
*.db
*.log
```

### 4.2 .env.example
```env
# Application
APP_PORT=8000
SECRET_KEY=change-this-in-production
DEBUG=false

# Database
DB_PORT=1433
DB_PASSWORD=YourStrong@Password123

# Admin
ADMINER_PORT=8080
```

---

## 💻 Part 5: Testing Your Setup

### 5.1 Build and Run
```bash
# Copy environment file
cp .env.example .env

# Build image
docker build -t loan-api:test .

# Run with compose
docker-compose up -d

# Check services
docker-compose ps

# View logs
docker-compose logs -f app

# Test health endpoint
curl http://localhost:8000/health
```

### 5.2 Access Services
| Service | URL |
|---------|-----|
| API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| Adminer | http://localhost:8080 |

### 5.3 Stop Services
```bash
# Stop
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

---

## 📤 Submission

### Repository Structure
```
group-repo/
└── lab2-docker-pipeline/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── models.py
    │   ├── schemas.py
    │   └── database.py
    ├── tests/
    │   └── test_api.py
    ├── Dockerfile
    ├── docker-compose.yml
    ├── Jenkinsfile
    ├── .dockerignore
    ├── .env.example
    ├── requirements.txt
    └── README.md
```

### README.md Template
```markdown
# Lab 2: Docker + Jenkins Pipeline - Group X

## Team Members
- Member 1 (Student ID)
- Member 2 (Student ID)
- Member 3 (Student ID)

## Project Overview
Docker และ CI/CD setup สำหรับ Loan Management System

## Prerequisites
- Docker Desktop 4.x+
- Docker Compose 2.x+
- Git

## Quick Start

### 1. Clone Repository
\`\`\`bash
git clone <repo-url>
cd lab2-docker-pipeline
\`\`\`

### 2. Setup Environment
\`\`\`bash
cp .env.example .env
# Edit .env if needed
\`\`\`

### 3. Build and Run
\`\`\`bash
docker-compose up -d
\`\`\`

### 4. Access Application
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Adminer: http://localhost:8080

## Docker Images

### Build
\`\`\`bash
docker build -t loan-api:latest .
\`\`\`

### Run
\`\`\`bash
docker run -p 8000:8000 loan-api:latest
\`\`\`

## CI/CD Pipeline

### Stages
1. **Checkout** - Get source code
2. **Build** - Build Docker image
3. **Test** - Run pytest
4. **Code Quality** - Lint & Security scan
5. **Deploy Staging** - Deploy to staging (develop branch)
6. **Deploy Production** - Deploy to production (main branch)

### Pipeline Diagram
\`\`\`
[Checkout] → [Build] → [Test] → [Quality] → [Deploy]
                                    ↓
                              ┌─────┴─────┐
                              ↓           ↓
                           [Lint]    [Security]
\`\`\`

## Screenshots
[Include screenshots of:]
- Docker containers running
- Swagger UI
- Jenkins pipeline (if available)

## Troubleshooting

### Database Connection Error
\`\`\`bash
# Wait for DB to be ready
docker-compose logs db
\`\`\`

### Port Already in Use
\`\`\`bash
# Change port in .env
APP_PORT=8001
\`\`\`

## Team Contributions
| Member | Contribution |
|--------|--------------|
| Member 1 | Dockerfile |
| Member 2 | docker-compose.yml |
| Member 3 | Jenkinsfile |
```

### Git Commands
```bash
cd lab2-docker-pipeline
git add .
git commit -m "Lab 2: Docker + Jenkins Pipeline - Complete"
git push origin main
```

---

## ✅ Checklist Before Submission

### Dockerfile
- [ ] Multi-stage build
- [ ] Non-root user
- [ ] Health check
- [ ] Optimized layers

### docker-compose.yml
- [ ] 3+ services
- [ ] Health checks
- [ ] Named volumes
- [ ] Custom network

### Jenkinsfile
- [ ] 5+ stages
- [ ] Parallel stages
- [ ] Conditional deploy
- [ ] Post actions

### Documentation
- [ ] README.md complete
- [ ] .env.example provided
- [ ] Screenshots included

---

## 🎯 Bonus Points

ทำเพิ่มเติมเพื่อแสดงความสามารถ:

1. **Docker Hub Integration** - Push image to Docker Hub
2. **Nginx Reverse Proxy** - Add nginx service
3. **SSL/TLS** - Configure HTTPS
4. **Monitoring** - Add Prometheus/Grafana
5. **Log Aggregation** - Add ELK Stack

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 9

**Next Phase:** Week 10-15 - Project Development
