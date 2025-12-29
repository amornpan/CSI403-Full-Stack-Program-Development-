# Extended: Database Design

## Normalization
- 1NF: No repeating groups
- 2NF: No partial dependencies
- 3NF: No transitive dependencies

## Relationships
```python
# One-to-Many
class User(Base):
    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    user_id = Column(ForeignKey("users.id"))
    owner = relationship("User", back_populates="tasks")
```

## Indexes
```python
title = Column(String(200), index=True)
```

## Migrations
```bash
pip install alembic
alembic init migrations
alembic revision --autogenerate -m "Add table"
alembic upgrade head
```
