# Workshop 3: 🗄️ Database Integration

## 📋 Overview
| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | เชื่อมต่อ MSSQL + SQLAlchemy |

---

## 💻 CP1: Run MSSQL Container (2%)

```bash
docker run -d \
  --name taskflow-db \
  -e "ACCEPT_EULA=Y" \
  -e "SA_PASSWORD=TaskFlow@123" \
  -p 1433:1433 \
  mcr.microsoft.com/mssql/server:2022-latest

# Wait 30 seconds, then create database
docker exec -it taskflow-db /opt/mssql-tools18/bin/sqlcmd \
  -S localhost -U sa -P "TaskFlow@123" -C \
  -Q "CREATE DATABASE taskflow"
```

---

## 💻 CP2: SQLAlchemy Setup (2%)

```bash
pip install sqlalchemy pyodbc
```

### app/database.py
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 💻 CP3: Create Models (2%)

### app/models/task.py
```python
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(String(20), default="pending")
    priority = Column(String(20), default="medium")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
```

---

## 💻 CP4: CRUD with Database (2%)

Update routes to use `db: Session = Depends(get_db)`

```bash
git add .
git commit -m "Add database integration"
git push
```

---

[📖 Extended →](../../docs/extended/week03-database-design.md)
