# Workshop 7: 🧪 Testing &amp; CI

## 📋 Overview
| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | pytest + Jenkins CI |

---

## 💻 CP1: pytest Setup (2%)

```bash
pip install pytest pytest-cov httpx
```

### tests/conftest.py
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)
```

---

## 💻 CP2: Write Tests (2%)

### tests/test_tasks.py
```python
def test_root(client):
    response = client.get("/")
    assert response.status_code == 200

def test_create_task(client):
    response = client.post("/api/tasks", json={"title": "Test"})
    assert response.status_code == 201

def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200

def test_not_found(client):
    response = client.get("/api/tasks/999")
    assert response.status_code == 404
```

```bash
pytest -v
pytest --cov=app
```

---

## 💻 CP3: Jenkins Setup (2%)

Add to docker-compose.yml:
```yaml
  jenkins:
    image: jenkins/jenkins:lts
    ports:
      - "8080:8080"
```

```bash
docker compose up -d jenkins
```

Open http://localhost:8080 and configure.

---

## 💻 CP4: Jenkinsfile (2%)

```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest --junitxml=results.xml'
            }
        }
    }
}
```

---

[📖 Extended →](../../docs/extended/week07-testing-strategies.md)
