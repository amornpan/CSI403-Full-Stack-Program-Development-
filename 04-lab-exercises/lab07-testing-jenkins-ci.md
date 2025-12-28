# Lab 07: Testing + Jenkins CI

**Week 8 | 8%**

## 🎯 Objectives

- เขียน Unit Tests ด้วย pytest
- ใช้ FastAPI TestClient
- ตั้งค่า Jenkins
- สร้าง CI Pipeline (Jenkinsfile)

---

## 💻 Part 1: pytest Setup

### 1.1 Install Testing Libraries

```bash
pip install pytest pytest-cov httpx
```

### 1.2 Create conftest.py

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

# In-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as c:
        yield c
    
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()
```

---

## 💻 Part 2: Write Tests

### 2.1 Test Health Endpoints

```python
# tests/test_health.py

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "TaskFlow" in response.json()["message"]


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

### 2.2 Test Task API

```python
# tests/test_tasks.py

class TestTaskAPI:
    
    def test_create_task(self, client):
        task_data = {
            "title": "Test Task",
            "description": "Test Description",
            "priority": "high"
        }
        response = client.post("/api/tasks", json=task_data)
        assert response.status_code == 201
        assert response.json()["title"] == "Test Task"
    
    def test_create_task_invalid(self, client):
        response = client.post("/api/tasks", json={})
        assert response.status_code == 422
    
    def test_get_tasks_empty(self, client):
        response = client.get("/api/tasks")
        assert response.status_code == 200
        assert response.json()["total"] == 0
    
    def test_get_task_not_found(self, client):
        response = client.get("/api/tasks/9999")
        assert response.status_code == 404
    
    def test_update_task(self, client):
        # Create first
        create_resp = client.post("/api/tasks", json={"title": "Original"})
        task_id = create_resp.json()["id"]
        
        # Update
        update_resp = client.put(f"/api/tasks/{task_id}", json={"title": "Updated"})
        assert update_resp.status_code == 200
        assert update_resp.json()["title"] == "Updated"
    
    def test_delete_task(self, client):
        # Create first
        create_resp = client.post("/api/tasks", json={"title": "To Delete"})
        task_id = create_resp.json()["id"]
        
        # Delete
        delete_resp = client.delete(f"/api/tasks/{task_id}")
        assert delete_resp.status_code == 204
        
        # Verify deleted
        get_resp = client.get(f"/api/tasks/{task_id}")
        assert get_resp.status_code == 404
    
    def test_filter_by_status(self, client):
        client.post("/api/tasks", json={"title": "Task 1", "status": "pending"})
        client.post("/api/tasks", json={"title": "Task 2", "status": "done"})
        
        response = client.get("/api/tasks?status=pending")
        assert response.status_code == 200
        tasks = response.json()["tasks"]
        assert all(t["status"] == "pending" for t in tasks)
    
    def test_search_tasks(self, client):
        client.post("/api/tasks", json={"title": "Python Lab"})
        client.post("/api/tasks", json={"title": "Docker Lab"})
        
        response = client.get("/api/tasks?search=Python")
        assert response.status_code == 200
        assert response.json()["total"] == 1
```

### 2.3 Run Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=app --cov-report=html -v

# Run specific test file
pytest tests/test_tasks.py -v
```

---

## 💻 Part 3: Jenkins Setup

### 3.1 Access Jenkins

```bash
# Start Jenkins (from docker-compose)
docker-compose up -d jenkins

# Get initial admin password
docker exec taskflow-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

เปิด Browser: http://localhost:8080

### 3.2 Install Plugins

Install suggested plugins + เพิ่ม:
- Docker Pipeline
- Pipeline
- GitHub Integration

### 3.3 Create Pipeline Job

1. New Item → Pipeline → "taskflow-ci"
2. Pipeline from SCM → Git
3. Repository URL: your GitHub repo
4. Script Path: `Jenkinsfile`

---

## 💻 Part 4: Jenkinsfile (CI)

### 4.1 Create Jenkinsfile

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'taskflow'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Code checked out"
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
                echo "✅ Dependencies installed"
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=app --cov-report=xml --cov-report=html -v --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
                echo "✅ Docker image built"
            }
        }
    }
    
    post {
        success {
            echo '🎉 CI Pipeline completed successfully!'
        }
        failure {
            echo '❌ CI Pipeline failed!'
        }
        always {
            cleanWs()
        }
    }
}
```

---

## 📤 Submission

### Checklist

- [ ] conftest.py with test database
- [ ] Test files (≥8 test cases)
- [ ] Coverage ≥60%
- [ ] Jenkins running
- [ ] Jenkinsfile (CI stages)
- [ ] Pipeline runs successfully

### Git Commands

```bash
git checkout -b feature/lab07-testing-ci
git add .
git commit -m "Lab 7: Testing + Jenkins CI"
git push -u origin feature/lab07-testing-ci
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| pytest setup + conftest | 1.5% |
| Test cases (≥8 tests) | 2.5% |
| Coverage ≥60% | 1% |
| Jenkinsfile (CI stages) | 2% |
| Pipeline runs successfully | 1% |
| **รวม** | **8%** |

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 8
