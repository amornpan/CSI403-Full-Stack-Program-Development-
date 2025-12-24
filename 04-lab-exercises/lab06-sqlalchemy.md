# Lab 06: SQLAlchemy ORM & Database

**Week 6 | February 11-13, 2026 | 2%**

## 🎯 Objectives
- Connect to database with SQLAlchemy
- Create ORM models
- Define relationships (One-to-Many, One-to-One)
- Perform CRUD with ORM

## 🔧 Setup

```bash
mkdir lab06-sqlalchemy
cd lab06-sqlalchemy
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy aiosqlite
mkdir app
```

## 💻 Part 1: Database Connection (20 min)

### Exercise 1.1: Create Database Config
Create `app/database.py`:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite for development
SQLALCHEMY_DATABASE_URL = "sqlite:///./loan_system.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite only
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## 💻 Part 2: Create Models (30 min)

### Exercise 2.1: User & Borrower Models
Create `app/models.py`:
```python
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="borrower")  # admin, borrower
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship: One User has One Borrower profile
    borrower = relationship("Borrower", back_populates="user", uselist=False)
    
    def __repr__(self):
        return f"<User {self.username}>"


class Borrower(Base):
    __tablename__ = "borrowers"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    annual_income = Column(Float)
    employment = Column(String(100))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="borrower")
    loans = relationship("Loan", back_populates="borrower")
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"<Borrower {self.full_name}>"


class Loan(Base):
    __tablename__ = "loans"
    
    id = Column(Integer, primary_key=True, index=True)
    borrower_id = Column(Integer, ForeignKey("borrowers.id"), nullable=False)
    
    loan_amount = Column(Float, nullable=False)
    interest_rate = Column(Float, default=7.5)
    term_months = Column(Integer, nullable=False)
    monthly_payment = Column(Float)
    purpose = Column(String(50))
    status = Column(String(20), default="pending")
    
    application_date = Column(DateTime(timezone=True), server_default=func.now())
    approval_date = Column(DateTime(timezone=True))
    
    # Relationships
    borrower = relationship("Borrower", back_populates="loans")
    payments = relationship("Payment", back_populates="loan")
    
    def __repr__(self):
        return f"<Loan #{self.id} - {self.loan_amount:,.0f} THB>"


class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    principal = Column(Float)
    interest = Column(Float)
    remaining_balance = Column(Float)
    
    # Relationship
    loan = relationship("Loan", back_populates="payments")
    
    def __repr__(self):
        return f"<Payment #{self.id} - {self.amount:,.0f} THB>"
```

### Exercise 2.2: Initialize Database
Create `app/init_db.py`:
```python
from database import engine, Base
from models import User, Borrower, Loan, Payment

def init_database():
    """Create all tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created!")

def drop_database():
    """Drop all tables"""
    Base.metadata.drop_all(bind=engine)
    print("⚠️ All tables dropped!")

if __name__ == "__main__":
    init_database()
```

Run: `python app/init_db.py`

## 💻 Part 3: CRUD Operations (30 min)

### Exercise 3.1: Create CRUD Functions
Create `app/crud.py`:
```python
from sqlalchemy.orm import Session
from models import User, Borrower, Loan, Payment
from typing import List, Optional

# ============ USER CRUD ============

def create_user(db: Session, username: str, email: str, password_hash: str, role: str = "borrower"):
    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()

# ============ BORROWER CRUD ============

def create_borrower(db: Session, user_id: int, first_name: str, last_name: str, **kwargs):
    borrower = Borrower(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        **kwargs
    )
    db.add(borrower)
    db.commit()
    db.refresh(borrower)
    return borrower

def get_borrower(db: Session, borrower_id: int) -> Optional[Borrower]:
    return db.query(Borrower).filter(Borrower.id == borrower_id).first()

def get_borrower_by_user(db: Session, user_id: int) -> Optional[Borrower]:
    return db.query(Borrower).filter(Borrower.user_id == user_id).first()

# ============ LOAN CRUD ============

def create_loan(db: Session, borrower_id: int, loan_amount: float, term_months: int, **kwargs):
    # Calculate monthly payment
    rate = kwargs.get("interest_rate", 7.5)
    total_interest = loan_amount * (rate / 100) * (term_months / 12)
    monthly_payment = (loan_amount + total_interest) / term_months
    
    loan = Loan(
        borrower_id=borrower_id,
        loan_amount=loan_amount,
        term_months=term_months,
        monthly_payment=round(monthly_payment, 2),
        **kwargs
    )
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

def get_loan(db: Session, loan_id: int) -> Optional[Loan]:
    return db.query(Loan).filter(Loan.id == loan_id).first()

def get_loans(db: Session, skip: int = 0, limit: int = 100) -> List[Loan]:
    return db.query(Loan).offset(skip).limit(limit).all()

def get_loans_by_borrower(db: Session, borrower_id: int) -> List[Loan]:
    return db.query(Loan).filter(Loan.borrower_id == borrower_id).all()

def get_loans_by_status(db: Session, status: str) -> List[Loan]:
    return db.query(Loan).filter(Loan.status == status).all()

def update_loan_status(db: Session, loan_id: int, new_status: str):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if loan:
        loan.status = new_status
        db.commit()
        db.refresh(loan)
    return loan

def delete_loan(db: Session, loan_id: int) -> bool:
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if loan:
        db.delete(loan)
        db.commit()
        return True
    return False

# ============ PAYMENT CRUD ============

def create_payment(db: Session, loan_id: int, amount: float, **kwargs):
    payment = Payment(
        loan_id=loan_id,
        amount=amount,
        **kwargs
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

def get_payments_by_loan(db: Session, loan_id: int) -> List[Payment]:
    return db.query(Payment).filter(Payment.loan_id == loan_id).all()
```

### Exercise 3.2: Test CRUD Operations
Create `app/test_crud.py`:
```python
from database import SessionLocal, engine, Base
from models import User, Borrower, Loan
import crud

# Create tables
Base.metadata.create_all(bind=engine)

# Create session
db = SessionLocal()

try:
    print("=" * 50)
    print("Testing CRUD Operations")
    print("=" * 50)
    
    # 1. Create User
    print("\n1. Creating user...")
    user = crud.create_user(
        db, 
        username="john_doe",
        email="john@example.com",
        password_hash="hashed_password_123"
    )
    print(f"   Created: {user}")
    
    # 2. Create Borrower
    print("\n2. Creating borrower profile...")
    borrower = crud.create_borrower(
        db,
        user_id=user.id,
        first_name="John",
        last_name="Doe",
        phone="081-234-5678",
        annual_income=600000,
        employment="Software Engineer"
    )
    print(f"   Created: {borrower}")
    
    # 3. Create Loans
    print("\n3. Creating loans...")
    loan1 = crud.create_loan(
        db,
        borrower_id=borrower.id,
        loan_amount=100000,
        term_months=36,
        purpose="Home Improvement"
    )
    print(f"   Created: {loan1}")
    print(f"   Monthly Payment: {loan1.monthly_payment:,.2f} THB")
    
    loan2 = crud.create_loan(
        db,
        borrower_id=borrower.id,
        loan_amount=50000,
        term_months=24,
        purpose="Education"
    )
    print(f"   Created: {loan2}")
    
    # 4. Query loans
    print("\n4. Querying borrower's loans...")
    loans = crud.get_loans_by_borrower(db, borrower.id)
    for loan in loans:
        print(f"   - Loan #{loan.id}: {loan.loan_amount:,.0f} THB ({loan.status})")
    
    # 5. Update loan status
    print("\n5. Updating loan status...")
    updated = crud.update_loan_status(db, loan1.id, "approved")
    print(f"   Loan #{updated.id} status: {updated.status}")
    
    # 6. Create payment
    print("\n6. Creating payment...")
    payment = crud.create_payment(
        db,
        loan_id=loan1.id,
        amount=loan1.monthly_payment,
        principal=2500,
        interest=625
    )
    print(f"   Payment: {payment.amount:,.2f} THB")
    
    # 7. Test relationships
    print("\n7. Testing relationships...")
    print(f"   User -> Borrower: {user.borrower.full_name}")
    print(f"   Borrower -> User: {borrower.user.username}")
    print(f"   Borrower -> Loans: {len(borrower.loans)} loans")
    print(f"   Loan -> Borrower: {loan1.borrower.full_name}")
    print(f"   Loan -> Payments: {len(loan1.payments)} payments")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!")
    print("=" * 50)

finally:
    db.close()
```

## 💻 Part 4: FastAPI Integration (20 min)

### Exercise 4.1: API with Database
Create `app/main.py`:
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
import crud
import models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loan API with SQLAlchemy")

@app.get("/")
def root():
    return {"message": "Loan API with Database"}

# ===== USERS =====

@app.post("/users")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    # Check existing
    if crud.get_user_by_username(db, username):
        raise HTTPException(status_code=400, detail="Username already exists")
    if crud.get_user_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    return crud.create_user(db, username, email, password)

@app.get("/users")
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ===== LOANS =====

@app.post("/borrowers/{borrower_id}/loans")
def create_loan(
    borrower_id: int,
    amount: float,
    term: int,
    purpose: str = None,
    db: Session = Depends(get_db)
):
    borrower = crud.get_borrower(db, borrower_id)
    if not borrower:
        raise HTTPException(status_code=404, detail="Borrower not found")
    
    return crud.create_loan(db, borrower_id, amount, term, purpose=purpose)

@app.get("/loans")
def list_loans(status: str = None, db: Session = Depends(get_db)):
    if status:
        return crud.get_loans_by_status(db, status)
    return crud.get_loans(db)

@app.get("/loans/{loan_id}")
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = crud.get_loan(db, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return {
        "id": loan.id,
        "amount": loan.loan_amount,
        "term": loan.term_months,
        "monthly_payment": loan.monthly_payment,
        "status": loan.status,
        "borrower": loan.borrower.full_name
    }

@app.patch("/loans/{loan_id}/status")
def update_status(loan_id: int, status: str, db: Session = Depends(get_db)):
    loan = crud.update_loan_status(db, loan_id, status)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return {"message": f"Status updated to {status}", "loan_id": loan_id}

@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    if not crud.delete_loan(db, loan_id):
        raise HTTPException(status_code=404, detail="Loan not found")
    return {"message": "Loan deleted", "loan_id": loan_id}
```

## 📝 Assignment

Extend the models and CRUD to include:
1. `LoanStatusHistory` table to track status changes
2. Function to get loan with full payment history
3. Function to calculate remaining balance
4. API endpoint to get borrower dashboard (loans summary)

## 📤 Submission
```bash
git add .
git commit -m "Lab 06: SQLAlchemy ORM"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Database setup | 0.5% |
| Models & relationships | 0.5% |
| CRUD operations | 0.5% |
| Assignment | 0.5% |

---
**Deadline:** Before Week 7 class
