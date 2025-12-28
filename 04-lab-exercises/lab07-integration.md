# Lab 07: Full Stack Integration

**Week 7 | Practice Lab (ไม่มีคะแนน)**

## 🎯 Objectives
- เชื่อมต่อ Frontend (Jinja2) กับ Backend (FastAPI)
- Implement Session-based Authentication
- สร้าง Login/Register Flow
- จัดการ Form Submission

## 📋 Prerequisites
- เสร็จ Lab 1-6
- เข้าใจ FastAPI และ Jinja2

## 💻 Part 1: Project Setup (15 min)

### 1.1 Project Structure
```
loan-system/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   └── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── loans.py
│   │   └── pages.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── pages/
│   │   │   ├── home.html
│   │   │   ├── dashboard.html
│   │   │   └── loans.html
│   │   └── components/
│   │       ├── navbar.html
│   │       ├── alerts.html
│   │       └── forms.html
│   └── static/
│       ├── css/
│       └── js/
├── requirements.txt
└── README.md
```

### 1.2 Requirements
```txt
fastapi==0.109.0
uvicorn==0.27.0
jinja2==3.1.3
python-multipart==0.0.6
sqlalchemy==2.0.25
passlib[bcrypt]==1.7.4
itsdangerous==2.1.2
```

## 💻 Part 2: Authentication Setup (30 min)

### 2.1 Security Module
สร้าง `app/auth/security.py`:

```python
from passlib.context import CryptContext
from itsdangerous import URLSafeTimedSerializer
import secrets

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Session management
SECRET_KEY = secrets.token_hex(32)
serializer = URLSafeTimedSerializer(SECRET_KEY)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_session_token(user_id: int, username: str) -> str:
    return serializer.dumps({"user_id": user_id, "username": username})

def verify_session_token(token: str, max_age: int = 86400):
    try:
        data = serializer.loads(token, max_age=max_age)
        return data
    except:
        return None

# In-memory session store
sessions = {}

def create_session(user_id: int, username: str, role: str) -> str:
    token = secrets.token_urlsafe(32)
    sessions[token] = {
        "user_id": user_id,
        "username": username,
        "role": role
    }
    return token

def get_session(token: str):
    return sessions.get(token)

def delete_session(token: str):
    if token in sessions:
        del sessions[token]
```

### 2.2 Authentication Dependencies
สร้าง `app/auth/dependencies.py`:

```python
from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse
from .security import get_session

def get_current_user(request: Request):
    """Get current user from session cookie"""
    token = request.cookies.get("session_token")
    
    if not token:
        return None
    
    session = get_session(token)
    return session

def require_login(request: Request):
    """Require user to be logged in"""
    user = get_current_user(request)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            headers={"Location": "/login?next=" + str(request.url.path)}
        )
    
    return user

def require_admin(request: Request):
    """Require user to be admin"""
    user = require_login(request)
    
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    
    return user
```

## 💻 Part 3: Auth Router (30 min)

### 3.1 Auth Routes
สร้าง `app/routers/auth.py`:

```python
from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from ..database import get_db
from ..auth.security import (
    hash_password, verify_password, 
    create_session, delete_session
)
from .. import crud, schemas

router = APIRouter(prefix="/auth", tags=["Authentication"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, next: str = "/dashboard"):
    return templates.TemplateResponse(
        "auth/login.html",
        {"request": request, "next": next}
    )

@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    next: str = Form("/dashboard"),
    db: Session = Depends(get_db)
):
    # Find user
    user = crud.get_user_by_username(db, username)
    
    if not user or not verify_password(password, user.password_hash):
        return templates.TemplateResponse(
            "auth/login.html",
            {
                "request": request,
                "error": "Invalid username or password",
                "next": next
            }
        )
    
    if not user.is_active:
        return templates.TemplateResponse(
            "auth/login.html",
            {
                "request": request,
                "error": "Account is disabled",
                "next": next
            }
        )
    
    # Create session
    token = create_session(user.id, user.username, user.role)
    
    # Redirect with cookie
    response = RedirectResponse(url=next, status_code=303)
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        max_age=86400,  # 24 hours
        samesite="lax"
    )
    
    return response

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse(
        "auth/register.html",
        {"request": request}
    )

@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db)
):
    errors = []
    
    # Validation
    if len(username) < 3:
        errors.append("Username must be at least 3 characters")
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    if password != confirm_password:
        errors.append("Passwords do not match")
    
    if crud.get_user_by_username(db, username):
        errors.append("Username already exists")
    
    if crud.get_user_by_email(db, email):
        errors.append("Email already registered")
    
    if errors:
        return templates.TemplateResponse(
            "auth/register.html",
            {"request": request, "errors": errors}
        )
    
    # Create user
    user = crud.create_user(
        db,
        username=username,
        email=email,
        password_hash=hash_password(password)
    )
    
    # Auto login
    token = create_session(user.id, user.username, user.role)
    
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        max_age=86400
    )
    
    return response

@router.get("/logout")
async def logout(request: Request):
    token = request.cookies.get("session_token")
    
    if token:
        delete_session(token)
    
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("session_token")
    
    return response
```

## 💻 Part 4: Page Router (30 min)

### 4.1 Page Routes
สร้าง `app/routers/pages.py`:

```python
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from ..database import get_db
from ..auth.dependencies import get_current_user, require_login
from .. import crud

router = APIRouter(tags=["Pages"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse(
        "pages/home.html",
        {"request": request, "user": user}
    )

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):
    user = require_login(request)
    
    # Get user's loans
    borrower = crud.get_borrower_by_user(db, user["user_id"])
    loans = []
    stats = {"total": 0, "active": 0, "paid": 0}
    
    if borrower:
        loans = crud.get_loans_by_borrower(db, borrower.id)
        stats = {
            "total": len(loans),
            "active": sum(1 for l in loans if l.status in ["current", "approved"]),
            "paid": sum(1 for l in loans if l.status == "paid")
        }
    
    return templates.TemplateResponse(
        "pages/dashboard.html",
        {
            "request": request,
            "user": user,
            "loans": loans,
            "stats": stats
        }
    )

@router.get("/loans", response_class=HTMLResponse)
async def loans_page(
    request: Request,
    db: Session = Depends(get_db)
):
    user = require_login(request)
    
    borrower = crud.get_borrower_by_user(db, user["user_id"])
    loans = []
    
    if borrower:
        loans = crud.get_loans_by_borrower(db, borrower.id)
    
    return templates.TemplateResponse(
        "pages/loans.html",
        {
            "request": request,
            "user": user,
            "loans": loans
        }
    )

@router.get("/loans/apply", response_class=HTMLResponse)
async def apply_loan_page(request: Request):
    user = require_login(request)
    
    return templates.TemplateResponse(
        "pages/apply_loan.html",
        {"request": request, "user": user}
    )
```

## 💻 Part 5: Templates (30 min)

### 5.1 Base Template
`app/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Loan System{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include "components/navbar.html" %}
    
    <main class="container my-4">
        {% include "components/alerts.html" %}
        {% block content %}{% endblock %}
    </main>
    
    <footer class="bg-dark text-white py-3 mt-auto">
        <div class="container text-center">
            <p class="mb-0">&copy; 2026 CSI403 Full Stack Development</p>
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 5.2 Navbar Component
`app/templates/components/navbar.html`:

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="/">
            <i class="bi bi-bank2"></i> Loan System
        </a>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/">Home</a>
                </li>
                {% if user %}
                <li class="nav-item">
                    <a class="nav-link" href="/dashboard">Dashboard</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/loans">My Loans</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/loans/apply">Apply</a>
                </li>
                {% endif %}
            </ul>
            
            <ul class="navbar-nav">
                {% if user %}
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">
                        <i class="bi bi-person-circle"></i> {{ user.username }}
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li><a class="dropdown-item" href="/profile">Profile</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="/auth/logout">Logout</a></li>
                    </ul>
                </li>
                {% else %}
                <li class="nav-item">
                    <a class="nav-link" href="/auth/login">Login</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/auth/register">Register</a>
                </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
```

### 5.3 Login Page
`app/templates/auth/login.html`:

```html
{% extends "base.html" %}

{% block title %}Login - Loan System{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-5">
        <div class="card shadow">
            <div class="card-body p-5">
                <h3 class="text-center mb-4">
                    <i class="bi bi-box-arrow-in-right"></i> Login
                </h3>
                
                {% if error %}
                <div class="alert alert-danger">{{ error }}</div>
                {% endif %}
                
                <form method="POST" action="/auth/login">
                    <input type="hidden" name="next" value="{{ next }}">
                    
                    <div class="mb-3">
                        <label class="form-label">Username</label>
                        <input type="text" name="username" class="form-control" required>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Password</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
                
                <hr>
                
                <p class="text-center mb-0">
                    Don't have an account? <a href="/auth/register">Register</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### 5.4 Dashboard Page
`app/templates/pages/dashboard.html`:

```html
{% extends "base.html" %}

{% block title %}Dashboard - Loan System{% endblock %}

{% block content %}
<h2 class="mb-4">Welcome, {{ user.username }}!</h2>

<div class="row mb-4">
    <div class="col-md-4">
        <div class="card bg-primary text-white">
            <div class="card-body">
                <h5 class="card-title">Total Loans</h5>
                <h2>{{ stats.total }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card bg-success text-white">
            <div class="card-body">
                <h5 class="card-title">Active Loans</h5>
                <h2>{{ stats.active }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card bg-info text-white">
            <div class="card-body">
                <h5 class="card-title">Paid Off</h5>
                <h2>{{ stats.paid }}</h2>
            </div>
        </div>
    </div>
</div>

<div class="card">
    <div class="card-header d-flex justify-content-between align-items-center">
        <h5 class="mb-0">Recent Loans</h5>
        <a href="/loans/apply" class="btn btn-primary btn-sm">Apply New Loan</a>
    </div>
    <div class="card-body">
        {% if loans %}
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Amount</th>
                    <th>Monthly</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for loan in loans[:5] %}
                <tr>
                    <td>#{{ loan.id }}</td>
                    <td>{{ "{:,.0f}".format(loan.loan_amount) }} THB</td>
                    <td>{{ "{:,.0f}".format(loan.monthly_payment) }} THB</td>
                    <td>
                        <span class="badge bg-{{ 'success' if loan.status == 'current' else 'secondary' }}">
                            {{ loan.status }}
                        </span>
                    </td>
                    <td>
                        <a href="/loans/{{ loan.id }}" class="btn btn-sm btn-outline-primary">View</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p class="text-muted text-center py-3">No loans yet. <a href="/loans/apply">Apply for your first loan!</a></p>
        {% endif %}
    </div>
</div>
{% endblock %}
```

## 💻 Part 6: Main Application (10 min)

### 6.1 Main App
สร้าง `app/main.py`:

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import auth, pages, loans
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loan Management System")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(auth.router)
app.include_router(pages.router)
app.include_router(loans.router)
```

## 📝 Exercise for G2: System Design

สำหรับ **G2: System Design (10%)** ใน Week 7:

### Deliverables:
1. **Architecture Diagram** แสดง:
   - Frontend Components
   - Backend Routes
   - Database Tables
   - Authentication Flow

2. **Database Design**:
   - ER Diagram
   - Table Schemas
   - Relationships

3. **UI Mockup**:
   - 5+ หน้าหลัก
   - Responsive Design

4. **API Specification**:
   - All endpoints
   - Request/Response formats

### Grading Rubric (10%):
| Criteria | Points |
|----------|:------:|
| Architecture Diagram | 2% |
| Database Design | 3% |
| UI Mockup | 3% |
| API Specification | 2% |

---

**Next:** Lab 08 - Docker Basics
