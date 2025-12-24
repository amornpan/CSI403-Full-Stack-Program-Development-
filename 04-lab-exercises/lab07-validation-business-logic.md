# Lab 07: Pydantic Validation & Business Logic

**Week 7 | February 18-20, 2026 | 2%**

## 🎯 Objectives
- Implement data validation with Pydantic
- Create business logic layer
- Handle validation errors gracefully
- Apply loan-specific validation rules

## 💻 Part 1: Advanced Pydantic Validation (30 min)

### Exercise 1.1: Complex Validators
Create `app/schemas.py`:
```python
from pydantic import BaseModel, Field, validator, root_validator, EmailStr
from typing import Optional, List
from datetime import date, datetime
from enum import Enum

class LoanPurpose(str, Enum):
    PERSONAL = "personal"
    EDUCATION = "education"
    HOME = "home_improvement"
    BUSINESS = "business"
    MEDICAL = "medical"
    OTHER = "other"

class LoanApplicationCreate(BaseModel):
    # Borrower info
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(..., pattern=r"^0[0-9]{9}$")
    date_of_birth: date
    annual_income: float = Field(..., gt=0)
    
    # Loan info
    loan_amount: float = Field(..., gt=10000, le=1000000)
    term_months: int = Field(..., ge=12, le=60)
    purpose: LoanPurpose
    
    # Employment
    employer_name: Optional[str] = None
    employment_years: Optional[int] = Field(None, ge=0)
    
    @validator("date_of_birth")
    def validate_age(cls, v):
        today = date.today()
        age = today.year - v.year - ((today.month, today.day) < (v.month, v.day))
        if age < 20:
            raise ValueError("Applicant must be at least 20 years old")
        if age > 65:
            raise ValueError("Applicant must be under 65 years old")
        return v
    
    @validator("phone")
    def validate_thai_phone(cls, v):
        if not v.startswith("0"):
            raise ValueError("Thai phone number must start with 0")
        if len(v) != 10:
            raise ValueError("Phone number must be 10 digits")
        return v
    
    @validator("term_months")
    def validate_term(cls, v):
        valid_terms = [12, 24, 36, 48, 60]
        if v not in valid_terms:
            raise ValueError(f"Term must be one of {valid_terms}")
        return v
    
    @root_validator
    def validate_loan_to_income(cls, values):
        income = values.get("annual_income", 0)
        amount = values.get("loan_amount", 0)
        
        if income > 0 and amount > 0:
            # Loan should not exceed 5x annual income
            if amount > income * 5:
                raise ValueError(
                    f"Loan amount ({amount:,.0f}) cannot exceed 5x annual income ({income*5:,.0f})"
                )
            
            # Monthly payment should not exceed 40% of monthly income
            monthly_income = income / 12
            term = values.get("term_months", 36)
            rate = 0.075  # 7.5%
            monthly_payment = (amount * (1 + rate * term/12)) / term
            
            if monthly_payment > monthly_income * 0.4:
                raise ValueError(
                    f"Monthly payment ({monthly_payment:,.0f}) exceeds 40% of monthly income ({monthly_income*0.4:,.0f})"
                )
        
        return values
    
    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "0812345678",
                "date_of_birth": "1990-01-15",
                "annual_income": 600000,
                "loan_amount": 200000,
                "term_months": 36,
                "purpose": "personal"
            }
        }
```

### Exercise 1.2: Custom Error Messages
```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = ".".join(str(x) for x in error["loc"][1:])  # Skip 'body'
        errors.append({
            "field": field,
            "message": error["msg"],
            "type": error["type"]
        })
    
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": "Validation Error",
            "details": errors
        }
    )
```

## 💻 Part 2: Business Logic Layer (30 min)

### Exercise 2.1: Loan Business Logic
Create `app/services/loan_service.py`:
```python
from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import Optional, Tuple
import models
import crud

class LoanService:
    
    # Interest rates by grade
    INTEREST_RATES = {
        "A": 6.0,
        "B": 7.5,
        "C": 9.0,
        "D": 11.0,
        "E": 13.0,
        "F": 15.0,
    }
    
    # Maximum loan amounts by grade
    MAX_AMOUNTS = {
        "A": 1000000,
        "B": 750000,
        "C": 500000,
        "D": 300000,
        "E": 200000,
        "F": 100000,
    }
    
    @staticmethod
    def calculate_grade(annual_income: float, employment_years: int) -> str:
        """Calculate borrower grade based on income and employment"""
        score = 0
        
        # Income scoring (0-50 points)
        if annual_income >= 1000000:
            score += 50
        elif annual_income >= 600000:
            score += 40
        elif annual_income >= 400000:
            score += 30
        elif annual_income >= 250000:
            score += 20
        else:
            score += 10
        
        # Employment years (0-30 points)
        if employment_years >= 10:
            score += 30
        elif employment_years >= 5:
            score += 20
        elif employment_years >= 2:
            score += 10
        
        # Grade mapping
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 40:
            return "D"
        elif score >= 30:
            return "E"
        else:
            return "F"
    
    @staticmethod
    def get_interest_rate(grade: str) -> float:
        """Get interest rate for grade"""
        return LoanService.INTEREST_RATES.get(grade, 15.0)
    
    @staticmethod
    def calculate_monthly_payment(
        principal: float,
        annual_rate: float,
        term_months: int
    ) -> float:
        """Calculate monthly payment using compound interest formula"""
        monthly_rate = annual_rate / 100 / 12
        
        if monthly_rate == 0:
            return principal / term_months
        
        payment = principal * (
            monthly_rate * (1 + monthly_rate) ** term_months
        ) / (
            (1 + monthly_rate) ** term_months - 1
        )
        
        return round(payment, 2)
    
    @staticmethod
    def validate_loan_eligibility(
        borrower_id: int,
        loan_amount: float,
        db: Session
    ) -> Tuple[bool, str]:
        """Check if borrower is eligible for loan"""
        borrower = crud.get_borrower(db, borrower_id)
        
        if not borrower:
            return False, "Borrower not found"
        
        # Check existing loans
        active_loans = [
            l for l in borrower.loans 
            if l.status in ["current", "approved", "pending"]
        ]
        
        if len(active_loans) >= 3:
            return False, "Maximum 3 active loans allowed"
        
        # Check total debt
        total_debt = sum(l.loan_amount for l in active_loans)
        if total_debt + loan_amount > borrower.annual_income * 5:
            return False, "Total debt exceeds maximum allowed"
        
        # Calculate grade and check max amount
        grade = LoanService.calculate_grade(
            borrower.annual_income,
            0  # TODO: get from employment record
        )
        
        max_amount = LoanService.MAX_AMOUNTS.get(grade, 100000)
        if loan_amount > max_amount:
            return False, f"Grade {grade} allows maximum {max_amount:,.0f} THB"
        
        return True, "Eligible"
    
    @staticmethod
    def process_loan_application(
        db: Session,
        borrower_id: int,
        loan_amount: float,
        term_months: int,
        purpose: str
    ) -> dict:
        """Process a new loan application"""
        
        # Validate eligibility
        eligible, message = LoanService.validate_loan_eligibility(
            borrower_id, loan_amount, db
        )
        
        if not eligible:
            return {
                "success": False,
                "error": message
            }
        
        borrower = crud.get_borrower(db, borrower_id)
        
        # Calculate grade and rate
        grade = LoanService.calculate_grade(
            borrower.annual_income, 0
        )
        rate = LoanService.get_interest_rate(grade)
        
        # Calculate monthly payment
        monthly_payment = LoanService.calculate_monthly_payment(
            loan_amount, rate, term_months
        )
        
        # Create loan
        loan = crud.create_loan(
            db,
            borrower_id=borrower_id,
            loan_amount=loan_amount,
            term_months=term_months,
            interest_rate=rate,
            purpose=purpose
        )
        
        return {
            "success": True,
            "loan_id": loan.id,
            "grade": grade,
            "interest_rate": rate,
            "monthly_payment": monthly_payment,
            "total_payment": monthly_payment * term_months
        }
```

### Exercise 2.2: Payment Business Logic
Create `app/services/payment_service.py`:
```python
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Dict
import models
import crud

class PaymentService:
    
    LATE_FEE_RATE = 0.02  # 2% late fee
    GRACE_PERIOD_DAYS = 15
    
    @staticmethod
    def calculate_payment_breakdown(
        remaining_balance: float,
        monthly_payment: float,
        annual_rate: float
    ) -> Dict[str, float]:
        """Calculate principal and interest portions"""
        monthly_rate = annual_rate / 100 / 12
        interest = remaining_balance * monthly_rate
        principal = monthly_payment - interest
        
        return {
            "payment": monthly_payment,
            "principal": round(principal, 2),
            "interest": round(interest, 2),
            "new_balance": round(remaining_balance - principal, 2)
        }
    
    @staticmethod
    def process_payment(
        db: Session,
        loan_id: int,
        amount: float
    ) -> dict:
        """Process a loan payment"""
        loan = crud.get_loan(db, loan_id)
        
        if not loan:
            return {"success": False, "error": "Loan not found"}
        
        if loan.status == "paid":
            return {"success": False, "error": "Loan already paid off"}
        
        # Calculate current balance
        payments = crud.get_payments_by_loan(db, loan_id)
        total_paid = sum(p.amount for p in payments)
        
        # Simple calculation (for demo)
        total_due = loan.monthly_payment * loan.term_months
        remaining = total_due - total_paid
        
        if amount > remaining:
            amount = remaining  # Cap at remaining balance
        
        # Check if late
        is_late = False
        late_fee = 0
        # TODO: Implement late payment logic
        
        # Create payment record
        breakdown = PaymentService.calculate_payment_breakdown(
            remaining, loan.monthly_payment, loan.interest_rate
        )
        
        payment = crud.create_payment(
            db,
            loan_id=loan_id,
            amount=amount,
            principal=breakdown["principal"],
            interest=breakdown["interest"],
            remaining_balance=breakdown["new_balance"]
        )
        
        # Update loan status if paid off
        new_remaining = remaining - amount
        if new_remaining <= 0:
            crud.update_loan_status(db, loan_id, "paid")
        
        return {
            "success": True,
            "payment_id": payment.id,
            "amount_paid": amount,
            "remaining_balance": max(0, new_remaining),
            "loan_status": "paid" if new_remaining <= 0 else loan.status
        }
    
    @staticmethod
    def generate_payment_schedule(
        principal: float,
        annual_rate: float,
        term_months: int
    ) -> List[Dict]:
        """Generate full payment schedule"""
        monthly_rate = annual_rate / 100 / 12
        
        # Calculate fixed monthly payment
        if monthly_rate == 0:
            monthly_payment = principal / term_months
        else:
            monthly_payment = principal * (
                monthly_rate * (1 + monthly_rate) ** term_months
            ) / (
                (1 + monthly_rate) ** term_months - 1
            )
        
        schedule = []
        balance = principal
        
        for month in range(1, term_months + 1):
            interest = balance * monthly_rate
            principal_paid = monthly_payment - interest
            balance -= principal_paid
            
            schedule.append({
                "month": month,
                "payment": round(monthly_payment, 2),
                "principal": round(principal_paid, 2),
                "interest": round(interest, 2),
                "balance": round(max(0, balance), 2)
            })
        
        return schedule
```

## 📝 Assignment

1. Add these validations to `LoanApplicationCreate`:
   - ID card number validation (13 digits, valid checksum)
   - Minimum income based on loan purpose
   - Employment verification for business loans

2. Create `PaymentScheduleResponse` schema with proper formatting

3. Add endpoint to check loan eligibility before applying

## 📤 Submission
```bash
git add .
git commit -m "Lab 07: Pydantic validation and business logic"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Pydantic validators | 0.5% |
| Business logic | 0.5% |
| Error handling | 0.5% |
| Assignment | 0.5% |

---
**Deadline:** Before Week 8 class
