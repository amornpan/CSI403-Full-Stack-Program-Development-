"""
CSI403 Full Stack Development
Pydantic Schemas - Data Validation
"""

from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

# ============================================
# ENUMS (matching models.py)
# ============================================

class UserRole(str, Enum):
    ADMIN = "admin"
    BORROWER = "borrower"

class LoanStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    CURRENT = "current"
    IN_GRACE_PERIOD = "in_grace_period"
    LATE_16_30 = "late_16_30"
    LATE_31_120 = "late_31_120"
    DEFAULT = "default"
    CHARGED_OFF = "charged_off"
    FULLY_PAID = "fully_paid"
    REJECTED = "rejected"

# ============================================
# USER SCHEMAS
# ============================================

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    confirm_password: str
    
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# ============================================
# BORROWER SCHEMAS
# ============================================

class BorrowerBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    emp_title: Optional[str] = None
    emp_length: Optional[int] = Field(None, ge=0, le=50)
    annual_income: float = Field(..., gt=0)
    home_ownership: Optional[str] = "rent"
    grade: Optional[str] = None
    sub_grade: Optional[str] = None

class BorrowerCreate(BorrowerBase):
    pass

class BorrowerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    emp_title: Optional[str] = None
    emp_length: Optional[int] = None
    annual_income: Optional[float] = None
    home_ownership: Optional[str] = None

class BorrowerResponse(BorrowerBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ============================================
# LOAN SCHEMAS
# ============================================

class LoanBase(BaseModel):
    loan_amount: float = Field(..., gt=0, le=10000000, description="Loan amount in THB")
    term: int = Field(..., description="Loan term in months (12, 24, 36, 48, or 60)")
    purpose: Optional[str] = None
    description: Optional[str] = None
    
    @validator('term')
    def validate_term(cls, v):
        valid_terms = [12, 24, 36, 48, 60]
        if v not in valid_terms:
            raise ValueError(f'Term must be one of {valid_terms}')
        return v
    
    @validator('loan_amount')
    def validate_amount(cls, v):
        if v < 10000:
            raise ValueError('Minimum loan amount is 10,000 THB')
        return v

class LoanCreate(LoanBase):
    pass

class LoanUpdate(BaseModel):
    status: Optional[LoanStatus] = None
    funded_amount: Optional[float] = None
    interest_rate: Optional[float] = None
    installment: Optional[float] = None

class LoanResponse(LoanBase):
    id: int
    borrower_id: int
    funded_amount: float
    interest_rate: float
    installment: float
    status: LoanStatus
    application_date: datetime
    issue_date: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class LoanListResponse(BaseModel):
    loans: List[LoanResponse]
    total: int
    page: int
    per_page: int

# ============================================
# PAYMENT SCHEMAS
# ============================================

class PaymentBase(BaseModel):
    payment_amount: float = Field(..., gt=0)

class PaymentCreate(PaymentBase):
    loan_id: int

class PaymentResponse(PaymentBase):
    id: int
    loan_id: int
    payment_date: datetime
    principal: float
    interest: float
    late_fee: float
    remaining_balance: float
    is_late: bool
    days_late: int
    
    class Config:
        from_attributes = True

# ============================================
# STATUS HISTORY SCHEMAS
# ============================================

class StatusHistoryResponse(BaseModel):
    id: int
    loan_id: int
    previous_status: Optional[str]
    new_status: str
    changed_by: Optional[int]
    notes: Optional[str]
    changed_at: datetime
    
    class Config:
        from_attributes = True

# ============================================
# DASHBOARD SCHEMAS
# ============================================

class DashboardStats(BaseModel):
    total_loans: int
    active_loans: int
    total_borrowed: float
    total_paid: float
    pending_applications: int

class AdminDashboardStats(DashboardStats):
    total_users: int
    total_borrowers: int
    default_rate: float
    total_funded: float

# ============================================
# API RESPONSE SCHEMAS
# ============================================

class MessageResponse(BaseModel):
    message: str
    success: bool = True

class ErrorResponse(BaseModel):
    detail: str
    error_code: Optional[str] = None
