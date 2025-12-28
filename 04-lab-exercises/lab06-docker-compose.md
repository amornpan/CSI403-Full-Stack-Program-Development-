# Lab 06: Docker + Docker Compose

**Week 7 | 8%**

## 🎯 Objectives

- เขียน Dockerfile สำหรับ FastAPI
- ใช้ Docker Compose สำหรับ Multi-container
- รัน TaskFlow ด้วย Docker

---

## 💻 Part 1: Dockerfile

### 1.1 Create Dockerfile

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for MSSQL
RUN apt-get update && apt-get install -y \
    curl gnupg2 apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 1.2 Create .dockerignore

```
# .dockerignore
__pycache__
*.pyc
*.pyo
.git
.gitignore
.env
.env.local
venv
.venv
*.md
.pytest_cache
.coverage
htmlcov
.vscode
.idea
```

---

## 💻 Part 2: Docker Compose

### 2.1 Create docker-compose.yml

```yaml
# docker-compose.yml
version: '3.8'

services:
  # FastAPI Application
  app:
    build: .
    container_name: taskflow-app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mssql+pyodbc://sa:${DB_PASSWORD}@db:1433/taskflow?driver=ODBC+Driver+17+for+SQL+Server
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - ./app:/app/app
    depends_on:
      db:
        condition: service_healthy
    networks:
      - taskflow-network
    restart: unless-stopped

  # MSSQL Database
  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    container_name: taskflow-db
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=${DB_PASSWORD}
      - MSSQL_PID=Express
    ports:
      - "1433:1433"
    volumes:
      - mssql_data:/var/opt/mssql
    healthcheck:
      test: /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "${DB_PASSWORD}" -Q "SELECT 1" || exit 1
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    networks:
      - taskflow-network
    restart: unless-stopped

  # Jenkins CI/CD (optional)
  jenkins:
    image: jenkins/jenkins:lts
    container_name: taskflow-jenkins
    privileged: true
    user: root
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - taskflow-network
    restart: unless-stopped

networks:
  taskflow-network:
    driver: bridge

volumes:
  mssql_data:
  jenkins_home:
```

### 2.2 Create .env file

```bash
# .env
DB_PASSWORD=YourStrong@Password123
SECRET_KEY=your-super-secret-key-change-this
```

---

## 💻 Part 3: Build and Run

### 3.1 Build Images

```bash
# Build all services
docker-compose build

# Build specific service
docker-compose build app
```

### 3.2 Run Services

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f app
```

### 3.3 Verify

```bash
# Check running containers
docker-compose ps

# Test app
curl http://localhost:8000/health

# Access:
# App: http://localhost:8000
# Swagger: http://localhost:8000/docs
# Jenkins: http://localhost:8080
```

### 3.4 Stop Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

---

## 💻 Part 4: Docker Commands Reference

```bash
# Build image
docker build -t taskflow:latest .

# Run container manually
docker run -d -p 8000:8000 --name taskflow taskflow:latest

# Enter container shell
docker exec -it taskflow-app bash

# View container logs
docker logs taskflow-app

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune
```

---

## 📤 Submission

### Checklist

- [ ] Dockerfile works correctly
- [ ] docker-compose.yml with 3 services (app, db, jenkins)
- [ ] .env file with secrets
- [ ] .dockerignore file
- [ ] `docker-compose up -d` runs without errors
- [ ] App connects to database
- [ ] All endpoints work

### Git Commands

```bash
git checkout -b feature/lab06-docker
git add .
git commit -m "Lab 6: Docker + Docker Compose"
git push -u origin feature/lab06-docker
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| Dockerfile ถูกต้อง | 2% |
| docker-compose.yml (3 services) | 3% |
| Network + Volume config | 1.5% |
| App runs and connects to DB | 1% |
| Documentation | 0.5% |
| **รวม** | **8%** |

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 7
