# Lab 01: Python Basics & Environment Setup

**Week 1 | January 7-9, 2026 | 2%**

## 🎯 Objectives
By the end of this lab, you will be able to:
- Set up Python development environment
- Write and run Python scripts
- Use variables and data types
- Perform basic input/output operations
- Work with strings and numbers

## 📋 Prerequisites
- Python 3.11+ installed
- VS Code with Python extension
- Git installed

## 🔧 Part 1: Environment Setup (20 min)

### 1.1 Verify Python Installation
```bash
python --version    # Should show Python 3.11.x
pip --version       # Should show pip 23.x
git --version       # Should show git 2.x
```

### 1.2 Create Project Folder
```bash
mkdir csi403-labs
cd csi403-labs
mkdir lab01-python
cd lab01-python
code .  # Open VS Code
```

### 1.3 VS Code Extensions
Install these extensions:
- Python (Microsoft)
- Pylance
- Python Indent

## 💻 Part 2: Python Basics (40 min)

### Exercise 2.1: Hello World
Create `01_hello.py`:
```python
# CSI403 Lab 1 - Exercise 1
# My first Python program

print("Hello, World!")
print("Welcome to CSI403 Full Stack Development")
print("=" * 40)
```

Run: `python 01_hello.py`

### Exercise 2.2: Variables and Data Types
Create `02_variables.py`:
```python
# Variables and Data Types

# String
course_name = "CSI403"
instructor = "Aj. Methas"

# Integer
credits = 3
students = 45

# Float
project_weight = 40.0

# Boolean
is_required = True

# Print with f-string
print(f"Course: {course_name}")
print(f"Instructor: {instructor}")
print(f"Credits: {credits}")
print(f"Students: {students}")
print(f"Project Weight: {project_weight}%")
print(f"Required: {is_required}")

# Check types
print(f"\nType of course_name: {type(course_name)}")
print(f"Type of credits: {type(credits)}")
print(f"Type of project_weight: {type(project_weight)}")
print(f"Type of is_required: {type(is_required)}")
```

### Exercise 2.3: Basic Calculations
Create `03_calculations.py`:
```python
# Simple Loan Calculator

# Loan information
principal = 100000  # Loan amount in THB
annual_rate = 7.5   # Interest rate (%)
years = 3           # Loan term

# Calculate simple interest
interest = principal * (annual_rate / 100) * years
total = principal + interest
monthly = total / (years * 12)

# Display results
print("=" * 30)
print("   LOAN CALCULATOR")
print("=" * 30)
print(f"Principal: {principal:,.2f} THB")
print(f"Interest Rate: {annual_rate}%")
print(f"Term: {years} years")
print("-" * 30)
print(f"Total Interest: {interest:,.2f} THB")
print(f"Total Payment: {total:,.2f} THB")
print(f"Monthly Payment: {monthly:,.2f} THB")
```

### Exercise 2.4: User Input
Create `04_input.py`:
```python
# Getting User Input

print("=== Student Registration ===\n")

# String input
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")

# Numeric input (convert from string)
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

# Display
print("\n=== Registration Complete ===")
print(f"Name: {name}")
print(f"Student ID: {student_id}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")
```

### Exercise 2.5: String Operations
Create `05_strings.py`:
```python
# String Operations

name = "  John Smith  "

# String methods
print(f"Original: '{name}'")
print(f"Strip: '{name.strip()}'")
print(f"Upper: '{name.upper()}'")
print(f"Lower: '{name.lower()}'")
print(f"Title: '{name.title()}'")
print(f"Replace: '{name.replace('John', 'Jane')}'")

# String formatting
loan_prefix = "LN"
year = "26"
month = "01"
sequence = 42

loan_id = f"{loan_prefix}-{year}{month}-{sequence:05d}"
print(f"\nGenerated Loan ID: {loan_id}")

# String operations
text = "CSI403 Full Stack Development"
print(f"\nLength: {len(text)}")
print(f"Contains 'Stack': {'Stack' in text}")
print(f"Split: {text.split()}")
```

## 📝 Part 3: Assignment (30 min)

### Assignment: Enhanced Loan Calculator
Create `assignment_loan_calc.py` that:

1. Asks user for their name
2. Asks for loan amount (must be > 0)
3. Asks for annual interest rate
4. Asks for loan term in years
5. Calculates and displays:
   - Total interest
   - Total payment
   - Monthly payment
6. Generates a loan ID (format: LN-YYMM-XXXXX)

### Expected Output:
```
========================================
       LOAN CALCULATOR v1.0
========================================
Enter your name: John Doe
Enter loan amount (THB): 500000
Enter annual interest rate (%): 6.5
Enter loan term (years): 5

========================================
       LOAN SUMMARY
========================================
Loan ID: LN-2601-00001
Applicant: John Doe
----------------------------------------
Principal Amount: 500,000.00 THB
Interest Rate: 6.5%
Loan Term: 5 years (60 months)
----------------------------------------
Total Interest: 162,500.00 THB
Total Payment: 662,500.00 THB
Monthly Payment: 11,041.67 THB
========================================
```

## 📤 Submission

### Git Commands:
```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Lab 01: Python basics completed"

# Push to your team's repository
git push origin main
```

### Required Files:
- [ ] `01_hello.py`
- [ ] `02_variables.py`
- [ ] `03_calculations.py`
- [ ] `04_input.py`
- [ ] `05_strings.py`
- [ ] `assignment_loan_calc.py`

## ✅ Grading Criteria (2%)
| Criteria | Points |
|----------|--------|
| All exercises completed | 1.0% |
| Assignment works correctly | 0.5% |
| Clean code & comments | 0.5% |

## 📚 Resources
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [F-string Formatting](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

---
**Deadline:** Before next class (January 14, 2026)
