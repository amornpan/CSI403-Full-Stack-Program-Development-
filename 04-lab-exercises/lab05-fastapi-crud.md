# Lab 05: FastAPI CRUD - Assessment Lab 1

**Week 5 | Assessment Lab | 5%**

## 🎯 Objectives
- สร้าง RESTful API ด้วย FastAPI
- ใช้ Pydantic สำหรับ Data Validation
- ทำ CRUD Operations
- สร้าง API Documentation ด้วย Swagger

## ⚠️ Important: This is an Assessment Lab

งานนี้เก็บคะแนน **5%** ของคะแนนรวม

### Submission Requirements:
- **Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ของสัปดาห์ที่ 5
- **Submit via:** GitHub Repository ของกลุ่ม
- **Folder:** `lab1-api-design/`

### Grading Rubric:
| Criteria | Points |
|----------|:------:|
| CRUD Endpoints ครบ 4 operations | 1.5% |
| Pydantic Schemas ถูกต้อง | 1% |
| Validation & Error Handling | 1% |
| Swagger Documentation | 0.5% |
| Code Quality & README | 1% |
| **Total** | **5%** |

---

## 🔧 Setup

```bash
mkdir lab1-api-design
cd lab1-api-design
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn pydantic
```

## 📋 Assignment: Loan API

สร้าง REST API สำหรับจัดการข้อมูล Loan ที่มี endpoints ดังนี้:

### Required Endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/loans` | Create new loan |
| GET | `/loans` | List all loans (with filters) |
| GET | `/loans/{loan_id}` | Get loan by ID |
| PUT | `/loans/{loan_id}` | Update loan |
| DELETE | `/loans/{loan_id}` | Delete loan |
| GET | `/loans/stats` | Get loan statistics |

---

## 💻 Part 1: Project Structure

สร้างโครงสร้างไฟล์:

```
lab1-api-design/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── database.py
├── requirements.txt
└── README.md
```

### requirements.txt
```
fastapi==0.109.0
uvicorn==0.27.0
pydantic==2.5.3
```

---

## 💻 Part 2: Pydantic Schemas (1%)

สร้าง `app/schemas.py`:

```python
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

class LoanStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    CURRENT = "current"
    PAID = "paid"
    LATE = "late"
    DEFAULT = "default"

class LoanPurpose(str, Enum):
    PERSONAL = "personal"
    EDUCATION = "education"
    HOME = "home"
    BUSINESS = "business"
    MEDICAL = "medical"
    OTHER = "other"

# TODO: Complete the schemas below

class LoanBase(BaseModel):
    """Base schema for Loan"""
    borrower_name: str = Field(..., min_length=2, max_length=100)
    borrower_email: EmailStr
    amount: float = Field(..., gt=0, le=1000000, description="Loan amount in THB")
    term_months: int = Field(..., ge=12, le=60, description="Loan term in months")
    purpose: LoanPurpose = LoanPurpose.PERSONAL
    
    @field_validator('term_months')
    @classmethod
    def validate_term(cls, v):
        valid_terms = [12, 24, 36, 48, 60]
        if v not in valid_terms:
            raise ValueError(f'Term must be one of {valid_terms}')
        return v
    
    # TODO: Add more validators
    # - amount must be in increments of 1000
    # - borrower_name must not contain numbers

class LoanCreate(LoanBase):
    """Schema for creating a new loan"""
    pass
    
    class Config:
        json_schema_extra = {
            "example": {
                "borrower_name": "John Doe",
                "borrower_email": "john@example.com",
                "amount": 100000,
                "term_months": 36,
                "purpose": "personal"
            }
        }

class LoanUpdate(BaseModel):
    """Schema for updating a loan"""
    borrower_name: Optional[str] = Field(None, min_length=2, max_length=100)
    borrower_email: Optional[EmailStr] = None
    amount: Optional[float] = Field(None, gt=0, le=1000000)
    term_months: Optional[int] = Field(None, ge=12, le=60)
    purpose: Optional[LoanPurpose] = None
    status: Optional[LoanStatus] = None

class LoanResponse(LoanBase):
    """Schema for loan response"""
    id: int
    status: LoanStatus = LoanStatus.PENDING
    interest_rate: float
    monthly_payment: float
    total_payment: float
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class LoanListResponse(BaseModel):
    """Schema for paginated loan list"""
    total: int
    page: int
    per_page: int
    loans: List[LoanResponse]

class LoanStats(BaseModel):
    """Schema for loan statistics"""
    total_loans: int
    total_amount: float
    average_amount: float
    status_breakdown: dict
    purpose_breakdown: dict
```

---

## 💻 Part 3: In-Memory Database (Reference)

สร้าง `app/database.py`:

```python
from datetime import datetime
from typing import Dict, List, Optional

# In-memory database
loans_db: Dict[int, dict] = {}
loan_id_counter = 0

def get_next_id() -> int:
    global loan_id_counter
    loan_id_counter += 1
    return loan_id_counter

def calculate_loan_details(amount: float, term_months: int) -> dict:
    """Calculate interest rate and payments based on amount and term"""
    # Interest rate based on amount
    if amount <= 100000:
        rate = 7.5
    elif amount <= 300000:
        rate = 8.0
    elif amount <= 500000:
        rate = 8.5
    else:
        rate = 9.0
    
    # Calculate monthly payment (simple interest)
    total_interest = amount * (rate / 100) * (term_months / 12)
    total_payment = amount + total_interest
    monthly_payment = total_payment / term_months
    
    return {
        "interest_rate": rate,
        "monthly_payment": round(monthly_payment, 2),
        "total_payment": round(total_payment, 2)
    }

def create_loan(loan_data: dict) -> dict:
    """Create a new loan"""
    loan_id = get_next_id()
    details = calculate_loan_details(loan_data["amount"], loan_data["term_months"])
    
    loan = {
        "id": loan_id,
        **loan_data,
        **details,
        "status": "pending",
        "created_at": datetime.now(),
        "updated_at": None
    }
    
    loans_db[loan_id] = loan
    return loan

def get_loan(loan_id: int) -> Optional[dict]:
    """Get loan by ID"""
    return loans_db.get(loan_id)

def get_all_loans() -> List[dict]:
    """Get all loans"""
    return list(loans_db.values())

def update_loan(loan_id: int, update_data: dict) -> Optional[dict]:
    """Update a loan"""
    if loan_id not in loans_db:
        return None
    
    loan = loans_db[loan_id]
    
    for key, value in update_data.items():
        if value is not None:
            loan[key] = value
    
    # Recalculate if amount or term changed
    if "amount" in update_data or "term_months" in update_data:
        details = calculate_loan_details(loan["amount"], loan["term_months"])
        loan.update(details)
    
    loan["updated_at"] = datetime.now()
    loans_db[loan_id] = loan
    
    return loan

def delete_loan(loan_id: int) -> bool:
    """Delete a loan"""
    if loan_id in loans_db:
        del loans_db[loan_id]
        return True
    return False

def get_loan_stats() -> dict:
    """Get loan statistics"""
    loans = list(loans_db.values())
    
    if not loans:
        return {
            "total_loans": 0,
            "total_amount": 0,
            "average_amount": 0,
            "status_breakdown": {},
            "purpose_breakdown": {}
        }
    
    total_amount = sum(l["amount"] for l in loans)
    
    status_breakdown = {}
    for loan in loans:
        status = loan["status"]
        status_breakdown[status] = status_breakdown.get(status, 0) + 1
    
    purpose_breakdown = {}
    for loan in loans:
        purpose = loan["purpose"]
        purpose_breakdown[purpose] = purpose_breakdown.get(purpose, 0) + 1
    
    return {
        "total_loans": len(loans),
        "total_amount": total_amount,
        "average_amount": round(total_amount / len(loans), 2),
        "status_breakdown": status_breakdown,
        "purpose_breakdown": purpose_breakdown
    }
```

---

## 💻 Part 4: FastAPI Main Application (1.5%)

สร้าง `app/main.py`:

```python
from fastapi import FastAPI, HTTPException, Query, Path, status
from typing import Optional, List

from .schemas import (
    LoanCreate, LoanUpdate, LoanResponse, 
    LoanListResponse, LoanStats, LoanStatus, LoanPurpose
)
from . import database as db

app = FastAPI(
    title="Loan Management API",
    description="""
    ## CSI403 Lab 1: API Design
    
    REST API for managing loans with the following features:
    * **Create** new loan applications
    * **Read** loan information
    * **Update** loan details
    * **Delete** loans
    * **Statistics** and reporting
    """,
    version="1.0.0",
    contact={
        "name": "Group X",
        "email": "groupx@example.com"
    }
)

# ============ HEALTH CHECK ============

@app.get("/", tags=["Health"])
def root():
    """API Health Check"""
    return {
        "message": "Loan Management API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "total_loans": len(db.loans_db)
    }

# ============ CRUD OPERATIONS ============

# TODO: Implement the following endpoints

@app.post("/loans", response_model=LoanResponse, status_code=status.HTTP_201_CREATED, tags=["Loans"])
def create_loan(loan: LoanCreate):
    """
    Create a new loan application.
    
    - **borrower_name**: Name of the borrower (2-100 characters)
    - **borrower_email**: Valid email address
    - **amount**: Loan amount (10,000 - 1,000,000 THB)
    - **term_months**: Loan term (12, 24, 36, 48, or 60 months)
    - **purpose**: Loan purpose
    """
    # TODO: Implement this endpoint
    pass

@app.get("/loans", response_model=LoanListResponse, tags=["Loans"])
def list_loans(
    status: Optional[LoanStatus] = Query(None, description="Filter by status"),
    purpose: Optional[LoanPurpose] = Query(None, description="Filter by purpose"),
    min_amount: Optional[float] = Query(None, ge=0, description="Minimum loan amount"),
    max_amount: Optional[float] = Query(None, le=1000000, description="Maximum loan amount"),
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=100, description="Items per page")
):
    """
    List all loans with optional filters and pagination.
    """
    # TODO: Implement this endpoint with filtering and pagination
    pass

@app.get("/loans/stats", response_model=LoanStats, tags=["Statistics"])
def get_statistics():
    """
    Get loan statistics including:
    - Total number of loans
    - Total and average loan amount
    - Breakdown by status
    - Breakdown by purpose
    """
    # TODO: Implement this endpoint
    pass

@app.get("/loans/{loan_id}", response_model=LoanResponse, tags=["Loans"])
def get_loan(
    loan_id: int = Path(..., gt=0, description="Loan ID")
):
    """
    Get a specific loan by ID.
    """
    # TODO: Implement this endpoint
    # Return 404 if loan not found
    pass

@app.put("/loans/{loan_id}", response_model=LoanResponse, tags=["Loans"])
def update_loan(
    loan_id: int = Path(..., gt=0, description="Loan ID"),
    loan_update: LoanUpdate = ...
):
    """
    Update a loan's information.
    
    Only provided fields will be updated.
    """
    # TODO: Implement this endpoint
    # Return 404 if loan not found
    pass

@app.delete("/loans/{loan_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Loans"])
def delete_loan(
    loan_id: int = Path(..., gt=0, description="Loan ID")
):
    """
    Delete a loan by ID.
    """
    # TODO: Implement this endpoint
    # Return 404 if loan not found
    pass

# ============ ADDITIONAL ENDPOINTS (BONUS) ============

@app.patch("/loans/{loan_id}/status", response_model=LoanResponse, tags=["Loans"])
def update_loan_status(
    loan_id: int = Path(..., gt=0),
    new_status: LoanStatus = Query(..., description="New status")
):
    """
    Update only the status of a loan.
    """
    # BONUS: Implement status-only update
    pass
```

---

## 💻 Part 5: Error Handling (1%)

เพิ่ม Error Handling ใน `app/main.py`:

```python
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# Custom exception
class LoanNotFoundException(Exception):
    def __init__(self, loan_id: int):
        self.loan_id = loan_id

@app.exception_handler(LoanNotFoundException)
async def loan_not_found_handler(request: Request, exc: LoanNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "LoanNotFound",
            "message": f"Loan with ID {exc.loan_id} not found",
            "loan_id": exc.loan_id
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(x) for x in error["loc"][1:]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    return JSONResponse(
        status_code=422,
        content={
            "error": "ValidationError",
            "message": "Request validation failed",
            "details": errors
        }
    )
```

---

## 💻 Part 6: Testing Your API

### Run the Server
```bash
cd lab1-api-design
uvicorn app.main:app --reload
```

### Test with Swagger UI
เปิด browser ไปที่: http://127.0.0.1:8000/docs

### Test with curl

```bash
# Create loan
curl -X POST "http://localhost:8000/loans" \
  -H "Content-Type: application/json" \
  -d '{
    "borrower_name": "John Doe",
    "borrower_email": "john@example.com",
    "amount": 100000,
    "term_months": 36,
    "purpose": "personal"
  }'

# List loans
curl "http://localhost:8000/loans"

# Get loan by ID
curl "http://localhost:8000/loans/1"

# Update loan
curl -X PUT "http://localhost:8000/loans/1" \
  -H "Content-Type: application/json" \
  -d '{"status": "approved"}'

# Delete loan
curl -X DELETE "http://localhost:8000/loans/1"

# Get statistics
curl "http://localhost:8000/loans/stats"
```

---

## 📤 Submission

### Repository Structure
```
group-repo/
└── lab1-api-design/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── schemas.py
    │   └── database.py
    ├── requirements.txt
    └── README.md
```

### README.md Template
```markdown
# Lab 1: API Design - Group X

## Team Members
- Member 1 (ID)
- Member 2 (ID)
- Member 3 (ID)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /loans | Create loan |
| GET | /loans | List loans |
| GET | /loans/{id} | Get loan |
| PUT | /loans/{id} | Update loan |
| DELETE | /loans/{id} | Delete loan |
| GET | /loans/stats | Statistics |

## How to Run
\`\`\`bash
pip install -r requirements.txt
uvicorn app.main:app --reload
\`\`\`

## API Documentation
http://localhost:8000/docs

## Screenshots
[Include Swagger UI screenshots]
```

### Git Commands
```bash
git add lab1-api-design/
git commit -m "Lab 1: API Design - Complete"
git push origin main
```

---

## ✅ Checklist Before Submission

- [ ] All 6 endpoints implemented
- [ ] Pydantic schemas with validation
- [ ] Error handling (404, 422)
- [ ] Swagger documentation works
- [ ] Code is clean and commented
- [ ] README.md is complete
- [ ] Tested all endpoints

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 5
