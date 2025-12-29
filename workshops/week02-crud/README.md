# Workshop 2: 📝 CRUD Operations

## 📋 Overview

| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | สร้าง Task API ครบ 5 operations |

---

## 💻 Checkpoint 1: Pydantic Schemas (2%)

### Create app/schemas/task.py

```python
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: datetime | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
```

---

## 💻 Checkpoint 2: Create Task - POST (2%)

### Create app/routes/tasks.py

```python
from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

tasks_db: dict[int, dict] = {}
task_counter: int = 0

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global task_counter
    task_counter += 1
    new_task = {
        "id": task_counter,
        **task.model_dump(),
        "created_at": datetime.now(),
        "updated_at": None
    }
    tasks_db[task_counter] = new_task
    return new_task
```

### Update app/main.py

```python
from app.routes import tasks
app.include_router(tasks.router)
```

---

## 💻 Checkpoint 3: Read Tasks - GET (2%)

```python
@router.get("/", response_model=list[TaskResponse])
def list_tasks(status: str | None = None, priority: str | None = None):
    tasks = list(tasks_db.values())
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if priority:
        tasks = [t for t in tasks if t["priority"] == priority]
    return tasks

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]
```

---

## 💻 Checkpoint 4: Update &amp; Delete (2%)

```python
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks_db[task_id]
    for key, value in task_update.model_dump(exclude_unset=True).items():
        task[key] = value
    task["updated_at"] = datetime.now()
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
```

### Commit

```bash
git add .
git commit -m "Add CRUD endpoints for tasks"
git push
```

---

## 🎉 Complete!

**Next:** Database Integration

[📖 Extended: REST Best Practices →](../../docs/extended/week02-rest-best-practices.md)
