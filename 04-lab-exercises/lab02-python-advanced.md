# Lab 02: Python Functions, Loops & Data Structures

**Week 2 | January 14-16, 2026 | 2%**

## 🎯 Objectives
- Define and use functions
- Work with loops (for, while)
- Use lists and dictionaries
- Apply these concepts to loan calculations

## 💻 Part 1: Functions (30 min)

### Exercise 1.1: Basic Functions
Create `01_functions.py`:
```python
# Basic Functions

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def calculate_interest(principal, rate, years):
    """
    Calculate simple interest.
    
    Args:
        principal: Loan amount
        rate: Annual interest rate (%)
        years: Loan term
    
    Returns:
        Interest amount
    """
    return principal * (rate / 100) * years

def calculate_monthly_payment(principal, rate, years):
    """Calculate monthly payment for a loan"""
    total_interest = calculate_interest(principal, rate, years)
    total = principal + total_interest
    months = years * 12
    return total / months

# Test functions
print(greet("CSI403 Student"))

principal = 100000
rate = 7.5
years = 3

interest = calculate_interest(principal, rate, years)
monthly = calculate_monthly_payment(principal, rate, years)

print(f"\nLoan Amount: {principal:,.2f} THB")
print(f"Interest: {interest:,.2f} THB")
print(f"Monthly Payment: {monthly:,.2f} THB")
```

### Exercise 1.2: Functions with Default Parameters
Create `02_default_params.py`:
```python
# Functions with Default Parameters

def create_loan(
    amount,
    term=36,          # Default 36 months
    rate=7.5,         # Default 7.5%
    purpose="personal"
):
    """Create a loan dictionary with default values"""
    monthly = (amount * (1 + rate/100 * term/12)) / term
    
    return {
        "amount": amount,
        "term": term,
        "rate": rate,
        "purpose": purpose,
        "monthly_payment": round(monthly, 2)
    }

# Create loans with different parameters
loan1 = create_loan(100000)  # All defaults
loan2 = create_loan(200000, term=60)  # Custom term
loan3 = create_loan(500000, rate=6.5, purpose="business")

print("Loan 1:", loan1)
print("Loan 2:", loan2)
print("Loan 3:", loan3)
```

## 💻 Part 2: Loops (30 min)

### Exercise 2.1: For Loops
Create `03_for_loops.py`:
```python
# For Loops

# Loop through list
loan_amounts = [50000, 100000, 150000, 200000, 250000]

print("=== Loan Options ===")
for amount in loan_amounts:
    print(f"  • {amount:,} THB")

# With index
print("\n=== Numbered List ===")
for i, amount in enumerate(loan_amounts, start=1):
    print(f"  {i}. {amount:,} THB")

# Range
print("\n=== Payment Schedule (First 6 months) ===")
balance = 100000
monthly_payment = 10000

for month in range(1, 7):
    interest = balance * 0.075 / 12
    principal = monthly_payment - interest
    balance -= principal
    print(f"Month {month}: Payment={monthly_payment:,.0f}, "
          f"Principal={principal:,.0f}, Interest={interest:,.0f}, "
          f"Balance={balance:,.0f}")
```

### Exercise 2.2: While Loops
Create `04_while_loops.py`:
```python
# While Loops

# Loan payoff simulation
balance = 100000
monthly_payment = 5000
annual_rate = 7.5
month = 0

print("=== Loan Payoff Schedule ===")
print(f"Initial Balance: {balance:,.2f} THB")
print(f"Monthly Payment: {monthly_payment:,.2f} THB")
print("-" * 50)

while balance > 0:
    month += 1
    interest = balance * (annual_rate / 100) / 12
    principal = min(monthly_payment - interest, balance)
    balance -= principal
    
    if balance < 0:
        balance = 0
    
    if month <= 12 or balance == 0:  # Show first year and final
        print(f"Month {month:3d}: Principal={principal:8,.2f}, "
              f"Interest={interest:8,.2f}, Balance={balance:10,.2f}")
    elif month == 13:
        print("...")

print("-" * 50)
print(f"Loan paid off in {month} months ({month/12:.1f} years)")
```

### Exercise 2.3: Loop Control
Create `05_loop_control.py`:
```python
# Loop Control: break, continue

# Find first loan over threshold
loans = [
    {"id": 1, "amount": 50000, "status": "paid"},
    {"id": 2, "amount": 150000, "status": "current"},
    {"id": 3, "amount": 200000, "status": "current"},
    {"id": 4, "amount": 75000, "status": "late"},
]

# Find first loan over 100,000
print("=== Finding Large Loans ===")
for loan in loans:
    if loan["amount"] > 100000:
        print(f"Found: Loan #{loan['id']} - {loan['amount']:,} THB")
        break

# Skip paid loans
print("\n=== Active Loans Only ===")
for loan in loans:
    if loan["status"] == "paid":
        continue  # Skip paid loans
    print(f"Loan #{loan['id']}: {loan['amount']:,} THB ({loan['status']})")
```

## 💻 Part 3: Data Structures (30 min)

### Exercise 3.1: Lists
Create `06_lists.py`:
```python
# Working with Lists

# Create list
loan_amounts = [100000, 50000, 200000, 75000, 150000]

print("=== List Operations ===")
print(f"Original: {loan_amounts}")
print(f"Length: {len(loan_amounts)}")
print(f"Sum: {sum(loan_amounts):,}")
print(f"Average: {sum(loan_amounts)/len(loan_amounts):,.2f}")
print(f"Min: {min(loan_amounts):,}")
print(f"Max: {max(loan_amounts):,}")

# Sorting
print(f"\nSorted (asc): {sorted(loan_amounts)}")
print(f"Sorted (desc): {sorted(loan_amounts, reverse=True)}")

# Add/Remove
loan_amounts.append(300000)
print(f"\nAfter append: {loan_amounts}")

loan_amounts.insert(0, 25000)
print(f"After insert at 0: {loan_amounts}")

removed = loan_amounts.pop()
print(f"After pop: {loan_amounts} (removed: {removed})")

# List comprehension
high_loans = [amt for amt in loan_amounts if amt > 100000]
print(f"\nLoans > 100,000: {high_loans}")
```

### Exercise 3.2: Dictionaries
Create `07_dictionaries.py`:
```python
# Working with Dictionaries

# Create dictionary
borrower = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "income": 50000,
    "loans": []
}

print("=== Borrower Info ===")
print(f"Name: {borrower['name']}")
print(f"Email: {borrower.get('email', 'N/A')}")
print(f"Phone: {borrower.get('phone', 'Not provided')}")

# Add/Update
borrower["phone"] = "081-234-5678"
borrower["income"] = 55000
print(f"\nUpdated: {borrower}")

# Dictionary methods
print(f"\nKeys: {list(borrower.keys())}")
print(f"Values: {list(borrower.values())}")

# Nested data
borrower["loans"] = [
    {"id": 101, "amount": 100000, "status": "current"},
    {"id": 102, "amount": 50000, "status": "paid"}
]

print(f"\n{borrower['name']}'s Loans:")
for loan in borrower["loans"]:
    print(f"  - Loan #{loan['id']}: {loan['amount']:,} THB ({loan['status']})")
```

### Exercise 3.3: List of Dictionaries
Create `08_list_of_dicts.py`:
```python
# List of Dictionaries - Common Pattern

loans = [
    {"id": 1, "borrower": "Alice", "amount": 100000, "rate": 7.5, "status": "current"},
    {"id": 2, "borrower": "Bob", "amount": 200000, "rate": 8.0, "status": "current"},
    {"id": 3, "borrower": "Charlie", "amount": 50000, "rate": 7.0, "status": "paid"},
    {"id": 4, "borrower": "Diana", "amount": 150000, "rate": 7.5, "status": "late"},
]

# Display all loans
print("=== All Loans ===")
print(f"{'ID':<5}{'Borrower':<12}{'Amount':>12}{'Rate':>8}{'Status':<10}")
print("-" * 47)
for loan in loans:
    print(f"{loan['id']:<5}{loan['borrower']:<12}{loan['amount']:>12,}"
          f"{loan['rate']:>7.1f}%  {loan['status']:<10}")

# Filter by status
current_loans = [l for l in loans if l["status"] == "current"]
print(f"\nCurrent Loans: {len(current_loans)}")

# Calculate totals
total_amount = sum(l["amount"] for l in loans)
avg_rate = sum(l["rate"] for l in loans) / len(loans)
print(f"Total Amount: {total_amount:,} THB")
print(f"Average Rate: {avg_rate:.2f}%")

# Find by condition
large_loans = [l for l in loans if l["amount"] >= 150000]
print(f"\nLoans >= 150,000 THB:")
for loan in large_loans:
    print(f"  - {loan['borrower']}: {loan['amount']:,} THB")
```

## 📝 Part 4: Assignment

### Assignment: Loan Portfolio Manager
Create `assignment_portfolio.py` that:

1. Creates a list of 5 loans (use dictionaries)
2. Implements these functions:
   - `add_loan(loans, borrower, amount, rate)` - Add new loan
   - `get_loan(loans, loan_id)` - Find loan by ID
   - `calculate_portfolio_total(loans)` - Sum all amounts
   - `get_loans_by_status(loans, status)` - Filter by status
   - `display_portfolio(loans)` - Print formatted table

3. Demonstrates all functions with sample data

### Sample Output:
```
=== Loan Portfolio Manager ===

Portfolio Summary:
-------------------------------------------------
ID    Borrower      Amount        Rate    Status
-------------------------------------------------
1     Alice        100,000        7.5%    current
2     Bob          200,000        8.0%    current
3     Charlie       50,000        7.0%    paid
4     Diana        150,000        7.5%    late
5     Eve          300,000        6.5%    current
-------------------------------------------------
Total: 800,000 THB | Active: 4 | Paid: 1

Current Loans: 3 loans totaling 600,000 THB
```

## 📤 Submission
```bash
git add .
git commit -m "Lab 02: Python functions, loops, and data structures"
git push origin main
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Exercises 1-8 completed | 1.0% |
| Assignment functional | 0.5% |
| Code quality | 0.5% |

---
**Deadline:** Before Week 3 class
