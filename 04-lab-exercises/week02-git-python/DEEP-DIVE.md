# Week 2: Deep Dive - Git & Python

> 📚 **เนื้อหาเพิ่มเติมสำหรับผู้ที่ต้องการศึกษาเชิงลึก**
> 
> ไม่จำเป็นต้องอ่านในคาบ แต่จะช่วยให้เข้าใจมากขึ้น

---

## 🔀 Git Deep Dive

### Git Internal Concepts

#### How Git Stores Data

Git ไม่ได้เก็บ "differences" แต่เก็บ "snapshots" ของไฟล์ทั้งหมด:

```
Commit 1: [Snapshot A] --> Commit 2: [Snapshot B] --> Commit 3: [Snapshot C]
```

#### Git Object Types

1. **Blob** - เก็บเนื้อหาไฟล์
2. **Tree** - เก็บโครงสร้างโฟลเดอร์
3. **Commit** - เก็บ metadata (author, message, parent)
4. **Tag** - เก็บ reference ถึง commit

### Advanced Git Commands

#### Branching Strategies

```bash
# Create feature branch
git checkout -b feature/task-api

# Work on feature
git add .
git commit -m "Add task API"

# Switch back to main
git checkout main

# Merge feature
git merge feature/task-api

# Delete feature branch
git branch -d feature/task-api
```

#### Git Stash

```bash
# Save work temporarily
git stash

# List stashes
git stash list

# Apply latest stash
git stash pop

# Apply specific stash
git stash apply stash@{0}
```

#### Interactive Rebase

```bash
# Rebase last 3 commits
git rebase -i HEAD~3

# Commands in editor:
# pick = keep commit
# squash = merge with previous
# reword = change message
# drop = remove commit
```

#### Git Reset vs Revert

```bash
# Reset (rewrite history) - ใช้กับ local only
git reset --soft HEAD~1   # Keep changes staged
git reset --mixed HEAD~1  # Keep changes unstaged
git reset --hard HEAD~1   # Discard changes

# Revert (safe for shared branches)
git revert abc1234
```

### .gitignore Best Practices

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment
.env
.env.local
*.local

# Testing
.coverage
htmlcov/
.pytest_cache/

# Build
dist/
build/
*.egg-info/

# OS
.DS_Store
Thumbs.db
```

### Git Hooks

```bash
# Pre-commit hook example (.git/hooks/pre-commit)
#!/bin/sh

# Run tests before commit
python -m pytest tests/ -q

# Run linter
python -m flake8 app/

# If any command fails, abort commit
```

---

## 🐍 Python Deep Dive

### Type Hints Advanced

#### Generic Types

```python
from typing import TypeVar, Generic, List, Dict, Optional

T = TypeVar('T')

class Repository(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def add(self, item: T) -> None:
        self.items.append(item)
    
    def get(self, index: int) -> Optional[T]:
        if 0 <= index < len(self.items):
            return self.items[index]
        return None
```

#### Union Types (Python 3.10+)

```python
# Old way
from typing import Union
def process(value: Union[str, int]) -> str:
    return str(value)

# New way (Python 3.10+)
def process(value: str | int) -> str:
    return str(value)

# Optional
def get_user(id: int) -> User | None:
    pass
```

#### TypedDict

```python
from typing import TypedDict

class TaskDict(TypedDict):
    id: int
    title: str
    status: str
    priority: str

def create_task(data: TaskDict) -> Task:
    pass
```

### Dataclasses Advanced

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Task:
    id: int
    title: str
    status: str = "pending"
    priority: str = "medium"
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        # Validation
        if len(self.title) < 1:
            raise ValueError("Title cannot be empty")
    
    def mark_done(self) -> None:
        self.status = "done"
        self.updated_at = datetime.now()

# Frozen (immutable)
@dataclass(frozen=True)
class ImmutableTask:
    id: int
    title: str
```

### Context Managers

```python
from contextlib import contextmanager

@contextmanager
def database_connection():
    conn = connect_to_database()
    try:
        yield conn
    finally:
        conn.close()

# Usage
with database_connection() as conn:
    conn.execute("SELECT * FROM tasks")

# Class-based
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_database()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False  # Don't suppress exceptions
```

### Decorators

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

def retry(max_attempts: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
        return wrapper
    return decorator

@timer
@retry(max_attempts=3)
def fetch_data():
    pass
```

### Async/Await

```python
import asyncio
import httpx

async def fetch_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def fetch_multiple(urls: list[str]) -> list[str]:
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

# Run async function
results = asyncio.run(fetch_multiple([
    "https://api.example.com/1",
    "https://api.example.com/2",
]))
```

---

## 🚀 FastAPI Deep Dive

### Dependency Injection

```python
from fastapi import Depends, FastAPI
from typing import Generator

app = FastAPI()

# Simple dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Class-based dependency
class CommonQueryParams:
    def __init__(
        self,
        skip: int = 0,
        limit: int = 100,
        search: str | None = None
    ):
        self.skip = skip
        self.limit = limit
        self.search = search

@app.get("/tasks")
def list_tasks(
    db: Session = Depends(get_db),
    params: CommonQueryParams = Depends()
):
    query = db.query(Task)
    if params.search:
        query = query.filter(Task.title.contains(params.search))
    return query.offset(params.skip).limit(params.limit).all()
```

### Background Tasks

```python
from fastapi import BackgroundTasks

def send_notification(email: str, message: str):
    # Simulate slow operation
    time.sleep(5)
    print(f"Sent to {email}: {message}")

@app.post("/tasks")
def create_task(
    task: TaskCreate,
    background_tasks: BackgroundTasks
):
    # Create task immediately
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    
    # Send notification in background
    background_tasks.add_task(
        send_notification,
        email="user@example.com",
        message=f"Task '{task.title}' created"
    )
    
    return new_task
```

### Middleware

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        response.headers["X-Process-Time"] = str(duration)
        return response

app.add_middleware(TimingMiddleware)
```

### Exception Handlers

```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class TaskNotFoundError(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id

@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Task not found",
            "task_id": exc.task_id,
            "message": f"Task with id {exc.task_id} does not exist"
        }
    )

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise TaskNotFoundError(task_id)
    return task
```

---

## 📚 Further Reading

### Git
- [Pro Git Book](https://git-scm.com/book/en/v2) (Free)
- [Git Flight Rules](https://github.com/k88hudson/git-flight-rules)
- [Learn Git Branching](https://learngitbranching.js.org/) (Interactive)

### Python
- [Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Real Python - Type Checking](https://realpython.com/python-type-checking/)
- [Python Asyncio](https://docs.python.org/3/library/asyncio.html)

### FastAPI
- [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [Awesome FastAPI](https://github.com/mjhea0/awesome-fastapi)

---

**Happy Learning! 🎓**
