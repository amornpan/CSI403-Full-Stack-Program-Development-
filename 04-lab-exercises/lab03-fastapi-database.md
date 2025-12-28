# Lab 03: FastAPI + Database (MSSQL + SQLAlchemy)

**Week 4 | 8%**

## 🎯 Objectives

- รัน MSSQL บน Docker
- ใช้ SQLAlchemy ORM สร้าง Models
- สร้าง Relationships ระหว่าง Tables
- เชื่อม FastAPI กับ Database

---

## 💻 Part 1: MSSQL Docker (20 min)

### 1.1 Run MSSQL Container

```bash
docker run -e "ACCEPT_EULA=Y" \
  -e "SA_PASSWORD=YourStrong@Password123" \
  -p 1433:1433 \
  --name mssql-taskflow \
  -d mcr.microsoft.com/mssql/server:2022-latest
```

### 1.2 Verify & Create Database

```bash
# Check container running
docker ps

# Connect and create database
docker exec -it mssql-taskflow /opt/mssql-tools/bin/sqlcmd \
  -S localhost -U sa -P "YourStrong@Password123" \
  -Q "CREATE DATABASE taskflow"
```

---

## 💻 Part 2: SQLAlchemy Setup (30 min)

### 2.1 Update app/database.py

```python
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)
```

### 2.2 Update app/config.py

```python
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "TaskFlow"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    DATABASE_URL: str = "mssql+pyodbc://sa:YourStrong@Password123@localhost:1433/taskflow?driver=ODBC+Driver+17+for+SQL+Server"
    SECRET_KEY: str = "your-secret-key"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

---

## 💻 Part 3: SQLAlchemy Models (40 min)

### 3.1 Create User Model

สร้างไฟล์ `app/models/user.py`:

```python
# app/models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")
    categories = relationship("Category", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
```

### 3.2 Create Category Model

สร้างไฟล์ `app/models/category.py`:

```python
# app/models/category.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    color = Column(String(7), default="#3498db")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    owner = relationship("User", back_populates="categories")
    tasks = relationship("Task", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
```

### 3.3 Create Task Model

สร้างไฟล์ `app/models/task.py`:

```python
# app/models/task.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(20), default="pending")
    priority = Column(String(20), default="medium")
    due_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}')>"
```

### 3.4 Update app/models/__init__.py

```python
# app/models/__init__.py
from .user import User
from .category import Category
from .task import Task
```

---

## 💻 Part 4: Update Schemas (20 min)

### 4.1 Create User Schema

สร้างไฟล์ `app/schemas/user.py`:

```python
# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
```

### 4.2 Create Category Schema

สร้างไฟล์ `app/schemas/category.py`:

```python
# app/schemas/category.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    color: str = Field(default="#3498db", pattern="^#[0-9A-Fa-f]{6}$")

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")

class CategoryResponse(BaseModel):
    id: int
    name: str
    color: str
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
```

### 4.3 Update app/schemas/__init__.py

```python
# app/schemas/__init__.py
from .user import UserCreate, UserResponse
from .category import CategoryCreate, CategoryUpdate, CategoryResponse
from .task import (
    TaskStatus, TaskPriority, TaskCreate, TaskUpdate, TaskResponse, TaskListResponse
)
```

---

## 💻 Part 5: Update API Routes (40 min)

### 5.1 Update Task Routes

```python
# app/routes/tasks.py
from fastapi import APIRouter, HTTPException, Depends, Query, status
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models import Task, Category
from app.schemas import TaskCreate, TaskUpdate, TaskResponse, TaskListResponse, TaskStatus, TaskPriority

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

def get_current_user_id():
    return 1  # Temporary

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    
    if task.category_id:
        category = db.query(Category).filter(Category.id == task.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
    
    db_task = Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=TaskListResponse)
def list_tasks(
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    category_id: Optional[int] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    user_id = get_current_user_id()
    query = db.query(Task).filter(Task.user_id == user_id)
    
    if status:
        query = query.filter(Task.status == status.value)
    if priority:
        query = query.filter(Task.priority == priority.value)
    if category_id:
        query = query.filter(Task.category_id == category_id)
    if search:
        query = query.filter(Task.title.contains(search))
    
    tasks = query.order_by(Task.created_at.desc()).all()
    return {"total": len(tasks), "tasks": tasks}

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        if hasattr(value, 'value'):  # Enum
            value = value.value
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
```

### 5.2 Create Category Routes

สร้างไฟล์ `app/routes/categories.py`:

```python
# app/routes/categories.py
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(prefix="/api/categories", tags=["Categories"])

def get_current_user_id():
    return 1

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    db_category = Category(**category.model_dump(), user_id=user_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=List[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    return db.query(Category).filter(Category.user_id == user_id).all()

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    category = db.query(Category).filter(
        Category.id == category_id, Category.user_id == user_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, update: CategoryUpdate, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    category = db.query(Category).filter(
        Category.id == category_id, Category.user_id == user_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    category = db.query(Category).filter(
        Category.id == category_id, Category.user_id == user_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
```

### 5.3 Create User Routes (Basic)

สร้างไฟล์ `app/routes/users.py`:

```python
# app/routes/users.py
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import bcrypt

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/api/users", tags=["Users"])

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

### 5.4 Update app/routes/__init__.py

```python
# app/routes/__init__.py
from .tasks import router as tasks_router
from .categories import router as categories_router
from .users import router as users_router
```

### 5.5 Update app/main.py

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import create_tables
from app.routes import tasks_router, categories_router, users_router

app = FastAPI(
    title=settings.APP_NAME,
    description="TaskFlow - Task Management System",
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)
app.include_router(categories_router)
app.include_router(users_router)

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}!", "version": settings.APP_VERSION}

@app.get("/health")
def health():
    return {"status": "healthy", "app": settings.APP_NAME}
```

---

## 💻 Part 6: Test the API (20 min)

### 6.1 Run Server

```bash
uvicorn app.main:app --reload
```

### 6.2 Create Test User

```bash
curl -X POST "http://localhost:8000/api/users" \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "email": "john@example.com", "password": "password123"}'
```

### 6.3 Create Category

```bash
curl -X POST "http://localhost:8000/api/categories" \
  -H "Content-Type: application/json" \
  -d '{"name": "Study", "color": "#3498db"}'
```

### 6.4 Create Task with Category

```bash
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete Lab 3", "priority": "high", "category_id": 1}'
```

### 6.5 List Tasks with Filter

```bash
curl "http://localhost:8000/api/tasks?priority=high"
```

---

## 📤 Submission

### Checklist

- [ ] MSSQL Docker running
- [ ] SQLAlchemy Models (User, Category, Task)
- [ ] Relationships work correctly
- [ ] Task CRUD with Database
- [ ] Category CRUD
- [ ] User registration
- [ ] Swagger docs work

### Git Commands

```bash
git checkout -b feature/lab03-database
git add .
git commit -m "Lab 3: FastAPI + Database (MSSQL + SQLAlchemy)"
git push -u origin feature/lab03-database
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| MSSQL Docker + Connection | 1.5% |
| SQLAlchemy Models (3 tables) | 2% |
| Relationships ถูกต้อง | 1.5% |
| CRUD APIs work with DB | 2% |
| Code Quality | 1% |
| **รวม** | **8%** |

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 4
