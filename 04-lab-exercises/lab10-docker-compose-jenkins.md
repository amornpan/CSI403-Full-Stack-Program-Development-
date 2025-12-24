# Lab 10: Docker Compose & Jenkins

**Week 11 | March 18-20, 2026 | 2%**

## 🎯 Objectives
- Create multi-container applications with Docker Compose
- Set up MSSQL database container
- Configure Jenkins for CI/CD
- Create basic pipeline

## 💻 Part 1: Docker Compose Basics (25 min)

### Exercise 1.1: Simple Compose File
Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./data/loan.db
    volumes:
      - ./data:/app/data
```

### Exercise 1.2: Full Stack Compose
Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  # FastAPI Application
  api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: loan-api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mssql+pyodbc://sa:YourStrong@Password123@db:1433/LoanDB?driver=ODBC+Driver+17+for+SQL+Server
      - SECRET_KEY=your-secret-key-here
      - DEBUG=false
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./app:/app/app
    networks:
      - loan-network
    restart: unless-stopped

  # Microsoft SQL Server
  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    container_name: loan-db
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=YourStrong@Password123
      - MSSQL_PID=Express
    ports:
      - "1433:1433"
    volumes:
      - mssql-data:/var/opt/mssql
    networks:
      - loan-network
    healthcheck:
      test: /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "YourStrong@Password123" -Q "SELECT 1" -b -o /dev/null
      interval: 10s
      timeout: 3s
      retries: 10
      start_period: 10s
    restart: unless-stopped

  # Database Admin (Adminer)
  adminer:
    image: adminer
    container_name: loan-adminer
    ports:
      - "8080:8080"
    networks:
      - loan-network
    depends_on:
      - db
    restart: unless-stopped

volumes:
  mssql-data:
    driver: local

networks:
  loan-network:
    driver: bridge
```

## 💻 Part 2: Docker Compose Commands (20 min)

### Exercise 2.1: Basic Operations
```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs
docker-compose logs -f api
docker-compose logs --tail=100 db

# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# Remove with volumes
docker-compose down -v

# Rebuild images
docker-compose build
docker-compose up --build

# Scale services
docker-compose up -d --scale api=3
```

### Exercise 2.2: Service Management
```bash
# List services
docker-compose ps

# Execute command in service
docker-compose exec api bash
docker-compose exec db /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "YourStrong@Password123"

# View service logs
docker-compose logs api

# Restart specific service
docker-compose restart api

# Pull latest images
docker-compose pull
```

## 💻 Part 3: Environment Configuration (15 min)

### Exercise 3.1: Environment Files
Create `.env`:
```env
# Database
DB_HOST=db
DB_PORT=1433
DB_NAME=LoanDB
DB_USER=sa
DB_PASSWORD=YourStrong@Password123

# Application
SECRET_KEY=your-super-secret-key-change-in-production
DEBUG=false
API_PORT=8000

# MSSQL
ACCEPT_EULA=Y
MSSQL_PID=Express
```

Update `docker-compose.yml`:
```yaml
services:
  api:
    environment:
      - DATABASE_URL=mssql+pyodbc://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server
      - SECRET_KEY=${SECRET_KEY}
    ports:
      - "${API_PORT}:8000"

  db:
    environment:
      - ACCEPT_EULA=${ACCEPT_EULA}
      - SA_PASSWORD=${DB_PASSWORD}
      - MSSQL_PID=${MSSQL_PID}
```

### Exercise 3.2: Multiple Environments
Create `docker-compose.override.yml` (development):
```yaml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app
    environment:
      - DEBUG=true
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Create `docker-compose.prod.yml`:
```yaml
version: '3.8'

services:
  api:
    image: yourusername/loan-api:latest
    environment:
      - DEBUG=false
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

Usage:
```bash
# Development (uses override automatically)
docker-compose up

# Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## 💻 Part 4: Jenkins Setup (30 min)

### Exercise 4.1: Jenkins Container
Add to `docker-compose.yml`:
```yaml
  jenkins:
    image: jenkins/jenkins:lts
    container_name: loan-jenkins
    privileged: true
    user: root
    ports:
      - "8081:8080"
      - "50000:50000"
    volumes:
      - jenkins-data:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - loan-network

volumes:
  jenkins-data:
```

### Exercise 4.2: Jenkinsfile
Create `Jenkinsfile`:
```groovy
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'loan-api'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} \
                        python -m pytest tests/ -v --tb=short || true
                '''
            }
        }
        
        stage('Code Quality') {
            steps {
                echo 'Checking code quality...'
                sh '''
                    docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} \
                        python -m flake8 app/ --count --statistics || true
                '''
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                echo 'Deploying to staging...'
                sh '''
                    docker-compose -f docker-compose.staging.yml down || true
                    docker-compose -f docker-compose.staging.yml up -d
                '''
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                echo 'Deploying to production...'
                sh '''
                    docker-compose -f docker-compose.prod.yml down || true
                    docker-compose -f docker-compose.prod.yml up -d
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            sh 'docker system prune -f || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
            // Send notification
        }
    }
}
```

### Exercise 4.3: Jenkins Setup Steps
1. Start Jenkins: `docker-compose up -d jenkins`
2. Get initial password: `docker exec loan-jenkins cat /var/jenkins_home/secrets/initialAdminPassword`
3. Access Jenkins: `http://localhost:8081`
4. Install suggested plugins
5. Create admin user
6. Install additional plugins: Docker, Docker Pipeline, GitHub

## 📝 Assignment

1. Create complete `docker-compose.yml` for Loan System with:
   - FastAPI app
   - MSSQL database
   - Adminer
   - Jenkins

2. Create `Jenkinsfile` with:
   - Build stage
   - Test stage
   - Deploy stage

3. Document setup instructions in README

## 📤 Submission
```bash
git add .
git commit -m "Lab 10: Docker Compose and Jenkins"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Docker Compose | 0.5% |
| Environment config | 0.5% |
| Jenkins setup | 0.5% |
| Assignment | 0.5% |

---
**Deadline:** Before Week 12 class
