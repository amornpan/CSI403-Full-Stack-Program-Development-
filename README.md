# CSI403 Full Stack Development - Teaching Materials

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/amornpan/CSI403-Full-Stack-Program-Development-)

## 📚 Course Information
| Item | Detail |
|------|--------|
| **Course Code** | CSI403 |
| **Credits** | 3 (2-3-5) |
| **Semester** | 2/2568 (Jan - Apr 2026) |
| **Instructor** | Aj. Methas Khamjad |
| **University** | Sripatum University Chonburi |

## 🛠️ Technology Stack
| Layer | Technologies |
|-------|-------------|
| **Frontend** | Jinja2, HTML5, CSS3, Bootstrap 5 |
| **Backend** | FastAPI, Python 3.11+, Pydantic |
| **Database** | MSSQL Server (Docker), SQLAlchemy ORM |
| **Authentication** | Session-based, bcrypt, Role-based Access |
| **DevOps** | Docker, Docker Compose, Jenkins |
| **Tools** | GitHub, Notion, VS Code, pytest |

## 📁 Project Structure
```
CSI403-FullStack-Teaching/
├── 00-course-info/           # Syllabus, calendar, grading
├── 01-starter-code/          # Loan Management System
│   └── loan-management-system/
│       ├── app/
│       │   ├── main.py       # FastAPI application
│       │   ├── models.py     # SQLAlchemy models
│       │   ├── schemas.py    # Pydantic schemas
│       │   ├── database.py   # DB connection
│       │   └── templates/    # Jinja2 templates
│       ├── Dockerfile
│       ├── docker-compose.yml
│       ├── Jenkinsfile
│       └── requirements.txt
├── 02-templates/             # Document templates (SRS, Test)
├── 03-sample-data/           # Loan dataset & SQL scripts
├── 04-lab-exercises/         # Weekly lab instructions
├── 05-quizzes/               # Quiz materials
└── presentations/            # [PRIVATE] LaTeX slides
```

## 📅 Weekly Schedule (15 Weeks)

### Phase 1: Foundation & Planning (Weeks 1-3)
| Week | Date | Lecture Topic | Lab Topic | Assessment |
|------|------|---------------|-----------|------------|
| 1 | Jan 7-9 | Course Intro, Full Stack Overview | Python Basics, Environment Setup | Team Formation |
| 2 | Jan 14-16 | Project Planning, SRS, SDLC | Python Functions, Loops, Lists | - |
| 3 | Jan 21-23 | HTML5, CSS3, Bootstrap 5 | Build Static Loan Form | **G2 Present (5%)** |

### Phase 2: Architecture & Design (Weeks 4-6)
| Week | Date | Lecture Topic | Lab Topic | Assessment |
|------|------|---------------|-----------|------------|
| 4 | Jan 28-30 | Jinja2 Template Engine | Template Inheritance, Blocks | - |
| 5 | Feb 4-6 | FastAPI Introduction | Routes, Parameters, CRUD | **Lab1 Design (5%)** |
| 6 | Feb 11-13 | SQLAlchemy ORM, Database Design | Create Models, Relationships | - |

### Phase 3: Development & Authentication (Weeks 7-9)
| Week | Date | Lecture Topic | Lab Topic | Assessment |
|------|------|---------------|-----------|------------|
| 7 | Feb 18-20 | Pydantic Validation, Business Logic | Validation Rules, Error Handling | **G3 Present (5%)** |
| 8 | Feb 25-27 | Session-based Authentication | Login, Register, Protected Routes | - |
| 9 | Mar 4-6 | Full Stack Integration | Connect All Layers, CRUD Flow | **P1 (5%), Q1 (5%)** |

### Phase 4: Build & Containerization (Weeks 10-11)
| Week | Date | Lecture Topic | Lab Topic | Assessment |
|------|------|---------------|-----------|------------|
| 10 | Mar 11-13 | Docker Fundamentals | Dockerfile, Build Images | - |
| 11 | Mar 18-20 | Docker Compose, Jenkins CI/CD | Multi-container, Pipeline | **Q2 Quiz (5%)** |

### Phase 5: Testing & Documentation (Weeks 12-13)
| Week | Date | Lecture Topic | Lab Topic | Assessment |
|------|------|---------------|-----------|------------|
| 12 | Mar 25-27 | Testing Methods (Black/White/Gray) | pytest, Unit Tests | - |
| 13 | Apr 1-3 | Test Documentation, Bug Reporting | Test Matrix, Coverage | **P2 (5%)** |

### Phase 6: Presentation & Final (Weeks 14-15)
| Week | Date | Lecture Topic | Lab Topic | Assessment |
|------|------|---------------|-----------|------------|
| 14 | Apr 8-10 | Deployment, Demo Preparation | Final Integration | **Groups 1-3 Present** |
| - | Apr 13-15 | 🎉 **Songkran Holiday** | No Class | - |
| 15 | Apr 22-24 | Course Summary, Q&A | Final Submission | **Groups 4-6, Project (40%)** |

## 📊 Assessment Breakdown
| Component | Weight | Description |
|-----------|--------|-------------|
| **Project** | 40% | Loan Management System |
| **Exercises** | 20% | G2, Lab1, G3, P1, P2 (5% each) |
| **Quizzes** | 10% | Q1 CI/CD, Q2 Testing (5% each) |
| **Workpiece** | 10% | System Demo |
| **Attendance** | 10% | Class + Lab participation |
| **Presentation** | 10% | G2, G3 (5% each) |

## 🚀 Case Study: Loan Management System

### Features
- ✅ User Registration & Authentication
- ✅ Role-based Access Control (Admin/Borrower)
- ✅ Loan Application & Approval Workflow
- ✅ Payment Tracking & History
- ✅ Status Management (Current → Paid/Default)
- ✅ Dashboard & Reports
- ✅ Dockerized Deployment
- ✅ CI/CD Pipeline

### Database Schema
```
users (id, username, email, password_hash, role, is_active)
    │
    └──< borrowers (id, user_id, name, income, grade, ...)
            │
            └──< loans (id, borrower_id, amount, rate, status, ...)
                    │
                    └──< payments (id, loan_id, amount, date, ...)
```

## 🔧 Quick Start

### Prerequisites
- Python 3.11+
- Docker Desktop
- VS Code
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/amornpan/CSI403-Full-Stack-Program-Development-.git
cd CSI403-Full-Stack-Program-Development-

# Navigate to starter code
cd 01-starter-code/loan-management-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

### Docker Setup
```bash
# Build and run with Docker Compose
docker-compose up -d

# Access application
# Web: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Database Admin: http://localhost:8080
```

## 📧 Contact
- **Instructor:** Aj. Methas Khamjad
- **Email:** methas@spuchonburi.ac.th
- **GitHub:** [CSI403-Full-Stack-Program-Development-](https://github.com/amornpan/CSI403-Full-Stack-Program-Development-)

---
**© 2026 Sripatum University Chonburi - School of Information Technology**
