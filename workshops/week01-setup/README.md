# Workshop 1: 🚀 Setup &amp; First API

## 📋 Workshop Overview

| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 checkpoints × 2%) |
| **Goal** | ติดตั้งเครื่องมือ + สร้าง API แรก |

---

## 🎯 Learning Objectives

- ✅ ติดตั้ง Python, Git, VS Code, Docker ได้
- ✅ สร้าง GitHub Repository ได้
- ✅ สร้าง Python Virtual Environment ได้
- ✅ สร้าง FastAPI Application ได้

---

## ⏰ Workshop Timeline

| Time | Duration | Activity |
|:----:|:--------:|----------|
| 0:00 | 15 min | 📖 Quick Review |
| 0:15 | 30 min | 💻 CP1: Install Tools |
| 0:45 | 30 min | 💻 CP2: GitHub Setup |
| 1:15 | 30 min | 💻 CP3: Project Setup |
| 1:45 | 30 min | 💻 CP4: First API |
| 2:15 | 15 min | ✅ Wrap-up &amp; Scoring |

---

## 💻 Checkpoint 1: Install Tools (2%)

### Step 1.1: Verify Installations

```bash
python --version    # Python 3.11.x
git --version       # git version 2.x.x
docker --version    # Docker version 24.x.x
code --version      # 1.x.x
```

### ✅ CP1 Checklist

| Task | Status |
|------|:------:|
| Python 3.11+ installed | ⬜ |
| Git installed | ⬜ |
| VS Code + Extensions | ⬜ |
| Docker Desktop running | ⬜ |

---

## 💻 Checkpoint 2: GitHub Setup (2%)

### Step 2.1: Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 2.2: Create Repository

1. GitHub.com → New repository
2. Name: `taskflow`
3. ✅ Add README file
4. Create repository

### Step 2.3: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/taskflow.git
cd taskflow
code .
```

### ✅ CP2 Checklist

| Task | Status |
|------|:------:|
| Git configured | ⬜ |
| Repository created | ⬜ |
| Repository cloned | ⬜ |

---

## 💻 Checkpoint 3: Project Setup (2%)

### Step 3.1: Create Folders

```bash
mkdir app app\routes app\models app\schemas app\templates app\static tests
```

### Step 3.2: Create Virtual Environment

```bash
conda activate csi403
# หรือ
python -m venv venv
venv\Scripts\activate
```

### Step 3.3: Create requirements.txt

```
fastapi==0.109.0
uvicorn==0.27.0
pydantic==2.5.3
pydantic-settings==2.1.0
```

### Step 3.4: Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ CP3 Checklist

| Task | Status |
|------|:------:|
| Folder structure created | ⬜ |
| Environment activated | ⬜ |
| Dependencies installed | ⬜ |

---

## 💻 Checkpoint 4: First API (2%)

### Step 4.1: Create app/config.py

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "TaskFlow"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

settings = Settings()
```

### Step 4.2: Create app/main.py

```python
from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

### Step 4.3: Create app/__init__.py

```python
# Empty file
```

### Step 4.4: Run Server

```bash
uvicorn app.main:app --reload
```

### Step 4.5: Test

- http://localhost:8000
- http://localhost:8000/docs
- http://localhost:8000/health

### Step 4.6: Commit

```bash
git add .
git commit -m "Initial project setup with FastAPI"
git push
```

### ✅ CP4 Checklist

| Task | Status |
|------|:------:|
| config.py created | ⬜ |
| main.py created | ⬜ |
| Server running | ⬜ |
| Swagger UI works | ⬜ |
| Code pushed | ⬜ |

---

## 🎉 Workshop Complete!

**Next Week:** CRUD Operations

[📖 Extended: Git Advanced →](../../docs/extended/week01-git-advanced.md)
