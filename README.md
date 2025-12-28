# CSI403 Full Stack Development - Teaching Materials

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/amornpan/CSI403-Full-Stack-Program-Development-)

## 📚 Course Information
| Item | Detail |
|------|--------|
| **Course Code** | CSI403 |
| **Course Name** | การพัฒนาโปรแกรมแบบ Full Stack (Software Full Stack Development) |
| **Credits** | 3 (2-3-5) |
| **Semester** | 2/2568 (Jan - Apr 2026) |
| **Instructor** | อ.เมธัส คำจาด |
| **University** | มหาวิทยาลัยศรีปทุม วิทยาเขตชลบุรี |

## 🎯 Course Structure

### Two-Phase Learning Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CSI403 COURSE STRUCTURE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PHASE 1: LEARNING (Week 1-9)          PHASE 2: PROJECT (Week 10-15)│
│  ┌─────────────────────────┐           ┌─────────────────────────┐  │
│  │  📖 Lecture + Lab       │           │  💻 Project Development │  │
│  │  • Content Delivery     │    ──▶    │  • Sprint-based Work    │  │
│  │  • Hands-on Practice    │           │  • Advisor Consultation │  │
│  │  • Skills Building      │           │  • Real-world Product   │  │
│  └─────────────────────────┘           └─────────────────────────┘  │
│                                                                     │
│  Assessment: 30%                        Assessment: 70%             │
│  (G1, Lab1, G2, Lab2)                   (Checkpoint, Test, Final)   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 🛠️ Technology Stack
| Layer | Technologies |
|-------|-------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, Jinja2 Templates |
| **Backend** | FastAPI, Python 3.11+, Pydantic |
| **Database** | Microsoft SQL Server, SQLAlchemy ORM |
| **Authentication** | Session-based, bcrypt, Role-based Access |
| **DevOps** | Docker, Docker Compose, Jenkins CI/CD |
| **Tools** | Git, GitHub, Notion, VS Code, pytest |

## 📁 Project Structure
```
CSI403-FullStack-Teaching/
├── 00-course-info/           # Syllabus, มคอ.3, grading
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
├── 05-quizzes/               # Quiz materials (optional)
└── presentations/            # [PRIVATE] LaTeX slides
```

## 📅 Teaching Plan

### Phase 1: Learning Phase (Week 1-9)

| Week | Lecture Topic | Lab / Activity | Deliverable |
|:----:|---------------|----------------|-------------|
| **1** | **Course Introduction** | Environment Setup | **จัดกลุ่ม** |
| | • Full Stack Overview | • Install Python, VS Code | (5-6 คน/กลุ่ม) |
| | • DevOps & CI/CD Concepts | • Git & GitHub Setup | |
| | • Technology Stack | • Python Basics Review | |
| **2** | **Project Planning** | Notion & Agile | - |
| | • Agile/Scrum Methodology | • Setup Notion Workspace | |
| | • SRS Document | • Create Kanban Board | |
| | • User Stories | • Write User Stories | |
| **3** | **Frontend: HTML/CSS** | Static UI Design | **G1: Project Proposal** |
| | • HTML5 Semantic Elements | • Build UI Mockup | (10%) |
| | • CSS3 & Flexbox | • Responsive Design | |
| | • Bootstrap 5 Components | • Form Design | |
| **4** | **Frontend: Jinja2** | Template Development | - |
| | • Template Syntax | • Create base.html | |
| | • Template Inheritance | • Build Page Templates | |
| | • Filters & Macros | • Dynamic Content | |
| **5** | **Backend: FastAPI** | API Development | **Lab1: API Design** |
| | • Routes & HTTP Methods | • CRUD Routes | (5%) |
| | • Path & Query Parameters | • Swagger Documentation | |
| | • Pydantic Validation | • Request Validation | |
| **6** | **Backend: Database** | ORM Implementation | - |
| | • SQLAlchemy ORM | • Create Models | |
| | • Models & Relationships | • Implement CRUD | |
| | • Database Design | • Connect to MSSQL | |
| **7** | **Full Stack Integration** | System Integration | **G2: System Design** |
| | • Frontend + Backend | • Connect Templates to API | (10%) |
| | • Session Authentication | • Login/Register Flow | |
| | • Form Handling | • Role-based Access | |
| **8** | **Docker Basics** | Containerization | - |
| | • Containers vs VMs | • Build Docker Image | |
| | • Dockerfile | • docker-compose.yml | |
| | • Docker Compose | • Multi-container Setup | |
| **9** | **CI/CD Pipeline** | Pipeline Setup | **Lab2: Docker + Pipeline** |
| | • Jenkins Introduction | • Setup Jenkins | (5%) |
| | • Pipeline Stages | • Create Jenkinsfile | |
| | • Automated Testing | • Configure Pipeline | |

### Phase 2: Project Phase (Week 10-15)

| Week | Sprint / Activity | Milestone | Deliverable |
|:----:|-------------------|-----------|-------------|
| **10** | **Sprint 1: Core Setup** | Foundation Ready | Progress Check |
| | • Project Kickoff | • Database Schema | |
| | • อาจารย์ให้คำปรึกษา | • User Authentication | |
| | | • Basic Project Structure | |
| **11** | **Sprint 2: Main Features** | Core Functions | Progress Check |
| | • CRUD Implementation | • Core CRUD Operations | |
| | • อาจารย์ให้คำปรึกษา | • Business Logic | |
| | | • Validation Rules | |
| **12** | **Sprint 3: Integration** | System Working | **Checkpoint Review** |
| | • Frontend + Backend | • Complete UI | (10%) |
| | • อาจารย์ให้คำปรึกษา | • API Integration | |
| | | • User Flows | |
| **13** | **Sprint 4: Testing** | Quality Assured | **Test Document** |
| | • Test Cases | • Test Matrix | (10%) |
| | • Bug Fixes | • Test Documentation | |
| | | • Bug Reports | |
| **14** | **Sprint 5: Deployment** | Deployment Ready | Final Preparation |
| | • Docker Deployment | • Docker Compose Working | |
| | • Demo Preparation | • CI/CD Pipeline | |
| | | • Presentation Ready | |
| **15** | **Final Presentation** | Complete System | **Final Project** |
| | • Project Demo | • Live Demo | (50%) |
| | • Q&A Session | • Technical Presentation | |
| | | • Code Review | |

## 📊 Assessment (100%)

### ไม่มีการสอบ - ประเมินจากผลงานและโปรเจค

| Component | Weight | Week | Description |
|-----------|:------:|:----:|-------------|
| **G1: Project Proposal** | 10% | 3 | SRS, User Stories, Project Plan |
| **Lab1: API Design** | 5% | 5 | FastAPI CRUD, Swagger Docs |
| **G2: System Design** | 10% | 7 | Architecture, Database Design, UI Mockup |
| **Lab2: Docker + Pipeline** | 5% | 9 | Dockerfile, docker-compose, Jenkinsfile |
| **Checkpoint Review** | 10% | 12 | Working Prototype Demo |
| **Test Document** | 10% | 13 | Test Cases, Test Matrix, Bug Reports |
| **Final Project** | **50%** | 15 | Complete System |
| └─ System Functionality | (25%) | | All features working |
| └─ Code Quality | (10%) | | Clean, documented code |
| └─ Documentation | (5%) | | User guide, README |
| └─ Presentation | (10%) | | Demo + Q&A |
| **Total** | **100%** | | |

## 🚀 Case Study: Loan Management System

### Features
- ✅ User Registration & Authentication
- ✅ Role-based Access Control (Admin/Borrower)
- ✅ Loan Application & Approval Workflow
- ✅ Payment Tracking & History
- ✅ Status Management
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
source venv/bin/activate  # Windows: venv\Scripts\activate

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
```

## 📚 Lab Exercises

| Lab | Topic | Week | Weight |
|-----|-------|:----:|:------:|
| Lab 1 | Python Basics & Environment Setup | 1 | - |
| Lab 2 | Project Planning & Notion | 2 | - |
| Lab 3 | HTML, CSS & Bootstrap | 3 | - |
| Lab 4 | Jinja2 Templates | 4 | - |
| **Lab 5** | **FastAPI CRUD (Lab1 Assessment)** | 5 | **5%** |
| Lab 6 | SQLAlchemy ORM | 6 | - |
| Lab 7 | Full Stack Integration | 7 | - |
| Lab 8 | Docker Basics | 8 | - |
| **Lab 9** | **Docker + Jenkins (Lab2 Assessment)** | 9 | **5%** |

## 📧 Contact
- **Instructor:** อ.เมธัส คำจาด
- **Email:** methas@spuchonburi.ac.th
- **GitHub:** [CSI403-Full-Stack-Program-Development-](https://github.com/amornpan/CSI403-Full-Stack-Program-Development-)

---
**© 2026 มหาวิทยาลัยศรีปทุม วิทยาเขตชลบุรี - คณะเทคโนโลยีสารสนเทศ**
