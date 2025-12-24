# Lab 08: Session-based Authentication

**Week 8 | February 25-27, 2026 | 2%**

## 🎯 Objectives
- Implement user registration with password hashing
- Create session-based login/logout
- Protect routes with authentication
- Implement role-based access control

## 🔧 Setup

```bash
pip install passlib[bcrypt] python-jose itsdangerous
```

## 💻 Part 1: Password Hashing (20 min)

### Exercise 1.1: Password Utilities
Create `app/auth/security.py`:
```python
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
import secrets

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)

def generate_session_token() -> str:
    """Generate a secure session token"""
    return secrets.token_urlsafe(32)

# Test
if __name__ == "__main__":
    password = "MySecurePassword123"
    hashed = hash_password(password)
    print(f"Original: {password}")
    print(f"Hashed: {hashed}")
    print(f"Verify (correct): {verify_password(password, hashed)}")
    print(f"Verify (wrong): {verify_password('wrong', hashed)}")
```

## 💻 Part 2: User Registration (25 min)

### Exercise 2.1: Registration Endpoint
Create `app/auth/router.py`:
```python
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field, validator

from database import get_db
from auth.security import hash_password, verify_password, generate_session_token
import crud

router = APIRouter(prefix="/auth", tags=["Authentication"])

# In-memory session store (use Redis in production)
sessions = {}

class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str
    
    @validator("username")
    def username_alphanumeric(cls, v):
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()
    
    @validator("password")
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain digit")
        return v
    
    @validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    # Check if username exists
    if crud.get_user_by_username(db, user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email exists
    if crud.get_user_by_email(db, user_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user with hashed password
    hashed_password = hash_password(user_data.password)
    user = crud.create_user(
        db,
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password
    )
    
    return {
        "message": "Registration successful",
        "user_id": user.id,
        "username": user.username
    }

@router.post("/login")
def login(
    credentials: UserLogin,
    response: Response,
    db: Session = Depends(get_db)
):
    # Find user
    user = crud.get_user_by_username(db, credentials.username)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Verify password
    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Check if active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled"
        )
    
    # Create session
    session_token = generate_session_token()
    sessions[session_token] = {
        "user_id": user.id,
        "username": user.username,
        "role": user.role
    }
    
    # Set cookie
    response.set_cookie(
        key="session_token",
        value=session_token,
        httponly=True,
        max_age=3600 * 24,  # 24 hours
        samesite="lax"
    )
    
    return {
        "message": "Login successful",
        "username": user.username,
        "role": user.role
    }

@router.post("/logout")
def logout(request: Request, response: Response):
    session_token = request.cookies.get("session_token")
    
    if session_token and session_token in sessions:
        del sessions[session_token]
    
    response.delete_cookie("session_token")
    
    return {"message": "Logged out successfully"}

@router.get("/me")
def get_current_user(request: Request):
    session_token = request.cookies.get("session_token")
    
    if not session_token or session_token not in sessions:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    return sessions[session_token]
```

## 💻 Part 3: Authentication Dependencies (25 min)

### Exercise 3.1: Auth Dependencies
Create `app/auth/dependencies.py`:
```python
from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import Optional
from functools import wraps

from database import get_db
from auth.router import sessions
import crud

def get_current_user(request: Request, db: Session = Depends(get_db)):
    """Get current authenticated user"""
    session_token = request.cookies.get("session_token")
    
    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    session = sessions.get(session_token)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session"
        )
    
    user = crud.get_user(db, session["user_id"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user

def get_current_active_user(current_user = Depends(get_current_user)):
    """Get current active user"""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    return current_user

def get_current_admin(current_user = Depends(get_current_active_user)):
    """Get current admin user"""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

def get_optional_user(request: Request, db: Session = Depends(get_db)):
    """Get current user if authenticated, None otherwise"""
    session_token = request.cookies.get("session_token")
    
    if not session_token:
        return None
    
    session = sessions.get(session_token)
    if not session:
        return None
    
    return crud.get_user(db, session["user_id"])
```

### Exercise 3.2: Protected Routes
```python
from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user, get_current_admin

router = APIRouter()

# Public route
@router.get("/public")
def public_route():
    return {"message": "This is public"}

# Authenticated users only
@router.get("/protected")
def protected_route(current_user = Depends(get_current_user)):
    return {
        "message": "This is protected",
        "user": current_user.username
    }

# Admin only
@router.get("/admin")
def admin_route(admin = Depends(get_current_admin)):
    return {
        "message": "Admin access granted",
        "admin": admin.username
    }

# Borrower can only see their own loans
@router.get("/my-loans")
def my_loans(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    borrower = crud.get_borrower_by_user(db, current_user.id)
    
    if not borrower:
        return {"loans": [], "message": "No borrower profile found"}
    
    loans = crud.get_loans_by_borrower(db, borrower.id)
    
    return {
        "user": current_user.username,
        "loans": [
            {
                "id": loan.id,
                "amount": loan.loan_amount,
                "status": loan.status
            }
            for loan in loans
        ]
    }
```

## 💻 Part 4: Login/Register Pages (20 min)

### Exercise 4.1: Login Template
Create `templates/auth/login.html`:
```html
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-5">
        <div class="card shadow">
            <div class="card-body p-5">
                <h3 class="text-center mb-4">
                    <i class="bi bi-box-arrow-in-right"></i> Login
                </h3>
                
                {% if error %}
                <div class="alert alert-danger">{{ error }}</div>
                {% endif %}
                
                <form method="POST" action="/auth/login">
                    <div class="mb-3">
                        <label class="form-label">Username</label>
                        <input type="text" name="username" class="form-control" required>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Password</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    
                    <div class="d-flex justify-content-between mb-3">
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="remember">
                            <label class="form-check-label" for="remember">Remember me</label>
                        </div>
                        <a href="/auth/forgot-password">Forgot password?</a>
                    </div>
                    
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
                
                <hr>
                
                <p class="text-center mb-0">
                    Don't have an account? <a href="/auth/register">Register</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Exercise 4.2: Register Template
Create `templates/auth/register.html`:
```html
{% extends "base.html" %}

{% block title %}Register{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card shadow">
            <div class="card-body p-5">
                <h3 class="text-center mb-4">
                    <i class="bi bi-person-plus"></i> Create Account
                </h3>
                
                {% if errors %}
                <div class="alert alert-danger">
                    <ul class="mb-0">
                    {% for error in errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                    </ul>
                </div>
                {% endif %}
                
                <form method="POST" action="/auth/register">
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">First Name</label>
                            <input type="text" name="first_name" class="form-control" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Last Name</label>
                            <input type="text" name="last_name" class="form-control" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Username</label>
                        <input type="text" name="username" class="form-control" required>
                        <div class="form-text">3-50 characters, letters and numbers only</div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Email</label>
                        <input type="email" name="email" class="form-control" required>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Password</label>
                        <input type="password" name="password" class="form-control" required>
                        <div class="form-text">
                            Minimum 8 characters with uppercase, lowercase, and number
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Confirm Password</label>
                        <input type="password" name="confirm_password" class="form-control" required>
                    </div>
                    
                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="terms" required>
                        <label class="form-check-label" for="terms">
                            I agree to the <a href="#">Terms and Conditions</a>
                        </label>
                    </div>
                    
                    <button type="submit" class="btn btn-primary w-100">Register</button>
                </form>
                
                <hr>
                
                <p class="text-center mb-0">
                    Already have an account? <a href="/auth/login">Login</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## 📝 Assignment

1. Implement password reset functionality
2. Add "Remember me" feature with longer session
3. Create middleware to check session on every request
4. Add rate limiting for login attempts

## 📤 Submission
```bash
git add .
git commit -m "Lab 08: Session-based authentication"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Password hashing | 0.5% |
| Login/Register | 0.5% |
| Protected routes | 0.5% |
| Templates | 0.5% |

---
**Deadline:** Before Week 9 class
