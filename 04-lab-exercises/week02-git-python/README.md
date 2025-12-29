# Week 2: Git + Python + Project Setup

## 🎯 Workshop Goals

เมื่อจบ workshop นี้ คุณจะสามารถ:
- ใช้ Git commands พื้นฐานได้
- สร้าง Python virtual environment
- Setup โปรเจค FastAPI
- Run server และเข้าถึง API documentation

---

## ⏰ Workshop Timeline (3 ชั่วโมง)

| Time | Activity |
|------|----------|
| 00:00 - 00:30 | 📖 Mini Lecture + Demo |
| 00:30 - 01:15 | 🔨 Part 1: Git Setup |
| 01:15 - 01:30 | ☕ Break |
| 01:30 - 02:15 | 🔨 Part 2: Python Environment |
| 02:15 - 02:45 | 🔨 Part 3: FastAPI Hello World |
| 02:45 - 03:00 | 🚀 Challenge (Bonus) |

---

## 🔨 Part 1: Git Setup (45 นาที)

### Step 1.1: Configure Git

เปิด Terminal (Command Prompt หรือ Git Bash) แล้วรันคำสั่ง:

```bash
# ตั้งชื่อ (ใช้ชื่อจริงของคุณ)
git config --global user.name "Your Name"

# ตั้ง email (ใช้ email เดียวกับ GitHub)
git config --global user.email "your.email@example.com"

# ตรวจสอบการตั้งค่า
git config --list
```

### Step 1.2: Create GitHub Repository

1. ไปที่ https://github.com
2. Click **"New repository"**
3. ตั้งชื่อ: `taskflow`
4. เลือก **Public**
5. ✅ Check "Add a README file"
6. Click **"Create repository"**

### Step 1.3: Clone Repository

```bash
# Clone repository มาที่เครื่อง
git clone https://github.com/YOUR_USERNAME/taskflow.git

# เข้าไปในโฟลเดอร์
cd taskflow

# ตรวจสอบ status
git status
```

### Step 1.4: Create Project Structure

```bash
# สร้างโฟลเดอร์
mkdir -p app/models app/schemas app/routes app/templates app/static/css app/static/js tests

# สร้างไฟล์ __init__.py
touch app/__init__.py
touch app/models/__init__.py
touch app/schemas/__init__.py
touch app/routes/__init__.py
touch tests/__init__.py
```

> **Windows Note:** ถ้าใช้ Command Prompt ให้ใช้ `mkdir` แยกทีละโฟลเดอร์ หรือใช้ Git Bash

### Step 1.5: First Commit

```bash
# ดู status
git status

# เพิ่มไฟล์ทั้งหมด
git add .

# Commit
git commit -m "Initial project structure"

# Push ขึ้น GitHub
git push origin main

# ดู history
git log --oneline
```

### ✅ Checkpoint 1 (2%)

**เรียก TA เพื่อตรวจ:**
- [ ] แสดง `git log --oneline` ที่มี commit "Initial project structure"
- [ ] แสดงโฟลเดอร์ structure ใน VS Code
- [ ] แสดง repository บน GitHub

---

## 🔨 Part 2: Python Environment (45 นาที)

### Step 2.1: Create Virtual Environment

```bash
# ตรวจสอบ Python version
python --version

# สร้าง virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# ควรเห็น (venv) หน้า prompt
```

### Step 2.2: Create requirements.txt

สร้างไฟล์ `requirements.txt` ใน root folder:

```
# Web Framework
fastapi==0.109.0
uvicorn==0.27.0

# Validation
pydantic==2.5.3
pydantic-settings==2.1.0

# Database (จะใช้ใน Week 4)
sqlalchemy==2.0.25

# Templates (จะใช้ใน Week 6)
jinja2==3.1.3

# Testing (จะใช้ใน Week 8)
pytest==7.4.4
httpx==0.26.0
```

### Step 2.3: Install Packages

```bash
# ติดตั้ง packages
pip install -r requirements.txt

# ตรวจสอบ packages ที่ติดตั้ง
pip list

# ควรเห็น fastapi, uvicorn, pydantic ฯลฯ
```

### Step 2.4: Create Config File

สร้างไฟล์ `app/config.py`:

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    APP_NAME: str = "TaskFlow"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database settings (จะใช้ใน Week 4)
    DATABASE_URL: str = "sqlite:///./taskflow.db"
    
    class Config:
        env_file = ".env"


# Create settings instance
settings = Settings()
```

### Step 2.5: Commit Changes

```bash
git add .
git commit -m "Add Python environment and config"
git push origin main
```

### ✅ Checkpoint 2 (2%)

**เรียก TA เพื่อตรวจ:**
- [ ] แสดง `pip list` ที่มี fastapi, uvicorn, pydantic
- [ ] แสดงไฟล์ `requirements.txt`
- [ ] แสดงไฟล์ `app/config.py`

---

## 🔨 Part 3: FastAPI Hello World (30 นาที)

### Step 3.1: Create Main Application

สร้างไฟล์ `app/main.py`:

```python
from fastapi import FastAPI
from app.config import settings

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="Task Management System - CSI403",
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    """Root endpoint - Welcome message"""
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME
    }
```

### Step 3.2: Run the Server

```bash
# รัน server (ต้อง activate venv ก่อน)
uvicorn app.main:app --reload

# ควรเห็น:
# INFO:     Uvicorn running on http://127.0.0.1:8000
# INFO:     Started reloader process
```

### Step 3.3: Test the API

เปิด Browser แล้วไปที่:

1. **http://localhost:8000** - ดู welcome message
2. **http://localhost:8000/health** - ดู health status
3. **http://localhost:8000/docs** - ดู Swagger UI (API documentation)
4. **http://localhost:8000/redoc** - ดู ReDoc (alternative docs)

### Step 3.4: Final Commit

```bash
# หยุด server ด้วย Ctrl+C

git add .
git commit -m "Add FastAPI application"
git push origin main
```

### ✅ Checkpoint 3 (2%)

**เรียก TA เพื่อตรวจ:**
- [ ] Server running บน http://localhost:8000
- [ ] แสดง Swagger UI ที่ /docs
- [ ] แสดง health endpoint response
- [ ] แสดง GitHub repository ที่มี commits ทั้งหมด

---

## 🚀 Challenge: Bonus (+2%)

**เสร็จเร็ว? ลองทำเพิ่ม:**

### Challenge: Add Info Endpoint

สร้าง endpoint `/info` ที่ return ข้อมูลเพิ่มเติม:

```python
@app.get("/info")
def app_info():
    """Application information endpoint"""
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "debug_mode": settings.DEBUG,
        "endpoints": {
            "root": "/",
            "health": "/health",
            "info": "/info",
            "docs": "/docs"
        },
        "developer": "YOUR_NAME"  # ใส่ชื่อคุณ
    }
```

### Bonus Checkpoint

**เรียก TA เพื่อตรวจ:**
- [ ] แสดง /info endpoint ที่มีข้อมูลครบ
- [ ] มีชื่อ developer เป็นชื่อตัวเอง
- [ ] Commit และ push ขึ้น GitHub แล้ว

---

## 📁 Final Project Structure

```
taskflow/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── routes/
│   │   └── __init__.py
│   ├── templates/
│   └── static/
│       ├── css/
│       └── js/
├── tests/
│   └── __init__.py
├── venv/
├── requirements.txt
└── README.md
```

---

## 🆘 Troubleshooting

### "python not found"
- ตรวจสอบว่าติดตั้ง Python แล้ว
- ลองใช้ `python3` แทน `python`

### "pip not found"
- ลองใช้ `python -m pip` แทน `pip`

### "venv\Scripts\activate ไม่ทำงาน"
- ใช้ PowerShell: `.\venv\Scripts\Activate.ps1`
- หรือใช้ Git Bash: `source venv/Scripts/activate`

### "Port 8000 already in use"
- ใช้ port อื่น: `uvicorn app.main:app --reload --port 8001`

### "ModuleNotFoundError: No module named 'app'"
- ตรวจสอบว่าอยู่ใน root folder ของ project
- ตรวจสอบว่ามีไฟล์ `app/__init__.py`

---

## 📖 Next Week Preview

**Week 3: FastAPI CRUD**
- สร้าง Task API ครบ 5 endpoints
- ใช้ Pydantic สำหรับ validation
- Error handling

---

**🎉 Congratulations! You've completed Week 2 Workshop!**
