# Lab 02: FastAPI CRUD

**Week 3 | 8%**

## 🎯 Objectives

เมื่อจบ Lab นี้ นักศึกษาจะสามารถ:
- สร้าง REST API ด้วย FastAPI
- ใช้ Pydantic สำหรับ Data Validation
- สร้าง CRUD Operations (Create, Read, Update, Delete)
- ใช้ Swagger UI สำหรับ API Documentation

## 📋 Prerequisites

- Lab 1 เสร็จแล้ว (มี taskflow project structure)
- Python 3.11+ และ FastAPI installed

---

## 💻 Part 1: Task Schema (30 min)

### 1.1 Create Pydantic Schemas

สร้างไฟล์ `app/schemas/task.py`:

```python
# app/schemas/task.py
"""Pydantic schemas for Task."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    """Task status enumeration."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(str, Enum):
    """Task priority enumeration."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskBase(BaseModel):
    """Base schema for Task."""
    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")
    status: TaskStatus = Field(default=TaskStatus.PENDING, description="Task status")
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM, description="Task priority")
    due_date: Optional[datetime] = Field(None, description="Due date")


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Complete Lab 2",
                "description": "Finish FastAPI CRUD lab",
                "status": "pending",
                "priority": "high",
                "due_date": "2026-01-20T23:59:59"
            }
        }


class TaskUpdate(BaseModel):
    """Schema for updating a task."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None


class TaskResponse(TaskBase):
    """Schema for task response."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TaskListResponse(BaseModel):
    """Schema for paginated task list."""
    total: int
    tasks: list[TaskResponse]
```

### 1.2 Update app/schemas/__init__.py

```python
# app/schemas/__init__.py
from .task import (
    TaskStatus,
    TaskPriority,
    TaskBase,
    TaskCreate,
    TaskUpdate,
    TaskResponse,
    TaskListResponse,
)
```

---

## 💻 Part 2: In-Memory Database (20 min)

สร้างไฟล์ `app/database.py` (In-Memory version):

```python
# app/database.py
"""In-Memory database for Task (temporary - will be replaced with MSSQL)."""

from datetime import datetime
from typing import Dict, List, Optional

# In-memory storage
tasks_db: Dict[int, dict] = {}
task_id_counter = 0


def get_next_id() -> int:
    """Generate next task ID."""
    global task_id_counter
    task_id_counter += 1
    return task_id_counter


def create_task(task_data: dict) -> dict:
    """Create a new task."""
    task_id = get_next_id()
    
    task = {
        "id": task_id,
        **task_data,
        "created_at": datetime.now(),
        "updated_at": None
    }
    
    tasks_db[task_id] = task
    return task


def get_task(task_id: int) -> Optional[dict]:
    """Get task by ID."""
    return tasks_db.get(task_id)


def get_all_tasks() -> List[dict]:
    """Get all tasks."""
    return list(tasks_db.values())


def update_task(task_id: int, update_data: dict) -> Optional[dict]:
    """Update a task."""
    if task_id not in tasks_db:
        return None
    
    task = tasks_db[task_id]
    
    for key, value in update_data.items():
        if value is not None:
            task[key] = value
    
    task["updated_at"] = datetime.now()
    tasks_db[task_id] = task
    
    return task


def delete_task(task_id: int) -> bool:
    """Delete a task."""
    if task_id in tasks_db:
        del tasks_db[task_id]
        return True
    return False


def filter_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None
) -> List[dict]:
    """Filter tasks by status, priority, or search term."""
    tasks = list(tasks_db.values())
    
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    
    if priority:
        tasks = [t for t in tasks if t["priority"] == priority]
    
    if search:
        search_lower = search.lower()
        tasks = [t for t in tasks if search_lower in t["title"].lower()]
    
    return tasks
```

---

## 💻 Part 3: Task API Routes (40 min)

สร้างไฟล์ `app/routes/tasks.py`:

```python
# app/routes/tasks.py
"""Task API routes."""

from fastapi import APIRouter, HTTPException, Query, Path, status
from typing import Optional

from app.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
    TaskListResponse,
    TaskStatus,
    TaskPriority,
)
from app import database as db

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


# ============ CREATE ============

@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Create a new task with title, description, status, priority, and due date."
)
def create_task(task: TaskCreate):
    """
    Create a new task.
    
    - **title**: Task title (required, 1-200 characters)
    - **description**: Task description (optional, max 1000 characters)
    - **status**: pending, in_progress, or done (default: pending)
    - **priority**: low, medium, or high (default: medium)
    - **due_date**: Due date in ISO format (optional)
    """
    task_data = task.model_dump()
    new_task = db.create_task(task_data)
    return new_task


# ============ READ ============

@router.get(
    "/",
    response_model=TaskListResponse,
    summary="List all tasks",
    description="Get all tasks with optional filters."
)
def list_tasks(
    status: Optional[TaskStatus] = Query(None, description="Filter by status"),
    priority: Optional[TaskPriority] = Query(None, description="Filter by priority"),
    search: Optional[str] = Query(None, description="Search in title"),
):
    """
    List all tasks with optional filters.
    
    - **status**: Filter by task status
    - **priority**: Filter by task priority
    - **search**: Search term for task title
    """
    tasks = db.filter_tasks(
        status=status.value if status else None,
        priority=priority.value if priority else None,
        search=search
    )
    
    return {
        "total": len(tasks),
        "tasks": tasks
    }


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Get task by ID",
    description="Get a specific task by its ID."
)
def get_task(
    task_id: int = Path(..., gt=0, description="Task ID")
):
    """
    Get a specific task by ID.
    
    - **task_id**: Task ID (must be > 0)
    
    Returns 404 if task not found.
    """
    task = db.get_task(task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    return task


# ============ UPDATE ============

@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Update task",
    description="Update an existing task. Only provided fields will be updated."
)
def update_task(
    task_id: int = Path(..., gt=0, description="Task ID"),
    task_update: TaskUpdate = ...
):
    """
    Update a task.
    
    - **task_id**: Task ID to update
    - Only provided fields will be updated
    
    Returns 404 if task not found.
    """
    # Check if task exists
    existing_task = db.get_task(task_id)
    if not existing_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    # Update task
    update_data = task_update.model_dump(exclude_unset=True)
    
    # Convert enum to value if present
    if "status" in update_data and update_data["status"]:
        update_data["status"] = update_data["status"].value
    if "priority" in update_data and update_data["priority"]:
        update_data["priority"] = update_data["priority"].value
    
    updated_task = db.update_task(task_id, update_data)
    
    return updated_task


# ============ DELETE ============

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete task",
    description="Delete a task by ID."
)
def delete_task(
    task_id: int = Path(..., gt=0, description="Task ID")
):
    """
    Delete a task.
    
    - **task_id**: Task ID to delete
    
    Returns 404 if task not found.
    """
    # Check if task exists
    existing_task = db.get_task(task_id)
    if not existing_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    db.delete_task(task_id)
    return None


# ============ ADDITIONAL ENDPOINTS ============

@router.patch(
    "/{task_id}/status",
    response_model=TaskResponse,
    summary="Update task status",
    description="Update only the status of a task."
)
def update_task_status(
    task_id: int = Path(..., gt=0, description="Task ID"),
    new_status: TaskStatus = Query(..., description="New status")
):
    """
    Update task status only.
    
    Quick way to change task status without updating other fields.
    """
    existing_task = db.get_task(task_id)
    if not existing_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    updated_task = db.update_task(task_id, {"status": new_status.value})
    return updated_task


@router.get(
    "/stats/summary",
    summary="Get task statistics",
    description="Get summary statistics of all tasks."
)
def get_task_stats():
    """
    Get task statistics.
    
    Returns count by status and priority.
    """
    tasks = db.get_all_tasks()
    
    status_counts = {"pending": 0, "in_progress": 0, "done": 0}
    priority_counts = {"low": 0, "medium": 0, "high": 0}
    
    for task in tasks:
        status_counts[task["status"]] = status_counts.get(task["status"], 0) + 1
        priority_counts[task["priority"]] = priority_counts.get(task["priority"], 0) + 1
    
    return {
        "total": len(tasks),
        "by_status": status_counts,
        "by_priority": priority_counts
    }
```

### 3.2 Update app/routes/__init__.py

```python
# app/routes/__init__.py
from .tasks import router as tasks_router
```

---

## 💻 Part 4: Update Main Application (20 min)

### 4.1 Update app/main.py

```python
# app/main.py
"""TaskFlow - Task Management System."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import tasks_router

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="""
    ## TaskFlow - Task Management System
    
    REST API for managing tasks with the following features:
    * **Create** new tasks
    * **Read** task information
    * **Update** task details
    * **Delete** tasks
    * **Filter** and search tasks
    * **Statistics** and reporting
    
    ### CSI403 Full Stack Development
    มหาวิทยาลัยศรีปทุม วิทยาเขตชลบุรี
    """,
    version=settings.APP_VERSION,
    contact={
        "name": "CSI403 Student",
        "email": "student@spuchonburi.ac.th"
    }
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks_router)


@app.get("/", tags=["Health"])
def root():
    """Root endpoint - Welcome message."""
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "running"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint."""
    from app import database as db
    
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "total_tasks": len(db.tasks_db)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
```

---

## 💻 Part 5: Testing Your API (30 min)

### 5.1 Run Server

```bash
uvicorn app.main:app --reload
```

### 5.2 Test with Swagger UI

เปิด Browser: http://localhost:8000/docs

### 5.3 Test Scenarios

**1. Create Tasks:**

```json
// POST /api/tasks
{
    "title": "Complete Lab 2",
    "description": "Finish FastAPI CRUD lab",
    "priority": "high"
}

{
    "title": "Review Python",
    "description": "Review Python basics",
    "status": "in_progress",
    "priority": "medium"
}

{
    "title": "Setup Database",
    "description": "Prepare MSSQL for Lab 3",
    "priority": "low"
}
```

**2. List Tasks:**

```
GET /api/tasks
GET /api/tasks?status=pending
GET /api/tasks?priority=high
GET /api/tasks?search=Lab
```

**3. Get Task by ID:**

```
GET /api/tasks/1
GET /api/tasks/999  (should return 404)
```

**4. Update Task:**

```json
// PUT /api/tasks/1
{
    "status": "in_progress"
}
```

**5. Update Status Only:**

```
PATCH /api/tasks/1/status?new_status=done
```

**6. Get Statistics:**

```
GET /api/tasks/stats/summary
```

**7. Delete Task:**

```
DELETE /api/tasks/3
```

### 5.4 Test with curl

```bash
# Create task
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Task", "priority": "high"}'

# List tasks
curl "http://localhost:8000/api/tasks"

# Get task
curl "http://localhost:8000/api/tasks/1"

# Update task
curl -X PUT "http://localhost:8000/api/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'

# Delete task
curl -X DELETE "http://localhost:8000/api/tasks/1"

# Statistics
curl "http://localhost:8000/api/tasks/stats/summary"
```

---

## 📤 Submission

### Checklist

- [ ] Pydantic schemas ครบ (TaskCreate, TaskUpdate, TaskResponse)
- [ ] CRUD endpoints ครบ (POST, GET, PUT, DELETE)
- [ ] Filter และ Search ทำงานได้
- [ ] Statistics endpoint ทำงานได้
- [ ] Error handling (404) ทำงานได้
- [ ] Swagger documentation ครบถ้วน
- [ ] Code สะอาด มี comments

### Git Commands

```bash
git checkout develop
git checkout -b feature/lab02-fastapi-crud
git add .
git commit -m "Lab 2: FastAPI CRUD - Task API complete"
git push -u origin feature/lab02-fastapi-crud
# Create PR and merge
```

### Screenshots ที่ต้องส่ง

1. Swagger UI หน้า /docs
2. ทดสอบ Create Task
3. ทดสอบ List Tasks with filter
4. ทดสอบ Statistics

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| Pydantic Schemas ครบถ้วน | 1.5% |
| CRUD Endpoints ทำงานได้ | 3% |
| Filter + Search + Stats | 1.5% |
| Error Handling (404) | 1% |
| Code Quality + Swagger Docs | 1% |
| **รวม** | **8%** |

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 3
