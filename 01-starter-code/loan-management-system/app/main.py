"""
CSI403 Full Stack Development
Loan Management System - Main Application
Sripatum University Chonburi
"""

from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

# Import local modules (to be created)
# from . import models, schemas, crud, auth
# from .database import engine, get_db

# Create FastAPI app
app = FastAPI(
    title="Loan Management System",
    description="CSI403 Full Stack Development Project",
    version="1.0.0"
)

# Mount static files (CSS, JS, images)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# ============================================
# ROUTES - PUBLIC
# ============================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "title": "Loan Management System"}
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page"""
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "title": "About Us"}
    )

# ============================================
# ROUTES - AUTHENTICATION
# ============================================

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Login page"""
    return templates.TemplateResponse(
        "auth/login.html",
        {"request": request, "title": "Login"}
    )

@app.post("/login")
async def login(request: Request):
    """Process login"""
    # TODO: Implement authentication
    pass

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Registration page"""
    return templates.TemplateResponse(
        "auth/register.html",
        {"request": request, "title": "Register"}
    )

@app.post("/register")
async def register(request: Request):
    """Process registration"""
    # TODO: Implement registration
    pass

@app.get("/logout")
async def logout(request: Request):
    """Logout user"""
    # TODO: Clear session
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

# ============================================
# ROUTES - BORROWER
# ============================================

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Borrower dashboard"""
    # TODO: Add authentication check
    return templates.TemplateResponse(
        "borrower/dashboard.html",
        {"request": request, "title": "Dashboard"}
    )

@app.get("/loans", response_class=HTMLResponse)
async def my_loans(request: Request):
    """View my loans"""
    # TODO: Get user's loans from database
    return templates.TemplateResponse(
        "borrower/loans.html",
        {"request": request, "title": "My Loans", "loans": []}
    )

@app.get("/loans/apply", response_class=HTMLResponse)
async def apply_loan_page(request: Request):
    """Loan application form"""
    return templates.TemplateResponse(
        "borrower/apply.html",
        {"request": request, "title": "Apply for Loan"}
    )

@app.post("/loans/apply")
async def apply_loan(request: Request):
    """Process loan application"""
    # TODO: Implement loan application
    pass

# ============================================
# ROUTES - ADMIN
# ============================================

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    """Admin dashboard"""
    # TODO: Add admin check
    return templates.TemplateResponse(
        "admin/dashboard.html",
        {"request": request, "title": "Admin Dashboard"}
    )

@app.get("/admin/loans", response_class=HTMLResponse)
async def admin_loans(request: Request):
    """View all loans"""
    # TODO: Get all loans from database
    return templates.TemplateResponse(
        "admin/loans.html",
        {"request": request, "title": "Manage Loans", "loans": []}
    )

@app.get("/admin/users", response_class=HTMLResponse)
async def admin_users(request: Request):
    """View all users"""
    # TODO: Get all users from database
    return templates.TemplateResponse(
        "admin/users.html",
        {"request": request, "title": "Manage Users", "users": []}
    )

# ============================================
# API ROUTES (for AJAX/API access)
# ============================================

@app.get("/api/health")
async def health_check():
    """API health check"""
    return {"status": "healthy", "message": "Loan Management System is running"}

@app.get("/api/loans")
async def api_get_loans():
    """Get all loans (API)"""
    # TODO: Implement with database
    return {"loans": []}

@app.get("/api/loans/{loan_id}")
async def api_get_loan(loan_id: int):
    """Get single loan (API)"""
    # TODO: Implement with database
    return {"loan_id": loan_id}


# ============================================
# RUN SERVER
# ============================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
