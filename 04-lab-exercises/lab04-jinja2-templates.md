# Lab 04: Jinja2 Templates

**Week 4 | January 28-30, 2026 | 2%**

## 🎯 Objectives
- Understand Jinja2 template syntax
- Use variables, filters, and expressions
- Implement control structures (if, for)
- Create template inheritance with blocks

## 📋 Prerequisites
- Python with FastAPI installed
- Understanding of HTML/CSS
- VS Code

## 🔧 Setup

```bash
mkdir lab04-jinja2
cd lab04-jinja2
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn jinja2
mkdir templates
```

## 💻 Part 1: Basic Templates (20 min)

### Exercise 1.1: Setup FastAPI with Templates
Create `main.py`:
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Sample data
LOANS = [
    {"id": 1, "borrower": "Alice", "amount": 100000, "status": "current"},
    {"id": 2, "borrower": "Bob", "amount": 200000, "status": "current"},
    {"id": 3, "borrower": "Charlie", "amount": 50000, "status": "paid"},
    {"id": 4, "borrower": "Diana", "amount": 150000, "status": "late"},
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "title": "Home", "message": "Welcome to Loan System!"}
    )

@app.get("/loans", response_class=HTMLResponse)
async def loans_list(request: Request):
    return templates.TemplateResponse(
        "loans.html",
        {"request": request, "title": "Loans", "loans": LOANS}
    )

@app.get("/loans/{loan_id}", response_class=HTMLResponse)
async def loan_detail(request: Request, loan_id: int):
    loan = next((l for l in LOANS if l["id"] == loan_id), None)
    return templates.TemplateResponse(
        "loan_detail.html",
        {"request": request, "title": f"Loan #{loan_id}", "loan": loan}
    )
```

### Exercise 1.2: Simple Template
Create `templates/home.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    
    {# This is a Jinja2 comment - won't appear in HTML #}
    
    <nav>
        <a href="/">Home</a> |
        <a href="/loans">View Loans</a>
    </nav>
</body>
</html>
```

Run and test:
```bash
uvicorn main:app --reload
# Visit http://127.0.0.1:8000
```

## 💻 Part 2: Variables & Filters (25 min)

### Exercise 2.1: Using Filters
Create `templates/loans.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #800000; color: white; }
        .status-current { color: green; }
        .status-paid { color: blue; }
        .status-late { color: red; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    
    <p>Total Loans: {{ loans | length }}</p>
    
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>Borrower</th>
                <th>Amount</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for loan in loans %}
            <tr>
                <td>{{ loop.index }}</td>
                <td>{{ loan.borrower | upper }}</td>
                <td>{{ "{:,.0f}".format(loan.amount) }} THB</td>
                <td class="status-{{ loan.status }}">
                    {{ loan.status | capitalize }}
                </td>
                <td>
                    <a href="/loans/{{ loan.id }}">View</a>
                </td>
            </tr>
            {% else %}
            <tr>
                <td colspan="5">No loans found.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <p><a href="/">Back to Home</a></p>
</body>
</html>
```

### Exercise 2.2: Custom Filters
Update `main.py` to add custom filters:
```python
# Add after templates = Jinja2Templates(...)

def format_currency(value):
    """Format number as Thai Baht"""
    return f"{value:,.2f} THB"

def format_status_badge(status):
    """Return Bootstrap badge class based on status"""
    badges = {
        "current": "success",
        "paid": "info",
        "late": "warning",
        "default": "danger",
        "pending": "secondary"
    }
    return badges.get(status, "secondary")

# Register custom filters
templates.env.filters["currency"] = format_currency
templates.env.filters["status_badge"] = format_status_badge
```

Now use in template:
```html
<td>{{ loan.amount | currency }}</td>
<td>
    <span class="badge bg-{{ loan.status | status_badge }}">
        {{ loan.status | capitalize }}
    </span>
</td>
```

## 💻 Part 3: Control Structures (25 min)

### Exercise 3.1: Conditionals
Create `templates/loan_detail.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        .card { border: 1px solid #ddd; padding: 20px; max-width: 400px; margin: 20px 0; }
        .alert { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-warning { background: #fff3cd; color: #856404; }
        .alert-danger { background: #f8d7da; color: #721c24; }
        .btn { padding: 8px 16px; text-decoration: none; border-radius: 4px; }
        .btn-primary { background: #800000; color: white; }
        .btn-success { background: #28a745; color: white; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    
    {% if loan %}
        <div class="card">
            <h2>Loan Details</h2>
            <p><strong>ID:</strong> {{ loan.id }}</p>
            <p><strong>Borrower:</strong> {{ loan.borrower }}</p>
            <p><strong>Amount:</strong> {{ loan.amount | currency }}</p>
            <p><strong>Status:</strong> 
                {% if loan.status == "current" %}
                    <span style="color: green;">● Current</span>
                {% elif loan.status == "paid" %}
                    <span style="color: blue;">● Fully Paid</span>
                {% elif loan.status == "late" %}
                    <span style="color: orange;">● Late Payment</span>
                {% elif loan.status == "default" %}
                    <span style="color: red;">● Default</span>
                {% else %}
                    <span style="color: gray;">● {{ loan.status | capitalize }}</span>
                {% endif %}
            </p>
            
            {# Show action buttons based on status #}
            {% if loan.status == "current" %}
                <div class="alert alert-success">
                    This loan is in good standing.
                </div>
                <a href="#" class="btn btn-success">Make Payment</a>
            {% elif loan.status == "late" %}
                <div class="alert alert-warning">
                    ⚠️ This loan has a late payment. Please pay soon to avoid penalties.
                </div>
                <a href="#" class="btn btn-primary">Pay Now</a>
            {% elif loan.status == "default" %}
                <div class="alert alert-danger">
                    ❌ This loan is in default. Please contact support immediately.
                </div>
            {% endif %}
        </div>
    {% else %}
        <div class="alert alert-danger">
            Loan not found!
        </div>
    {% endif %}
    
    <p><a href="/loans">← Back to Loans</a></p>
</body>
</html>
```

### Exercise 3.2: Loop Variables
Create `templates/payment_schedule.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Payment Schedule</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background: #800000; color: white; }
        tr:nth-child(even) { background: #f9f9f9; }
        tr:hover { background: #f1f1f1; }
        .first-row { font-weight: bold; }
        .last-row { background: #e8f5e9 !important; }
    </style>
</head>
<body>
    <h1>Payment Schedule</h1>
    
    <table>
        <thead>
            <tr>
                <th>Month</th>
                <th>Payment</th>
                <th>Principal</th>
                <th>Interest</th>
                <th>Balance</th>
            </tr>
        </thead>
        <tbody>
            {% for payment in payments %}
            <tr class="{% if loop.first %}first-row{% endif %} {% if loop.last %}last-row{% endif %}">
                <td>
                    {{ loop.index }} of {{ loop.length }}
                    {% if loop.first %} (First){% endif %}
                    {% if loop.last %} (Last){% endif %}
                </td>
                <td>{{ payment.amount | currency }}</td>
                <td>{{ payment.principal | currency }}</td>
                <td>{{ payment.interest | currency }}</td>
                <td>{{ payment.balance | currency }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <h3>Summary</h3>
    <p>Total Payments: {{ payments | length }}</p>
    <p>Total Amount: {{ payments | sum(attribute='amount') | currency }}</p>
</body>
</html>
```

Add route in `main.py`:
```python
@app.get("/schedule", response_class=HTMLResponse)
async def payment_schedule(request: Request):
    # Generate sample payment schedule
    payments = []
    balance = 100000
    monthly_payment = 3500
    rate = 0.075 / 12
    
    for month in range(1, 37):
        interest = balance * rate
        principal = monthly_payment - interest
        balance -= principal
        if balance < 0:
            balance = 0
        
        payments.append({
            "amount": monthly_payment,
            "principal": principal,
            "interest": interest,
            "balance": balance
        })
    
    return templates.TemplateResponse(
        "payment_schedule.html",
        {"request": request, "payments": payments}
    )
```

## 💻 Part 4: Template Inheritance (30 min)

### Exercise 4.1: Base Template
Create `templates/base.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Loan System{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {# Navigation #}
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-bank2"></i> Loan System
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    {% block nav_items %}
                    <li class="nav-item">
                        <a class="nav-link" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/loans">Loans</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/schedule">Schedule</a>
                    </li>
                    {% endblock %}
                </ul>
                <ul class="navbar-nav">
                    {% block nav_right %}
                    <li class="nav-item">
                        <a class="nav-link" href="/login">Login</a>
                    </li>
                    {% endblock %}
                </ul>
            </div>
        </div>
    </nav>
    
    {# Flash Messages #}
    {% if messages %}
    <div class="container mt-3">
        {% for category, message in messages %}
        <div class="alert alert-{{ category }} alert-dismissible fade show">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
        {% endfor %}
    </div>
    {% endif %}
    
    {# Main Content #}
    <main class="container my-4">
        {% block content %}
        <p>No content provided.</p>
        {% endblock %}
    </main>
    
    {# Footer #}
    <footer class="bg-dark text-white py-3 mt-auto">
        <div class="container text-center">
            {% block footer %}
            <p class="mb-0">&copy; 2026 CSI403 Full Stack Development</p>
            {% endblock %}
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Exercise 4.2: Child Templates
Create `templates/pages/home.html`:
```html
{% extends "base.html" %}

{% block title %}Home - Loan System{% endblock %}

{% block content %}
<div class="row">
    <div class="col-lg-8">
        <h1>Welcome to Loan Management System</h1>
        <p class="lead">Manage your loans efficiently with our comprehensive platform.</p>
        
        <div class="row mt-4">
            <div class="col-md-4">
                <div class="card text-center">
                    <div class="card-body">
                        <i class="bi bi-cash-stack text-success" style="font-size: 2rem;"></i>
                        <h5 class="mt-2">Active Loans</h5>
                        <h2>{{ stats.active_loans }}</h2>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-center">
                    <div class="card-body">
                        <i class="bi bi-currency-dollar text-primary" style="font-size: 2rem;"></i>
                        <h5 class="mt-2">Total Amount</h5>
                        <h2>{{ stats.total_amount | currency }}</h2>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-center">
                    <div class="card-body">
                        <i class="bi bi-check-circle text-info" style="font-size: 2rem;"></i>
                        <h5 class="mt-2">Paid Off</h5>
                        <h2>{{ stats.paid_loans }}</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-lg-4">
        <div class="card">
            <div class="card-header bg-primary text-white">
                Quick Actions
            </div>
            <div class="list-group list-group-flush">
                <a href="/loans" class="list-group-item list-group-item-action">
                    <i class="bi bi-list"></i> View All Loans
                </a>
                <a href="/apply" class="list-group-item list-group-item-action">
                    <i class="bi bi-plus-circle"></i> Apply for Loan
                </a>
                <a href="/schedule" class="list-group-item list-group-item-action">
                    <i class="bi bi-calendar"></i> Payment Schedule
                </a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

Update `main.py` home route:
```python
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    stats = {
        "active_loans": sum(1 for l in LOANS if l["status"] in ["current", "late"]),
        "total_amount": sum(l["amount"] for l in LOANS),
        "paid_loans": sum(1 for l in LOANS if l["status"] == "paid")
    }
    return templates.TemplateResponse(
        "pages/home.html",
        {"request": request, "stats": stats}
    )
```

## 📝 Assignment

Create a complete loan application page that:
1. Extends `base.html`
2. Has a multi-step form (use cards)
3. Shows loan calculation preview
4. Uses proper Jinja2 features

## 📤 Submission
```bash
git add .
git commit -m "Lab 04: Jinja2 templates"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Basic templates | 0.5% |
| Filters & variables | 0.5% |
| Control structures | 0.5% |
| Template inheritance | 0.5% |

---
**Deadline:** Before Week 5 class
