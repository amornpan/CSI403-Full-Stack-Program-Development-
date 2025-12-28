# Lab 05: Jinja2 Templates + Full Integration

**Week 6 | 8%**

## 🎯 Objectives

- ใช้ Jinja2 Template Engine
- สร้าง Template Inheritance (base.html)
- เชื่อม Frontend กับ Backend
- สร้าง Login/Logout Flow

---

## 💻 Part 1: Base Template

### 1.1 Create base.html

สร้างไฟล์ `app/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TaskFlow{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <link href="{{ url_for('static', path='css/style.css') }}" rel="stylesheet">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% if user %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/dashboard">
                <i class="bi bi-check2-square"></i> TaskFlow
            </a>
            <div class="navbar-nav me-auto">
                <a class="nav-link" href="/dashboard">Dashboard</a>
                <a class="nav-link" href="/tasks">Tasks</a>
                <a class="nav-link" href="/categories">Categories</a>
            </div>
            <div class="navbar-nav">
                <span class="nav-link"><i class="bi bi-person"></i> {{ user.username }}</span>
                <a class="nav-link" href="/logout">Logout</a>
            </div>
        </div>
    </nav>
    {% endif %}

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                <div class="alert alert-{{ category }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', path='js/main.js') }}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 💻 Part 2: Page Templates

### 2.1 Login Page

สร้างไฟล์ `app/templates/auth/login.html`:

```html
{% extends "base.html" %}
{% block title %}Login - TaskFlow{% endblock %}

{% block content %}
<div class="row justify-content-center mt-5">
    <div class="col-md-4">
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h4><i class="bi bi-box-arrow-in-right"></i> Login</h4>
            </div>
            <div class="card-body">
                <form method="POST" action="/login">
                    <div class="mb-3">
                        <label class="form-label">Email</label>
                        <input type="email" name="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Password</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
                <hr>
                <p class="text-center">Don't have account? <a href="/register">Register</a></p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### 2.2 Dashboard Page

สร้างไฟล์ `app/templates/dashboard.html`:

```html
{% extends "base.html" %}
{% block title %}Dashboard - TaskFlow{% endblock %}

{% block content %}
<h1><i class="bi bi-speedometer2"></i> Dashboard</h1>

<div class="row mt-4">
    <div class="col-md-3">
        <div class="card bg-warning text-dark">
            <div class="card-body text-center">
                <h2>{{ stats.pending }}</h2>
                <p>Pending</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-primary text-white">
            <div class="card-body text-center">
                <h2>{{ stats.in_progress }}</h2>
                <p>In Progress</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-success text-white">
            <div class="card-body text-center">
                <h2>{{ stats.done }}</h2>
                <p>Done</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-info text-white">
            <div class="card-body text-center">
                <h2>{{ stats.total }}</h2>
                <p>Total</p>
            </div>
        </div>
    </div>
</div>

<div class="card mt-4">
    <div class="card-header">
        <i class="bi bi-calendar"></i> Upcoming Tasks
    </div>
    <ul class="list-group list-group-flush">
        {% for task in upcoming_tasks %}
        <li class="list-group-item d-flex justify-content-between">
            <span>{{ task.title }}</span>
            <small>{{ task.due_date.strftime('%d/%m/%Y') if task.due_date else 'No date' }}</small>
        </li>
        {% else %}
        <li class="list-group-item text-center text-muted">No upcoming tasks</li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

### 2.3 Tasks List Page

สร้างไฟล์ `app/templates/tasks/list.html`:

```html
{% extends "base.html" %}
{% block title %}Tasks - TaskFlow{% endblock %}

{% block content %}
<div class="d-flex justify-content-between mb-4">
    <h1><i class="bi bi-list-task"></i> Tasks</h1>
    <a href="/tasks/create" class="btn btn-success">
        <i class="bi bi-plus"></i> New Task
    </a>
</div>

<div class="card">
    <table class="table table-hover mb-0">
        <thead class="table-dark">
            <tr>
                <th>Title</th>
                <th>Status</th>
                <th>Priority</th>
                <th>Due Date</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for task in tasks %}
            <tr>
                <td>{{ task.title }}</td>
                <td>
                    <span class="badge bg-{{ 'warning' if task.status == 'pending' else 'primary' if task.status == 'in_progress' else 'success' }}">
                        {{ task.status }}
                    </span>
                </td>
                <td>
                    <span class="badge bg-{{ 'success' if task.priority == 'low' else 'warning' if task.priority == 'medium' else 'danger' }}">
                        {{ task.priority }}
                    </span>
                </td>
                <td>{{ task.due_date.strftime('%d/%m/%Y') if task.due_date else '-' }}</td>
                <td>
                    <a href="/tasks/{{ task.id }}/edit" class="btn btn-sm btn-outline-primary">Edit</a>
                    <form action="/tasks/{{ task.id }}/delete" method="POST" class="d-inline" onsubmit="return confirm('Delete?')">
                        <button class="btn btn-sm btn-outline-danger">Delete</button>
                    </form>
                </td>
            </tr>
            {% else %}
            <tr>
                <td colspan="5" class="text-center py-4">No tasks found</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
```

---

## 💻 Part 3: Routes with Templates

### 3.1 Create Page Routes

สร้างไฟล์ `app/routes/pages.py`:

```python
# app/routes/pages.py
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import bcrypt

from app.database import get_db
from app.models import User, Task, Category

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_current_user(request: Request, db: Session):
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return db.query(User).filter(User.id == user_id).first()


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request, "user": None})


@router.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        return templates.TemplateResponse("auth/login.html", {
            "request": request, "user": None, "error": "Invalid credentials"
        })
    request.session["user_id"] = user.id
    return RedirectResponse(url="/dashboard", status_code=302)


@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=302)


@router.get("/dashboard")
def dashboard(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login")
    
    stats = {
        "pending": db.query(Task).filter(Task.user_id == user.id, Task.status == "pending").count(),
        "in_progress": db.query(Task).filter(Task.user_id == user.id, Task.status == "in_progress").count(),
        "done": db.query(Task).filter(Task.user_id == user.id, Task.status == "done").count(),
        "total": db.query(Task).filter(Task.user_id == user.id).count(),
    }
    
    upcoming = db.query(Task).filter(Task.user_id == user.id, Task.status != "done").order_by(Task.due_date).limit(5).all()
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request, "user": user, "stats": stats, "upcoming_tasks": upcoming
    })


@router.get("/tasks")
def tasks_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login")
    
    tasks = db.query(Task).filter(Task.user_id == user.id).order_by(Task.created_at.desc()).all()
    
    return templates.TemplateResponse("tasks/list.html", {
        "request": request, "user": user, "tasks": tasks
    })
```

---

## 📤 Submission

### Checklist

- [ ] base.html with template inheritance
- [ ] Login/Logout flow works
- [ ] Dashboard shows stats
- [ ] Tasks CRUD via web pages
- [ ] Flash messages work
- [ ] Session management

### Git Commands

```bash
git checkout -b feature/lab05-jinja2
git add .
git commit -m "Lab 5: Jinja2 templates + full integration"
git push -u origin feature/lab05-jinja2
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| Template Inheritance | 2% |
| Login/Logout Flow | 2% |
| Dashboard + Tasks Pages | 2% |
| Form Handling + Flash | 1.5% |
| Code Quality | 0.5% |
| **รวม** | **8%** |

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 6
