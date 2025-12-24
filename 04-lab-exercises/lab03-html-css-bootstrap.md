# Lab 03: HTML, CSS & Bootstrap 5

**Week 3 | January 21-23, 2026 | 2%**

## 🎯 Objectives
- Create HTML page structure
- Apply CSS styling
- Use Bootstrap 5 components
- Build responsive layouts

## 📋 Prerequisites
- VS Code with Live Server extension
- Basic understanding of web browsers

## 💻 Part 1: HTML Basics (30 min)

### Exercise 1.1: HTML Structure
Create folder `lab03-html/` and file `01_structure.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Management System</title>
</head>
<body>
    <header>
        <h1>Loan Management System</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/loans">Loans</a>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        <section id="hero">
            <h2>Welcome to Our Lending Platform</h2>
            <p>Get the loan you need with competitive rates.</p>
        </section>
        
        <section id="features">
            <h2>Our Services</h2>
            <article>
                <h3>Personal Loans</h3>
                <p>Up to 1,000,000 THB with flexible terms.</p>
            </article>
            <article>
                <h3>Business Loans</h3>
                <p>Grow your business with our financing options.</p>
            </article>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 CSI403 Full Stack Development</p>
    </footer>
</body>
</html>
```

### Exercise 1.2: HTML Forms
Create `02_form.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Application Form</title>
</head>
<body>
    <h1>Loan Application</h1>
    
    <form action="/apply" method="POST">
        <!-- Personal Information -->
        <fieldset>
            <legend>Personal Information</legend>
            
            <div>
                <label for="fullname">Full Name:</label>
                <input type="text" id="fullname" name="fullname" required>
            </div>
            
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div>
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone" pattern="[0-9]{10}">
            </div>
            
            <div>
                <label for="dob">Date of Birth:</label>
                <input type="date" id="dob" name="dob">
            </div>
        </fieldset>
        
        <!-- Loan Details -->
        <fieldset>
            <legend>Loan Details</legend>
            
            <div>
                <label for="amount">Loan Amount (THB):</label>
                <input type="number" id="amount" name="amount" 
                       min="10000" max="1000000" step="1000" required>
            </div>
            
            <div>
                <label for="term">Loan Term:</label>
                <select id="term" name="term" required>
                    <option value="">Select term...</option>
                    <option value="12">12 months</option>
                    <option value="24">24 months</option>
                    <option value="36">36 months</option>
                    <option value="48">48 months</option>
                    <option value="60">60 months</option>
                </select>
            </div>
            
            <div>
                <label for="purpose">Purpose:</label>
                <select id="purpose" name="purpose">
                    <option value="personal">Personal</option>
                    <option value="education">Education</option>
                    <option value="home">Home Improvement</option>
                    <option value="business">Business</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <div>
                <label for="description">Additional Information:</label>
                <textarea id="description" name="description" rows="4"></textarea>
            </div>
        </fieldset>
        
        <!-- Agreement -->
        <fieldset>
            <legend>Agreement</legend>
            
            <div>
                <input type="checkbox" id="agree" name="agree" required>
                <label for="agree">I agree to the terms and conditions</label>
            </div>
            
            <div>
                <input type="checkbox" id="newsletter" name="newsletter">
                <label for="newsletter">Subscribe to newsletter</label>
            </div>
        </fieldset>
        
        <div>
            <button type="submit">Submit Application</button>
            <button type="reset">Clear Form</button>
        </div>
    </form>
</body>
</html>
```

### Exercise 1.3: HTML Tables
Create `03_table.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan List</title>
</head>
<body>
    <h1>My Loans</h1>
    
    <table border="1">
        <thead>
            <tr>
                <th>Loan ID</th>
                <th>Amount</th>
                <th>Term</th>
                <th>Rate</th>
                <th>Monthly Payment</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>LN-2601-00001</td>
                <td>100,000 THB</td>
                <td>36 months</td>
                <td>7.5%</td>
                <td>3,111 THB</td>
                <td>Current</td>
                <td>
                    <a href="/loans/1">View</a>
                    <a href="/loans/1/pay">Pay</a>
                </td>
            </tr>
            <tr>
                <td>LN-2601-00002</td>
                <td>50,000 THB</td>
                <td>24 months</td>
                <td>7.0%</td>
                <td>2,229 THB</td>
                <td>Paid</td>
                <td>
                    <a href="/loans/2">View</a>
                </td>
            </tr>
            <tr>
                <td>LN-2601-00003</td>
                <td>200,000 THB</td>
                <td>60 months</td>
                <td>8.0%</td>
                <td>4,055 THB</td>
                <td>Current</td>
                <td>
                    <a href="/loans/3">View</a>
                    <a href="/loans/3/pay">Pay</a>
                </td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <th colspan="4">Total Outstanding</th>
                <th colspan="3">300,000 THB</th>
            </tr>
        </tfoot>
    </table>
</body>
</html>
```

## 💻 Part 2: CSS Styling (30 min)

### Exercise 2.1: Basic CSS
Create `04_styled.html` and `style.css`:

**style.css:**
```css
/* CSS Variables */
:root {
    --primary-color: #800000;
    --secondary-color: #d4af37;
    --text-color: #333;
    --bg-color: #f5f5f5;
    --white: #ffffff;
}

/* Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
}

/* Header */
header {
    background-color: var(--primary-color);
    color: var(--white);
    padding: 1rem 2rem;
}

header h1 {
    margin-bottom: 0.5rem;
}

nav a {
    color: var(--white);
    text-decoration: none;
    margin-right: 1rem;
    padding: 0.5rem;
}

nav a:hover {
    background-color: var(--secondary-color);
    border-radius: 4px;
}

/* Main Content */
main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

section {
    background: var(--white);
    padding: 2rem;
    margin-bottom: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

h2 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    border-bottom: 2px solid var(--secondary-color);
    padding-bottom: 0.5rem;
}

/* Forms */
form {
    max-width: 600px;
}

fieldset {
    border: 1px solid #ddd;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 4px;
}

legend {
    color: var(--primary-color);
    font-weight: bold;
    padding: 0 0.5rem;
}

label {
    display: block;
    margin-bottom: 0.25rem;
    font-weight: 500;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="number"],
input[type="date"],
select,
textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

input:focus,
select:focus,
textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 2px rgba(128, 0, 0, 0.1);
}

button {
    background-color: var(--primary-color);
    color: var(--white);
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    margin-right: 0.5rem;
}

button:hover {
    background-color: #600000;
}

button[type="reset"] {
    background-color: #6c757d;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: var(--primary-color);
    color: var(--white);
}

tr:hover {
    background-color: #f5f5f5;
}

/* Footer */
footer {
    background-color: var(--primary-color);
    color: var(--white);
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
}
```

## 💻 Part 3: Bootstrap 5 (40 min)

### Exercise 3.1: Bootstrap Setup
Create `05_bootstrap.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan System - Bootstrap</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="bi bi-bank2"></i> Loan System
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Loans</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Apply</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="#"><i class="bi bi-box-arrow-in-right"></i> Login</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    
    <!-- Hero Section -->
    <section class="bg-primary text-white py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <h1 class="display-4 fw-bold">Get Your Loan Today</h1>
                    <p class="lead">Fast approval, competitive rates, flexible terms.</p>
                    <a href="#apply" class="btn btn-warning btn-lg">Apply Now</a>
                </div>
                <div class="col-lg-6">
                    <img src="https://via.placeholder.com/500x300" class="img-fluid rounded" alt="Loan">
                </div>
            </div>
        </div>
    </section>
    
    <!-- Features -->
    <section class="py-5">
        <div class="container">
            <h2 class="text-center mb-4">Why Choose Us?</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card h-100 text-center">
                        <div class="card-body">
                            <i class="bi bi-lightning-charge text-primary" style="font-size: 3rem;"></i>
                            <h5 class="card-title mt-3">Fast Approval</h5>
                            <p class="card-text">Get approved within 24 hours.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100 text-center">
                        <div class="card-body">
                            <i class="bi bi-percent text-success" style="font-size: 3rem;"></i>
                            <h5 class="card-title mt-3">Low Rates</h5>
                            <p class="card-text">Starting from 6.5% per year.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100 text-center">
                        <div class="card-body">
                            <i class="bi bi-calendar-check text-warning" style="font-size: 3rem;"></i>
                            <h5 class="card-title mt-3">Flexible Terms</h5>
                            <p class="card-text">12 to 60 months repayment.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Loan Calculator Card -->
    <section class="bg-light py-5" id="apply">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-6">
                    <div class="card shadow">
                        <div class="card-header bg-primary text-white">
                            <h4 class="mb-0"><i class="bi bi-calculator"></i> Loan Calculator</h4>
                        </div>
                        <div class="card-body">
                            <form>
                                <div class="mb-3">
                                    <label for="calcAmount" class="form-label">Loan Amount (THB)</label>
                                    <input type="number" class="form-control" id="calcAmount" 
                                           placeholder="100,000" min="10000" max="1000000">
                                </div>
                                <div class="mb-3">
                                    <label for="calcTerm" class="form-label">Term (months)</label>
                                    <select class="form-select" id="calcTerm">
                                        <option value="12">12 months</option>
                                        <option value="24">24 months</option>
                                        <option value="36" selected>36 months</option>
                                        <option value="48">48 months</option>
                                        <option value="60">60 months</option>
                                    </select>
                                </div>
                                <div class="mb-3">
                                    <label for="calcRate" class="form-label">Interest Rate: <span id="rateValue">7.5</span>%</label>
                                    <input type="range" class="form-range" id="calcRate" 
                                           min="5" max="15" step="0.5" value="7.5">
                                </div>
                                <button type="button" class="btn btn-primary w-100">Calculate</button>
                            </form>
                            
                            <hr>
                            
                            <div class="text-center">
                                <p class="mb-1">Estimated Monthly Payment</p>
                                <h2 class="text-primary">3,111 THB</h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Footer -->
    <footer class="bg-dark text-white py-4">
        <div class="container text-center">
            <p class="mb-0">&copy; 2026 CSI403 Full Stack Development - SPU Chonburi</p>
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Update rate display
        document.getElementById('calcRate').addEventListener('input', function() {
            document.getElementById('rateValue').textContent = this.value;
        });
    </script>
</body>
</html>
```

### Exercise 3.2: Bootstrap Form
Create `06_bootstrap_form.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Loan System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        body {
            background: linear-gradient(135deg, #800000 0%, #400000 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <div class="card shadow-lg">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <i class="bi bi-bank2 text-primary" style="font-size: 3rem;"></i>
                            <h3 class="mt-2">Loan System</h3>
                            <p class="text-muted">Sign in to your account</p>
                        </div>
                        
                        <form>
                            <div class="mb-3">
                                <label for="email" class="form-label">Email address</label>
                                <div class="input-group">
                                    <span class="input-group-text"><i class="bi bi-envelope"></i></span>
                                    <input type="email" class="form-control" id="email" 
                                           placeholder="you@example.com" required>
                                </div>
                            </div>
                            
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <div class="input-group">
                                    <span class="input-group-text"><i class="bi bi-lock"></i></span>
                                    <input type="password" class="form-control" id="password" 
                                           placeholder="••••••••" required>
                                </div>
                            </div>
                            
                            <div class="d-flex justify-content-between mb-3">
                                <div class="form-check">
                                    <input type="checkbox" class="form-check-input" id="remember">
                                    <label class="form-check-label" for="remember">Remember me</label>
                                </div>
                                <a href="#" class="text-decoration-none">Forgot password?</a>
                            </div>
                            
                            <button type="submit" class="btn btn-primary w-100 mb-3">
                                <i class="bi bi-box-arrow-in-right"></i> Sign In
                            </button>
                            
                            <div class="text-center">
                                <span class="text-muted">Don't have an account?</span>
                                <a href="#" class="text-decoration-none">Register</a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

## 📝 Assignment: Complete Loan Application Page

Create a complete loan application page with:
1. Responsive navbar
2. Application form with validation
3. Loan calculator sidebar
4. Footer with links

### Requirements:
- Use Bootstrap 5
- Fully responsive (mobile-friendly)
- Include at least 10 form fields
- Use cards, grid system, and components

## 📤 Submission
```bash
git add .
git commit -m "Lab 03: HTML, CSS, Bootstrap"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| HTML exercises | 0.5% |
| CSS styling | 0.5% |
| Bootstrap page | 0.5% |
| Assignment | 0.5% |

---
**Deadline:** Before Week 4 class
