# Lab 05: FastAPI CRUD Operations

**Week 5 | February 4-6, 2026 | 2%**

## 🎯 Objectives
- Create RESTful API endpoints
- Handle path and query parameters
- Use Pydantic for data validation
- Implement CRUD operations
- Test with Swagger UI

## 🔧 Setup

```bash
mkdir lab05-fastapi
cd lab05-fastapi
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pydantic
```

## 💻 Part 1: Basic Routes (20 min)

### Exercise 1.1: Hello FastAPI
Create `main.py`:
```python
from fastapi import FastAPI

app = FastAPI(
    title="Loan Management API",
    description="CSI403 Lab 05 - FastAPI CRUD",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Loan API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

Run: `uvicorn main:app --reload`
Test: Visit `http://127.0.0.1:8000/docs`

### Exercise 1.2: Path Parameters
```python
@app.get("/loans/{loan_id}")
def get_loan(loan_id: int):
    return {"loan_id": loan_id, "message": f"Getting loan #{loan_id}"}

@app.get("/users/{user_id}/loans/{loan_id}")
def get_user_loan(user_id: int, loan_id: int):
    return {
        "user_id": user_id,
        "loan_id": loan_id,
        "message": f"Loan #{loan_id} for user #{user_id}"
    }
```

### Exercise 1.3: Query Parameters
```python
from typing import Optional

@app.get("/loans")
def list_loans(
    status: Optional[str] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    skip: int = 0,
    limit: int = 10
):
    return {
        "filters": {
            "status": status,
            "min_amount": min_amount,
            "max_amount": max_amount
        },
        "pagination": {
            "skip": skip,
            "limit": limit
        }
    }
```

## 💻 Part 2: Pydantic Models (25 min)

### Exercise 2.1: Create Schemas
Create `schemas.py`:
```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

class LoanStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    CURRENT = "current"
    PAID = "paid"
    LATE = "late"
    DEFAULT = "default"

class LoanBase(BaseModel):
    amount: float = Field(..., gt=0, le=1000000, description="Loan amount in THB")
    term: int = Field(..., ge=12, le=60, description="Term in months")
    purpose: Optional[str] = Field(None, max_length=200)

class LoanCreate(LoanBase):
    borrower_name: str = Field(..., min_length=2, max_length=100)
    borrower_email: EmailStr
    
    class Config:
        json_schema_extra = {
            "example": {
                "amount": 100000,
                "term": 36,
                "purpose": "Home improvement",
                "borrower_name": "John Doe",
                "borrower_email": "john@example.com"
            }
        }

class LoanUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0, le=1000000)
    term: Optional[int] = Field(None, ge=12, le=60)
    purpose: Optional[str] = Field(None, max_length=200)
    status: Optional[LoanStatus] = None

class LoanResponse(LoanBase):
    id: int
    borrower_name: str
    borrower_email: str
    status: LoanStatus = LoanStatus.PENDING
    interest_rate: float = 7.5
    monthly_payment: float
    created_at: datetime
    
    class Config:
        from_attributes = True
```

### Exercise 2.2: Use Schemas in Routes
Update `main.py`:
```python
from fastapi import FastAPI, HTTPException, status
from schemas import LoanCreate, LoanUpdate, LoanResponse, LoanStatus
from datetime import datetime
from typing import List

app = FastAPI(title="Loan Management API")

# In-memory database
loans_db = []
loan_id_counter = 0

def calculate_monthly_payment(amount: float, rate: float, term: int) -> float:
    """Calculate monthly payment using simple interest"""
    total_interest = amount * (rate / 100) * (term / 12)
    return round((amount + total_interest) / term, 2)

@app.post("/loans", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def create_loan(loan: LoanCreate):
    global loan_id_counter
    loan_id_counter += 1
    
    monthly_payment = calculate_monthly_payment(loan.amount, 7.5, loan.term)
    
    new_loan = {
        "id": loan_id_counter,
        "amount": loan.amount,
        "term": loan.term,
        "purpose": loan.purpose,
        "borrower_name": loan.borrower_name,
        "borrower_email": loan.borrower_email,
        "status": LoanStatus.PENDING,
        "interest_rate": 7.5,
        "monthly_payment": monthly_payment,
        "created_at": datetime.now()
    }
    
    loans_db.append(new_loan)
    return new_loan

@app.get("/loans", response_model=List[LoanResponse])
def list_loans(
    status: LoanStatus = None,
    skip: int = 0,
    limit: int = 10
):
    result = loans_db
    
    if status:
        result = [l for l in result if l["status"] == status]
    
    return result[skip:skip + limit]

@app.get("/loans/{loan_id}", response_model=LoanResponse)
def get_loan(loan_id: int):
    loan = next((l for l in loans_db if l["id"] == loan_id), None)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Loan #{loan_id} not found"
        )
    return loan

@app.put("/loans/{loan_id}", response_model=LoanResponse)
def update_loan(loan_id: int, loan_update: LoanUpdate):
    loan_index = next((i for i, l in enumerate(loans_db) if l["id"] == loan_id), None)
    
    if loan_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Loan #{loan_id} not found"
        )
    
    loan = loans_db[loan_index]
    update_data = loan_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        loan[key] = value
    
    # Recalculate monthly payment if amount or term changed
    if "amount" in update_data or "term" in update_data:
        loan["monthly_payment"] = calculate_monthly_payment(
            loan["amount"], loan["interest_rate"], loan["term"]
        )
    
    return loan

@app.delete("/loans/{loan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loan(loan_id: int):
    loan_index = next((i for i, l in enumerate(loans_db) if l["id"] == loan_id), None)
    
    if loan_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Loan #{loan_id} not found"
        )
    
    loans_db.pop(loan_index)
    return None
```

## 💻 Part 3: Advanced Features (25 min)

### Exercise 3.1: Request Validation
```python
from fastapi import Query, Path

@app.get("/search")
def search_loans(
    q: str = Query(..., min_length=2, description="Search query"),
    min_amount: float = Query(0, ge=0, description="Minimum loan amount"),
    max_amount: float = Query(1000000, le=10000000, description="Maximum loan amount"),
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=100, description="Items per page")
):
    # Filter loans
    results = [
        l for l in loans_db
        if q.lower() in l["borrower_name"].lower()
        and min_amount <= l["amount"] <= max_amount
    ]
    
    # Paginate
    start = (page - 1) * per_page
    end = start + per_page
    
    return {
        "query": q,
        "total": len(results),
        "page": page,
        "per_page": per_page,
        "data": results[start:end]
    }

@app.patch("/loans/{loan_id}/status")
def update_loan_status(
    loan_id: int = Path(..., gt=0, description="Loan ID"),
    new_status: LoanStatus = Query(..., description="New status")
):
    loan = next((l for l in loans_db if l["id"] == loan_id), None)
    
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    old_status = loan["status"]
    loan["status"] = new_status
    
    return {
        "loan_id": loan_id,
        "old_status": old_status,
        "new_status": new_status,
        "message": f"Status updated from {old_status} to {new_status}"
    }
```

### Exercise 3.2: Response Models & Tags
```python
from fastapi import FastAPI, HTTPException, status
from typing import List

app = FastAPI(
    title="Loan Management API",
    description="""
    ## Loan Management System API
    
    This API allows you to:
    * **Create** new loan applications
    * **Read** loan information
    * **Update** loan details
    * **Delete** loans
    """,
    version="1.0.0",
    contact={
        "name": "CSI403 Support",
        "email": "support@example.com"
    }
)

# Tags for grouping endpoints
tags_metadata = [
    {"name": "loans", "description": "Loan management operations"},
    {"name": "statistics", "description": "Loan statistics and reports"},
]

@app.get("/loans", response_model=List[LoanResponse], tags=["loans"])
def list_loans():
    """
    Retrieve all loans.
    
    - **status**: Filter by loan status
    - **skip**: Number of records to skip
    - **limit**: Maximum records to return
    """
    return loans_db

@app.get("/stats", tags=["statistics"])
def get_statistics():
    """Get loan portfolio statistics."""
    if not loans_db:
        return {"message": "No loans in database"}
    
    total_amount = sum(l["amount"] for l in loans_db)
    avg_amount = total_amount / len(loans_db)
    
    status_counts = {}
    for loan in loans_db:
        status = loan["status"].value
        status_counts[status] = status_counts.get(status, 0) + 1
    
    return {
        "total_loans": len(loans_db),
        "total_amount": total_amount,
        "average_amount": round(avg_amount, 2),
        "status_breakdown": status_counts
    }
```

## 💻 Part 4: Error Handling (20 min)

### Exercise 4.1: Custom Exceptions
```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

class LoanNotFoundException(Exception):
    def __init__(self, loan_id: int):
        self.loan_id = loan_id

class InsufficientAmountException(Exception):
    def __init__(self, amount: float, minimum: float):
        self.amount = amount
        self.minimum = minimum

@app.exception_handler(LoanNotFoundException)
async def loan_not_found_handler(request: Request, exc: LoanNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "LoanNotFound",
            "message": f"Loan #{exc.loan_id} does not exist",
            "loan_id": exc.loan_id
        }
    )

@app.exception_handler(InsufficientAmountException)
async def insufficient_amount_handler(request: Request, exc: InsufficientAmountException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "InsufficientAmount",
            "message": f"Amount {exc.amount} is below minimum {exc.minimum}",
            "amount": exc.amount,
            "minimum": exc.minimum
        }
    )

# Use in routes
@app.get("/loans/{loan_id}")
def get_loan(loan_id: int):
    loan = next((l for l in loans_db if l["id"] == loan_id), None)
    if not loan:
        raise LoanNotFoundException(loan_id)
    return loan
```

## 📝 Assignment

Create a complete CRUD API for a Payment resource:

### Requirements:
1. Create `PaymentCreate`, `PaymentUpdate`, `PaymentResponse` schemas
2. Implement these endpoints:
   - `POST /loans/{loan_id}/payments` - Create payment
   - `GET /loans/{loan_id}/payments` - List payments for a loan
   - `GET /payments/{payment_id}` - Get payment details
   - `DELETE /payments/{payment_id}` - Delete payment
3. Add proper validation and error handling
4. Document with docstrings

### Submission:
```bash
git add .
git commit -m "Lab 05: FastAPI CRUD operations"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Basic routes | 0.5% |
| Pydantic schemas | 0.5% |
| CRUD operations | 0.5% |
| Assignment | 0.5% |

---
**Deadline:** Before Week 6 class
