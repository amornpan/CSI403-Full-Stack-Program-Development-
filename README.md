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
│                    CSI403 COURSE STRUCTURE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PHASE 1: LEARNING (Week 2-9)          PHASE 2: PROJECT (Week 10-15)│
│  ┌─────────────────────────┐           ┌─────────────────────────┐  │
│  │  📖 Lecture + Lab       │           │  💻 Project Development │  │
│  │  • สร้าง TaskFlow       │    ──▶    │  • Sprint-based Work    │  │
│  │  • ทุก Lab เก็บคะแนน    │           │  • Advisor Consultation │  │
│  │  • Hands-on Practice    │           │  • Real-world Product   │  │
│  └─────────────────────────┘           └─────────────────────────┘  │
│                                                                     │
│  Assessment: 64%                        Assessment: 36%             │
│  (8 Labs × 8%)                          (G1, G2, Checkpoint, Final) │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 🎯 Case Study: TaskFlow - Task Management System

นักศึกษาจะสร้างระบบ **TaskFlow** ตลอด 8 สัปดาห์ โดยเพิ่ม Features ทีละสัปดาห์

```
Week 2: 📁 โครงสร้างโปรเจค + Git
Week 3: 🚀 Task API (CRUD)
Week 4: 🗄️ Database + Users + Categories
Week 5: 🎨 หน้าเว็บ Static (HTML/CSS/JS)
Week 6: 🔗 Jinja2 + เชื่อมทุกอย่าง
Week 7: 🐳 Docker + Compose
Week 8: 🧪 Testing + Jenkins CI
Week 9: 🚀 Jenkins CD + Auto Deploy

ผลลัพธ์: ระบบ TaskFlow สมบูรณ์! 🎉
```

### TaskFlow Features
- ✅ User Registration & Authentication (Session-based)
- ✅ Task CRUD (Create, Read, Update, Delete)
- ✅ Category Management
- ✅ Task Status (Pending → In Progress → Done)
- ✅ Task Priority (Low, Medium, High)
- ✅ Due Date Tracking
- ✅ Search & Filter
- ✅ Dashboard with Statistics
- ✅ Dockerized Deployment
- ✅ Jenkins CI/CD Pipeline

## 🛠️ Technology Stack
| Layer | Technologies |
|-------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5, Jinja2 Templates |
| **Backend** | FastAPI, Python 3.11+, Pydantic |
| **Database** | Microsoft SQL Server (Docker), SQLAlchemy ORM |
| **Authentication** | Session-based, bcrypt |
| **DevOps** | Docker, Docker Compose, Jenkins CI/CD |
| **Testing** | pytest, pytest-cov |
| **Tools** | Git, GitHub, VS Code |

## 📁 Project Structure
```
CSI403-FullStack-Teaching/
├── 00-course-info/           # Syllabus, grading criteria
├── 01-starter-code/          # TaskFlow starter template
│   └── taskflow/
│       ├── app/
│       │   ├── main.py       # FastAPI application
│       │   ├── models.py     # SQLAlchemy models
│       │   ├── schemas.py    # Pydantic schemas
│       │   ├── database.py   # DB connection
│       │   ├── routes/       # API routes
│       │   ├── templates/    # Jinja2 templates
│       │   └── static/       # CSS, JS, images
│       ├── tests/            # pytest test files
│       ├── Dockerfile
│       ├── docker-compose.yml
│       ├── Jenkinsfile
│       └── requirements.txt
├── 02-templates/             # Document templates
├── 03-sample-data/           # Sample SQL scripts
├── 04-lab-exercises/         # Weekly lab instructions (8 Labs)
├── 05-quizzes/               # (Optional) Quiz materials
└── presentations/            # LaTeX slides
```

## 📅 Teaching Plan

### Phase 1: Learning Phase (Week 2-9) - สร้าง TaskFlow

| Week | Lecture Topic | Lab / Activity | Deliverable |
|:----:|---------------|----------------|-------------|
| **1** | **ปฐมนิเทศ** | - | - |
| **2** | **Git + Python + Setup** | Project Setup | **Lab 1 (8%)** |
| | • Git workflow (Branch, PR) | • สร้าง GitHub repo | |
| | • Python review | • โครงสร้างโปรเจค TaskFlow | |
| | • Project structure | • requirements.txt | |
| **3** | **FastAPI Fundamentals** | API Development | **Lab 2 (8%)** |
| | • REST API concepts | • Task API (CRUD) | |
| | • FastAPI basics | • Pydantic validation | |
| | • Pydantic schemas | • Swagger documentation | |
| **4** | **FastAPI + Database** | Database Integration | **Lab 3 (8%)** |
| | • MSSQL Docker | • SQLAlchemy models | |
| | • SQLAlchemy ORM | • User + Category + Task | |
| | • Relationships | • CRUD with database | |
| **5** | **Frontend Basics** | UI Development | **Lab 4 (8%)** |
| | • HTML/CSS review | • Static pages | |
| | • Bootstrap 5 | • Dashboard, Tasks, Categories | |
| | • JavaScript basics | • Forms + Modals | |
| **6** | **Jinja2 + Integration** | Full Stack | **Lab 5 (8%)** |
| | • Jinja2 templates | • เชื่อม Frontend + Backend | |
| | • Template inheritance | • Login/Logout | |
| | • Form handling | • CRUD ผ่านหน้าเว็บ | |
| **7** | **Docker + Compose** | Containerization | **Lab 6 (8%)** |
| | • Docker basics | • Dockerfile | |
| | • Dockerfile | • docker-compose.yml | |
| | • Docker Compose | • App + DB + Jenkins | |
| **8** | **Testing + Jenkins CI** | CI Pipeline | **Lab 7 (8%)** |
| | • pytest basics | • Test cases (≥8 tests) | |
| | • Jenkins setup | • Jenkinsfile (Test stage) | |
| | • CI concepts | • Auto test on push | |
| **9** | **Jenkins CD** | CD Pipeline | **Lab 8 (8%)** |
| | • CD concepts | • Build + Deploy stages | |
| | • Deployment | • Auto deploy to local | |
| | • Health checks | • Complete pipeline | |

### Phase 2: Project Phase (Week 10-15)

| Week | Sprint / Activity | Milestone | Deliverable |
|:----:|-------------------|-----------|-------------|
| **10** | **จัดทีม + G1: Proposal** | Project Kickoff | **G1 (5%)** |
| | • จัดกลุ่ม 4-5 คน | • SRS document | |
| | • เลือกโปรเจค | • User Stories | |
| **11** | **G2: System Design** | Design Complete | **G2 (5%)** |
| | • Architecture design | • ERD diagram | |
| | • Database design | • API design | |
| **12** | **Checkpoint Demo** | Prototype Ready | **Checkpoint (8%)** |
| | • Working prototype | • 50%+ features | |
| | • Demo to class | • Deployed | |
| **13** | **Development Sprint** | Core Features | Progress Check |
| | • Feature development | • CRUD complete | |
| | • อาจารย์ให้คำปรึกษา | • Testing | |
| **14** | **Development Sprint** | Testing & Polish | Progress Check |
| | • Bug fixes | • All features done | |
| | • Documentation | • Docker working | |
| **15** | **Final Presentation** | Complete System | **Final (12%)** |
| | • Project demo | • Live demo | |
| | • **Oral Defense (4%)** | • Code review | |
| | • **Peer Eval (2%)** | • Q&A session | |

## 📊 Assessment (100%)

### ไม่มีการสอบ - ประเมินจากผลงานและโปรเจค

| Component | Weight | Week | Description |
|-----------|:------:|:----:|-------------|
| **Phase 1: Learning** | **64%** | 2-9 | |
| Lab 1: Git + Python + Setup | 8% | 2 | Project structure, Git workflow |
| Lab 2: FastAPI CRUD | 8% | 3 | REST API, Pydantic |
| Lab 3: FastAPI + Database | 8% | 4 | SQLAlchemy, MSSQL |
| Lab 4: Frontend Basics | 8% | 5 | HTML/CSS/JS, Bootstrap |
| Lab 5: Jinja2 + Integration | 8% | 6 | Templates, Full stack |
| Lab 6: Docker + Compose | 8% | 7 | Containerization |
| Lab 7: Testing + Jenkins CI | 8% | 8 | pytest, CI pipeline |
| Lab 8: Jenkins CD | 8% | 9 | CD pipeline, Deployment |
| **Phase 2: Project** | **36%** | 10-15 | |
| G1: Project Proposal | 5% | 10 | SRS, User Stories |
| G2: System Design | 5% | 11 | Architecture, ERD, API |
| Checkpoint Demo | 8% | 12 | Working prototype |
| Final Project | 12% | 15 | Complete system |
| Oral Defense | 4% | 15 | Individual Q&A |
| Peer Evaluation | 2% | 15 | Team member rating |
| **Total** | **100%** | | |

## 🚀 Quick Start

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
cd 01-starter-code/taskflow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

### Docker Setup (Full Environment)
```bash
# Build and run with Docker Compose
docker-compose up -d

# Access:
# App: http://localhost:8000
# Swagger: http://localhost:8000/docs
# Jenkins: http://localhost:8080
```

## 📚 Lab Exercises

| Lab | Topic | Week | Weight |
|-----|-------|:----:|:------:|
| **Lab 1** | Git + Python + Setup | 2 | **8%** |
| **Lab 2** | FastAPI CRUD | 3 | **8%** |
| **Lab 3** | FastAPI + Database | 4 | **8%** |
| **Lab 4** | Frontend (HTML/CSS/JS) | 5 | **8%** |
| **Lab 5** | Jinja2 + Integration | 6 | **8%** |
| **Lab 6** | Docker + Compose | 7 | **8%** |
| **Lab 7** | Testing + Jenkins CI | 8 | **8%** |
| **Lab 8** | Jenkins CD | 9 | **8%** |

**หมายเหตุ:** ทุก Lab เก็บคะแนน รวม 64% ของคะแนนทั้งหมด

## 📧 Contact
- **Instructor:** อ.เมธัส คำจาด
- **Email:** methas@spuchonburi.ac.th
- **GitHub:** [CSI403-Full-Stack-Program-Development-](https://github.com/amornpan/CSI403-Full-Stack-Program-Development-)

---
**© 2026 มหาวิทยาลัยศรีปทุม วิทยาเขตชลบุรี - คณะเทคโนโลยีสารสนเทศ**
