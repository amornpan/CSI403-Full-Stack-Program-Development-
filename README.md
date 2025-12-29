# CSI403 Full Stack Development

<div align="center">

![Course Banner](https://img.shields.io/badge/CSI403-Full%20Stack%20Development-maroon?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&amp;logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green?style=flat-square&amp;logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=flat-square&amp;logo=docker)

**"Learn by Doing, Score by Completing"**

*เรียนจบคาบ = งานเสร็จ = ได้คะแนน = ไม่มีการบ้าน!*

</div>

---

## 📑 Table of Contents

- [Course Overview](#-course-overview)
- [Class Structure](#-class-structure)
- [Assessment](#-assessment)
- [Setup Guides](#-setup-guides)
- [Lab Workshops](#-lab-workshops)
- [Extended Learning](#-extended-learning)
- [Course Schedule](#-course-schedule)

---

## 🎯 Course Overview

### Philosophy

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   📖 Lecture (ทฤษฎี)          →  เข้าใจ Concept             │
│   💻 Lab Workshop (ปฏิบัติ)   →  ลงมือทำ + เก็บคะแนน        │
│                                                             │
│   ❌ NO Homework    ❌ NO Midterm    ❌ NO Final Exam       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### What You'll Build: TaskFlow

Task Management System ที่มีฟีเจอร์:

- ✅ User Registration &amp; Login
- ✅ Create, Read, Update, Delete Tasks
- ✅ Categories &amp; Priorities
- ✅ Dashboard with Statistics
- ✅ Docker Deployment
- ✅ CI/CD Pipeline with Jenkins

### Technology Stack

| Layer | Technologies |
|-------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5, Jinja2 |
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy, Pydantic |
| **Database** | Microsoft SQL Server |
| **DevOps** | Docker, Docker Compose, Jenkins, Git |
| **Testing** | pytest, pytest-cov |

---

## 🏫 Class Structure

### คาบทฤษฎี (Lecture)
- 2 กลุ่ม × 2 คาบ/สัปดาห์
- สอน Concept, Demo ตัวอย่าง

### คาบปฏิบัติ (Lab Workshop)
- 4 กลุ่ม × 3 คาบ/สัปดาห์
- Hands-on + เก็บคะแนน

**Timeline ต่อคาบ Lab (2.5 ชม.):**

```
┌─────────────────────────────────────────────────────────────┐
│  ⏰ 15 min   │  📖 Quick Review                             │
├──────────────┼──────────────────────────────────────────────┤
│  ⏰ 30 min   │  💻 Checkpoint 1 (2%)                        │
├──────────────┼──────────────────────────────────────────────┤
│  ⏰ 30 min   │  💻 Checkpoint 2 (2%)                        │
├──────────────┼──────────────────────────────────────────────┤
│  ⏰ 30 min   │  💻 Checkpoint 3 (2%)                        │
├──────────────┼──────────────────────────────────────────────┤
│  ⏰ 30 min   │  💻 Checkpoint 4 (2%)                        │
├──────────────┼──────────────────────────────────────────────┤
│  ⏰ 15 min   │  ✅ Wrap-up &amp; Scoring                        │
└─────────────────────────────────────────────────────────────┘
                      Total: 8% per Lab
```

---

## 📊 Assessment

### Phase 1: Weekly Labs (64%)

| Week | Lab | Score |
|:----:|-----|:-----:|
| 1 | 🚀 Setup &amp; First API | 8% |
| 2 | 📝 CRUD Operations | 8% |
| 3 | 🗄️ Database Integration | 8% |
| 4 | 🎨 Frontend Basics | 8% |
| 5 | 🔗 Full Integration | 8% |
| 6 | 🐳 Docker Deployment | 8% |
| 7 | 🧪 Testing &amp; CI | 8% |
| 8 | 🚀 CD &amp; Go Live | 8% |

### Phase 2: Group Project (36%)

| Week | Deliverable | Score |
|:----:|-------------|:-----:|
| 10 | G1: Project Proposal | 5% |
| 11 | G2: System Design | 5% |
| 12 | Checkpoint Demo | 8% |
| 15 | Final Presentation | 12% |
| 15 | Oral Defense | 4% |
| 15 | Peer Evaluation | 2% |

### Scoring per Checkpoint

| Status | Score |
|--------|:-----:|
| ✅ Complete | 100% |
| 🔶 Partial | 50% |
| ❌ Incomplete | 0% |

### Late Policy

| Submission | Deduction |
|------------|:---------:|
| ภายในคาบ Lab | 0% |
| ภายใน 24 ชม. | 0% |
| 24-48 ชม. | -50% |
| หลัง 48 ชม. | ไม่รับ |

---

## 🛠️ Setup Guides

**⭐ ทำก่อนเรียน Week 1!**

| # | Guide | เวลา |
|:-:|-------|:----:|
| 1 | [Git &amp; GitHub](./docs/setup/01-git-github.md) | 30 min |
| 2 | [Miniconda &amp; Python](./docs/setup/02-miniconda-python.md) | 20 min |
| 3 | [Docker](./docs/setup/03-docker.md) | 30 min |
| 4 | [VS Code](./docs/setup/04-vscode.md) | 15 min |

### Quick Verification

```bash
git --version          # git version 2.x.x
conda --version        # conda 23.x.x
python --version       # Python 3.11.x
docker --version       # Docker version 24.x.x
code --version         # 1.x.x
```

---

## 💻 Lab Workshops

| Week | Workshop | Guide | Checklist |
|:----:|----------|:-----:|:---------:|
| 1 | Setup &amp; First API | [📖](./workshops/week01-setup/README.md) | [✅](./workshops/week01-setup/CHECKLIST.md) |
| 2 | CRUD Operations | [📖](./workshops/week02-crud/README.md) | [✅](./workshops/week02-crud/CHECKLIST.md) |
| 3 | Database Integration | [📖](./workshops/week03-database/README.md) | [✅](./workshops/week03-database/CHECKLIST.md) |
| 4 | Frontend Basics | [📖](./workshops/week04-frontend/README.md) | [✅](./workshops/week04-frontend/CHECKLIST.md) |
| 5 | Full Integration | [📖](./workshops/week05-integration/README.md) | [✅](./workshops/week05-integration/CHECKLIST.md) |
| 6 | Docker Deployment | [📖](./workshops/week06-docker/README.md) | [✅](./workshops/week06-docker/CHECKLIST.md) |
| 7 | Testing &amp; CI | [📖](./workshops/week07-testing/README.md) | [✅](./workshops/week07-testing/CHECKLIST.md) |
| 8 | CD &amp; Go Live | [📖](./workshops/week08-cicd/README.md) | [✅](./workshops/week08-cicd/CHECKLIST.md) |

---

## 📖 Extended Learning

*เนื้อหาเสริมสำหรับผู้สนใจ (Optional)*

| Week | Topic | Link |
|:----:|-------|:----:|
| 1 | Git Advanced | [📖](./docs/extended/week01-git-advanced.md) |
| 2 | REST Best Practices | [📖](./docs/extended/week02-rest-best-practices.md) |
| 3 | Database Design | [📖](./docs/extended/week03-database-design.md) |
| 4 | CSS &amp; Responsive | [📖](./docs/extended/week04-css-responsive.md) |
| 5 | Security | [📖](./docs/extended/week05-security.md) |
| 6 | Docker Production | [📖](./docs/extended/week06-docker-production.md) |
| 7 | Testing Strategies | [📖](./docs/extended/week07-testing-strategies.md) |
| 8 | DevOps | [📖](./docs/extended/week08-devops.md) |

---

## 🗓️ Course Schedule

### Phase 1: Learning (Week 1-8)

| Week | Lecture | Lab |
|:----:|---------|-----|
| 1 | Course Intro + Git + Python | 🚀 Setup &amp; First API |
| 2 | REST API + FastAPI | 📝 CRUD Operations |
| 3 | Database + SQLAlchemy | 🗄️ Database Integration |
| 4 | HTML + CSS + Bootstrap | 🎨 Frontend Basics |
| 5 | Jinja2 + Session Auth | 🔗 Full Integration |
| 6 | Docker + Compose | 🐳 Docker Deployment |
| 7 | Testing + pytest | 🧪 Testing &amp; CI |
| 8 | CI/CD + Jenkins | 🚀 CD &amp; Go Live |

### Phase 2: Project (Week 9-15)

| Week | Activity | Deliverable |
|:----:|----------|-------------|
| 9 | Review + Team Formation | - |
| 10 | Project Planning | G1: Proposal (5%) |
| 11 | System Design | G2: Design (5%) |
| 12 | Sprint 1 | Checkpoint (8%) |
| 13 | Sprint 2 | - |
| 14 | Sprint 3 | - |
| 15 | Final | Presentation (18%) |

---

## 📂 Repository Structure

```
CSI403-FullStack-Teaching/
│
├── README.md                    # 👈 You are here!
│
├── docs/
│   ├── setup/                   # Installation Guides
│   │   ├── 01-git-github.md
│   │   ├── 02-miniconda-python.md
│   │   ├── 03-docker.md
│   │   └── 04-vscode.md
│   └── extended/                # Extended Learning
│
├── workshops/                   # Lab Materials
│   ├── week01-setup/
│   │   ├── README.md           # Workshop Guide
│   │   ├── CHECKLIST.md        # Scoring Checklist
│   │   └── solution/           # Reference Code
│   └── ...
│
└── scoring/                     # TA Scoring Tools
```

---

## 🆘 Getting Help

- ✋ ยกมือเรียก TA ในคาบ Lab
- 📝 เปิด GitHub Issue

---

<div align="center">

**Ready to start? 🚀**

[📖 Start with Git Setup →](./docs/setup/01-git-github.md)

</div>
