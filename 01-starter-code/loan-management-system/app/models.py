"""
CSI403 Full Stack Development
Database Models - SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum

# ============================================
# ENUMS
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

class HomeOwnership(str, Enum):
    RENT = "rent"
    OWN = "own"
    MORTGAGE = "mortgage"
    OTHER = "other"

class Grade(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

# ============================================
# MODELS
# ============================================

# Import Base from database module
from database import Base

class User(Base):
    """User account for authentication"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default=UserRole.BORROWER.value)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship
    borrower = relationship("Borrower", back_populates="user", uselist=False)
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, role={self.role})>"


class Borrower(Base):
    """Borrower profile information"""
    __tablename__ = "borrowers"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Personal information
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(10))
    
    # Employment information
    emp_title = Column(String(100))  # Job title
    emp_length = Column(Integer)  # Years employed
    annual_income = Column(Float)
    
    # Housing
    home_ownership = Column(String(20), default=HomeOwnership.RENT.value)
    
    # Credit information
    grade = Column(String(1))  # A-G
    sub_grade = Column(String(2))  # A1-G5
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="borrower")
    loans = relationship("Loan", back_populates="borrower")
    
    def __repr__(self):
        return f"<Borrower(id={self.id}, name={self.first_name} {self.last_name})>"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Loan(Base):
    """Loan application and details"""
    __tablename__ = "loans"
    
    id = Column(Integer, primary_key=True, index=True)
    borrower_id = Column(Integer, ForeignKey("borrowers.id"), nullable=False)
    
    # Loan details
    loan_amount = Column(Float, nullable=False)
    funded_amount = Column(Float, default=0)
    term = Column(Integer, nullable=False)  # months (36 or 60)
    interest_rate = Column(Float, nullable=False)
    installment = Column(Float)  # monthly payment
    
    # Purpose
    purpose = Column(String(50))
    description = Column(Text)
    
    # Status
    status = Column(String(30), default=LoanStatus.PENDING.value)
    
    # Dates
    application_date = Column(DateTime(timezone=True), server_default=func.now())
    issue_date = Column(DateTime(timezone=True))  # When approved/funded
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    borrower = relationship("Borrower", back_populates="loans")
    payments = relationship("Payment", back_populates="loan")
    status_history = relationship("LoanStatusHistory", back_populates="loan")
    
    def __repr__(self):
        return f"<Loan(id={self.id}, amount={self.loan_amount}, status={self.status})>"
    
    @property
    def loan_id_formatted(self):
        """Generate formatted loan ID: LN-YYMM-XXXXX"""
        if self.application_date:
            return f"LN-{self.application_date.strftime('%y%m')}-{self.id:05d}"
        return f"LN-0000-{self.id:05d}"


class Payment(Base):
    """Payment records"""
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    
    # Payment details
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    payment_amount = Column(Float, nullable=False)
    principal = Column(Float, default=0)
    interest = Column(Float, default=0)
    late_fee = Column(Float, default=0)
    
    # Balance after payment
    remaining_balance = Column(Float)
    
    # Status
    is_late = Column(Boolean, default=False)
    days_late = Column(Integer, default=0)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    loan = relationship("Loan", back_populates="payments")
    
    def __repr__(self):
        return f"<Payment(id={self.id}, loan_id={self.loan_id}, amount={self.payment_amount})>"


class LoanStatusHistory(Base):
    """Audit trail for loan status changes"""
    __tablename__ = "loan_status_history"
    
    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    
    # Status change
    previous_status = Column(String(30))
    new_status = Column(String(30), nullable=False)
    
    # Who made the change
    changed_by = Column(Integer, ForeignKey("users.id"))
    
    # Notes
    notes = Column(Text)
    
    # Timestamp
    changed_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    loan = relationship("Loan", back_populates="status_history")
    
    def __repr__(self):
        return f"<LoanStatusHistory(loan_id={self.loan_id}, {self.previous_status} -> {self.new_status})>"
