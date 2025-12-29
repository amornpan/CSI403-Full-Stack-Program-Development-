# Week 2: Checkpoints

## ✅ Checkpoint 1: Git Setup (2%)

### Requirements
| # | Criteria | Pass |
|---|----------|:----:|
| 1 | `git log --oneline` แสดง commit "Initial project structure" | ⬜ |
| 2 | โฟลเดอร์ structure ครบตามที่กำหนด | ⬜ |
| 3 | Repository บน GitHub มี commit | ⬜ |

### Expected Output

```bash
$ git log --oneline
abc1234 Initial project structure
```

### Folder Structure
```
taskflow/
├── app/
│   ├── __init__.py
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
└── README.md
```

### Scoring
- ✅ ผ่านทั้ง 3 ข้อ = **2%**
- ⚠️ ผ่าน 2 ข้อ = **1%**
- ❌ ผ่าน 0-1 ข้อ = **0%**

---

## ✅ Checkpoint 2: Python Environment (2%)

### Requirements
| # | Criteria | Pass |
|---|----------|:----:|
| 1 | `pip list` แสดง fastapi, uvicorn, pydantic | ⬜ |
| 2 | ไฟล์ `requirements.txt` มี packages ครบ | ⬜ |
| 3 | ไฟล์ `app/config.py` ทำงานได้ถูกต้อง | ⬜ |

### Expected pip list (บางส่วน)

```
Package            Version
------------------ -------
fastapi            0.109.0
uvicorn            0.27.0
pydantic           2.5.3
pydantic-settings  2.1.0
```

### config.py Test

```python
>>> from app.config import settings
>>> print(settings.APP_NAME)
TaskFlow
```

### Scoring
- ✅ ผ่านทั้ง 3 ข้อ = **2%**
- ⚠️ ผ่าน 2 ข้อ = **1%**
- ❌ ผ่าน 0-1 ข้อ = **0%**

---

## ✅ Checkpoint 3: FastAPI Application (2%)

### Requirements
| # | Criteria | Pass |
|---|----------|:----:|
| 1 | Server running บน http://localhost:8000 | ⬜ |
| 2 | Swagger UI accessible at /docs | ⬜ |
| 3 | /health endpoint returns correct JSON | ⬜ |
| 4 | GitHub มี commits ทั้งหมด | ⬜ |

### Expected Responses

**GET /**
```json
{
    "message": "Welcome to TaskFlow!",
    "version": "1.0.0",
    "docs": "/docs"
}
```

**GET /health**
```json
{
    "status": "healthy",
    "app": "TaskFlow"
}
```

### Scoring
- ✅ ผ่านทั้ง 4 ข้อ = **2%**
- ⚠️ ผ่าน 2-3 ข้อ = **1%**
- ❌ ผ่าน 0-1 ข้อ = **0%**

---

## 🚀 Bonus Challenge (+2%)

### Requirements
| # | Criteria | Pass |
|---|----------|:----:|
| 1 | /info endpoint exists and returns JSON | ⬜ |
| 2 | Response includes developer name | ⬜ |
| 3 | Response includes list of endpoints | ⬜ |
| 4 | Committed and pushed to GitHub | ⬜ |

### Expected Response

**GET /info**
```json
{
    "app_name": "TaskFlow",
    "version": "1.0.0",
    "debug_mode": true,
    "endpoints": {
        "root": "/",
        "health": "/health",
        "info": "/info",
        "docs": "/docs"
    },
    "developer": "Student Name"
}
```

### Scoring
- ✅ ผ่านทั้ง 4 ข้อ = **+2% Bonus**
- ❌ ไม่ครบ = **0%**

---

## 📊 Summary

| Checkpoint | Max Score | Your Score |
|------------|:---------:|:----------:|
| Checkpoint 1: Git Setup | 2% | ⬜ |
| Checkpoint 2: Python Env | 2% | ⬜ |
| Checkpoint 3: FastAPI | 2% | ⬜ |
| Bonus Challenge | +2% | ⬜ |
| **Total** | **8%** | **⬜** |

---

## 📝 TA Notes

```
Student ID: ________________
Name: _____________________

CP1: ⬜ 0%  ⬜ 1%  ⬜ 2%
CP2: ⬜ 0%  ⬜ 1%  ⬜ 2%
CP3: ⬜ 0%  ⬜ 1%  ⬜ 2%
Bonus: ⬜ 0%  ⬜ +2%

Total: ______%

Notes: _____________________
___________________________
```
