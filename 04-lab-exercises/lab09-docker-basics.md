# Lab 09: Docker Basics

**Week 10 | March 11-13, 2026 | 2%**

## 🎯 Objectives
- Understand Docker concepts
- Create Dockerfile for FastAPI app
- Build and run Docker images
- Use Docker commands

## 💻 Part 1: Docker Concepts (15 min)

### Key Terms
- **Image**: Blueprint/template for containers
- **Container**: Running instance of an image
- **Dockerfile**: Instructions to build an image
- **Registry**: Storage for images (Docker Hub)

### Basic Commands
```bash
# Check Docker version
docker --version

# List images
docker images

# List containers
docker ps          # Running only
docker ps -a       # All containers

# Pull image
docker pull python:3.11-slim

# Run container
docker run -it python:3.11-slim bash
```

## 💻 Part 2: Dockerfile (30 min)

### Exercise 2.1: Simple Dockerfile
Create `Dockerfile`:
```dockerfile
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Exercise 2.2: Multi-stage Build
Create `Dockerfile.multi`:
```dockerfile
# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application
COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 💻 Part 3: Build & Run (25 min)

### Exercise 3.1: Build Image
```bash
# Build with tag
docker build -t loan-api:v1 .

# Build with different Dockerfile
docker build -f Dockerfile.multi -t loan-api:v1-slim .

# List images
docker images | grep loan-api
```

### Exercise 3.2: Run Container
```bash
# Run in foreground
docker run -p 8000:8000 loan-api:v1

# Run in background (detached)
docker run -d -p 8000:8000 --name loan-api-container loan-api:v1

# View logs
docker logs loan-api-container
docker logs -f loan-api-container  # Follow

# Stop container
docker stop loan-api-container

# Remove container
docker rm loan-api-container

# Run with environment variables
docker run -d -p 8000:8000 \
    -e DATABASE_URL="sqlite:///./data/loan.db" \
    -e SECRET_KEY="my-secret" \
    --name loan-api \
    loan-api:v1
```

### Exercise 3.3: Volume Mounting
```bash
# Mount local directory
docker run -d -p 8000:8000 \
    -v $(pwd)/data:/app/data \
    --name loan-api \
    loan-api:v1

# For Windows PowerShell
docker run -d -p 8000:8000 \
    -v ${PWD}/data:/app/data \
    --name loan-api \
    loan-api:v1
```

## 💻 Part 4: Docker Commands (20 min)

### Exercise 4.1: Container Management
```bash
# Execute command in running container
docker exec -it loan-api-container bash
docker exec loan-api-container python --version

# Copy files
docker cp loan-api-container:/app/data/loan.db ./backup.db
docker cp ./seed.sql loan-api-container:/app/

# Inspect container
docker inspect loan-api-container

# Resource usage
docker stats

# Prune unused resources
docker system prune
docker image prune
docker container prune
```

### Exercise 4.2: .dockerignore
Create `.dockerignore`:
```
# Git
.git
.gitignore

# Python
__pycache__
*.pyc
*.pyo
*.pyd
.Python
venv/
.venv/
env/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp

# Test
.pytest_cache/
.coverage
htmlcov/

# Local
*.db
*.sqlite3
.env
.env.local

# Docker
Dockerfile*
docker-compose*.yml

# Docs
*.md
docs/
```

## 💻 Part 5: Push to Registry (10 min)

### Exercise 5.1: Docker Hub
```bash
# Login to Docker Hub
docker login

# Tag image for registry
docker tag loan-api:v1 yourusername/loan-api:v1
docker tag loan-api:v1 yourusername/loan-api:latest

# Push to Docker Hub
docker push yourusername/loan-api:v1
docker push yourusername/loan-api:latest

# Pull from anywhere
docker pull yourusername/loan-api:v1
```

## 📝 Assignment

1. Create optimized Dockerfile for the Loan Management System
2. Build and test locally
3. Push to Docker Hub
4. Document all steps in README

### Requirements:
- Use multi-stage build
- Non-root user
- Health check endpoint
- Environment variables for config
- Volume for database

### Dockerfile Template:
```dockerfile
FROM python:3.11-slim as builder
# ... build stage

FROM python:3.11-slim
# ... production stage

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/health || exit 1
```

## 📤 Submission
```bash
git add .
git commit -m "Lab 09: Docker basics"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Dockerfile | 0.5% |
| Build & Run | 0.5% |
| Docker commands | 0.5% |
| Assignment | 0.5% |

---
**Deadline:** Before Week 11 class
