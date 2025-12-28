# Lab 01: Git + Python + Project Setup

**Week 2 | 8%**

## 🎯 Objectives

เมื่อจบ Lab นี้ นักศึกษาจะสามารถ:
- ใช้ Git commands พื้นฐานได้
- ใช้ GitHub workflow (Branch, PR, Merge)
- สร้างโครงสร้างโปรเจค Python ที่ถูกต้อง
- ตั้งค่า Virtual Environment

## 📋 Prerequisites

- Python 3.11+ installed
- Git installed
- VS Code with Python extension
- GitHub account

---

## 💻 Part 1: Git Setup (30 min)

### 1.1 Configure Git

```bash
# ตั้งค่าชื่อและ email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# ตรวจสอบ
git config --list
```

### 1.2 Create GitHub Repository

1. ไปที่ https://github.com/new
2. Repository name: `taskflow`
3. Description: `CSI403 Full Stack Development - Task Management System`
4. ✅ Public
5. ✅ Add README.md
6. ✅ Add .gitignore (Python)
7. Click **Create repository**

### 1.3 Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/taskflow.git
cd taskflow
```

---

## 💻 Part 2: Project Structure (40 min)

### 2.1 Create Folder Structure

```bash
# สร้างโครงสร้างโปรเจค
mkdir -p app/{models,schemas,routes,templates,static/{css,js,images}}
mkdir tests
touch app/__init__.py
touch app/main.py
touch app/config.py
touch app/database.py
touch app/models/__init__.py
touch app/schemas/__init__.py
touch app/routes/__init__.py
touch tests/__init__.py
```

### 2.2 โครงสร้างที่ได้

```
taskflow/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── config.py         # Configuration settings
│   ├── database.py       # Database connection
│   ├── models/           # SQLAlchemy models
│   │   └── __init__.py
│   ├── schemas/          # Pydantic schemas
│   │   └── __init__.py
│   ├── routes/           # API routes
│   │   └── __init__.py
│   ├── templates/        # Jinja2 templates
│   └── static/           # Static files
│       ├── css/
│       ├── js/
│       └── images/
├── tests/                # Test files
│   └── __init__.py
├── .gitignore
├── requirements.txt
└── README.md
```

### 2.3 Create requirements.txt

```bash
# สร้างไฟล์ requirements.txt
cat > requirements.txt << 'EOF'
# Web Framework
fastapi==0.109.0
uvicorn==0.27.0

# Validation
pydantic==2.5.3
pydantic-settings==2.1.0
python-multipart==0.0.6

# Database
sqlalchemy==2.0.25
pyodbc==5.0.1

# Templates
jinja2==3.1.3

# Security
bcrypt==4.1.2
python-jose==3.3.0

# Testing
pytest==7.4.4
pytest-cov==4.1.0
httpx==0.26.0

# Development
python-dotenv==1.0.0
EOF
```

### 2.4 Create Virtual Environment

```bash
# สร้าง virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Part 3: Initial Code (30 min)

### 3.1 Create app/config.py

```python
# app/config.py
"""Application configuration settings."""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    APP_NAME: str = "TaskFlow"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "mssql+pyodbc://sa:YourStrong@Password123@localhost:1433/taskflow?driver=ODBC+Driver+17+for+SQL+Server"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### 3.2 Create app/main.py

```python
# app/main.py
"""TaskFlow - Task Management System."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import settings

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="Task Management System for CSI403 Full Stack Development",
    version=settings.APP_VERSION,
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def root():
    """Root endpoint - Health check."""
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
```

### 3.3 Update .gitignore

```bash
cat > .gitignore << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment variables
.env
.env.local

# Database
*.db
*.sqlite

# Logs
*.log

# Testing
.pytest_cache/
.coverage
htmlcov/

# Build
dist/
build/
*.egg-info/

# OS
.DS_Store
Thumbs.db
EOF
```

### 3.4 Update README.md

```markdown
# TaskFlow - Task Management System

CSI403 Full Stack Development - มหาวิทยาลัยศรีปทุม วิทยาเขตชลบุรี

## 📋 Description

ระบบจัดการงาน (Task Management System) สำหรับวิชา CSI403

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python 3.11+
- **Database:** MSSQL, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5, Jinja2
- **DevOps:** Docker, Jenkins

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker Desktop

### Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/taskflow.git
cd taskflow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

### Access

- App: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📁 Project Structure

```
taskflow/
├── app/
│   ├── main.py           # FastAPI app
│   ├── config.py         # Settings
│   ├── database.py       # DB connection
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── routes/           # API routes
│   ├── templates/        # Jinja2 templates
│   └── static/           # CSS, JS, images
├── tests/                # Test files
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── Jenkinsfile
```

## 👤 Author

- **Name:** [Your Name]
- **Student ID:** [Your ID]
- **Email:** [Your Email]

## 📝 License

MIT License
```

---

## 💻 Part 4: Git Workflow (30 min)

### 4.1 Check Status

```bash
git status
```

### 4.2 Add Files

```bash
git add .
```

### 4.3 Commit

```bash
git commit -m "Lab 1: Initial project setup - TaskFlow structure"
```

### 4.4 Push to GitHub

```bash
git push origin main
```

### 4.5 Create Development Branch

```bash
# สร้าง branch develop
git checkout -b develop

# Push branch ใหม่
git push -u origin develop
```

### 4.6 Feature Branch Workflow

```bash
# สร้าง feature branch
git checkout -b feature/add-hello-endpoint

# แก้ไข app/main.py - เพิ่ม endpoint ใหม่
```

เพิ่มใน `app/main.py`:

```python
@app.get("/hello/{name}")
def hello(name: str):
    """Say hello to someone."""
    return {"message": f"Hello, {name}! Welcome to TaskFlow."}
```

```bash
# Commit
git add .
git commit -m "Add hello endpoint"

# Push feature branch
git push -u origin feature/add-hello-endpoint
```

### 4.7 Create Pull Request

1. ไปที่ GitHub repository
2. Click **"Compare & pull request"**
3. Base: `develop` ← Compare: `feature/add-hello-endpoint`
4. Title: "Add hello endpoint"
5. Description: "Added /hello/{name} endpoint"
6. Click **"Create pull request"**
7. Click **"Merge pull request"**
8. Click **"Confirm merge"**

### 4.8 Update Local

```bash
git checkout develop
git pull origin develop
```

---

## 💻 Part 5: Run and Test (20 min)

### 5.1 Run Development Server

```bash
# ต้อง activate venv ก่อน
uvicorn app.main:app --reload
```

### 5.2 Test Endpoints

เปิด Browser:

- http://localhost:8000 → Root endpoint
- http://localhost:8000/health → Health check
- http://localhost:8000/hello/John → Hello endpoint
- http://localhost:8000/docs → Swagger UI

### 5.3 Screenshot

ถ่าย Screenshot:
1. Swagger UI (/docs)
2. Hello endpoint response
3. GitHub repository

---

## 📤 Submission

### Checklist

- [ ] GitHub repository สร้างแล้ว
- [ ] โครงสร้างโปรเจคถูกต้อง
- [ ] requirements.txt ครบ
- [ ] app/main.py ทำงานได้
- [ ] app/config.py ตั้งค่าถูกต้อง
- [ ] .gitignore ครบ
- [ ] README.md อัปเดตแล้ว
- [ ] ใช้ Branch + PR workflow
- [ ] Server รันได้ (uvicorn)

### Submit

1. Push ทุกอย่างขึ้น GitHub
2. ส่ง GitHub Repository URL ใน Google Form

### Repository URL Format

```
https://github.com/YOUR_USERNAME/taskflow
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| GitHub repo + โครงสร้างถูกต้อง | 2% |
| requirements.txt + venv | 1% |
| app/main.py + app/config.py | 2% |
| Git workflow (Branch + PR) | 2% |
| README.md + Documentation | 1% |
| **รวม** | **8%** |

---

## 📚 Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 2
