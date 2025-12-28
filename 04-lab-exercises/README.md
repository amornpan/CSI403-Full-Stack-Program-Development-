# Lab Exercises - CSI403 Full Stack Development

## 📋 Overview

รายวิชานี้ใช้การประเมินจาก **ผลงานและโปรเจค** (ไม่มีการสอบ)

**ทุก Lab เก็บคะแนน!** รวม 64% ของคะแนนทั้งหมด

## 🎯 Course Structure

### Two-Phase Learning Model

| Phase | Weeks | Focus | Assessment |
|-------|-------|-------|------------|
| **Phase 1: Learning** | 2-9 | สร้าง TaskFlow | **64%** (8 Labs × 8%) |
| **Phase 2: Project** | 10-15 | Group Project | **36%** |

---

## 📅 Lab Schedule (Phase 1: Week 2-9)

| Week | Lab File | Topic | Weight |
|:----:|----------|-------|:------:|
| 2 | `lab01-git-python-setup.md` | Git + Python + Project Setup | **8%** |
| 3 | `lab02-fastapi-crud.md` | FastAPI Fundamentals | **8%** |
| 4 | `lab03-fastapi-database.md` | FastAPI + Database | **8%** |
| 5 | `lab04-frontend-basics.md` | Frontend (HTML/CSS/JS/Bootstrap) | **8%** |
| 6 | `lab05-jinja2-integration.md` | Jinja2 + Full Integration | **8%** |
| 7 | `lab06-docker-compose.md` | Docker + Docker Compose | **8%** |
| 8 | `lab07-testing-jenkins-ci.md` | Testing + Jenkins CI | **8%** |
| 9 | `lab08-jenkins-cd.md` | Jenkins CD + Deployment | **8%** |
| | | **Total** | **64%** |

---

## 🎯 Case Study: TaskFlow

นักศึกษาจะสร้างระบบ **TaskFlow - Task Management System** ตลอด 8 สัปดาห์

```
Week 2: 📁 โครงสร้างโปรเจค + Git repo
        └── ได้: taskflow/ folder structure

Week 3: 🚀 Task API (CRUD)
        └── ได้: 5 API endpoints (In-Memory)

Week 4: 🗄️ Database + Models
        └── ได้: MSSQL + User + Category + Task

Week 5: 🎨 หน้าเว็บ Static
        └── ได้: HTML/CSS/JS + Bootstrap pages

Week 6: 🔗 Jinja2 + เชื่อมทุกอย่าง
        └── ได้: Full Stack application

Week 7: 🐳 Docker + Compose
        └── ได้: docker-compose up ใช้งานได้

Week 8: 🧪 Testing + CI
        └── ได้: pytest + Jenkins auto test

Week 9: 🚀 CD + Deploy
        └── ได้: Complete CI/CD Pipeline

ผลลัพธ์: ระบบ TaskFlow สมบูรณ์! 🎉
```

---

## 📊 Assessment Summary (100%)

### Phase 1: Learning (64%)

| Lab | Topic | Week | Weight |
|-----|-------|:----:|:------:|
| Lab 1 | Git + Python + Setup | 2 | 8% |
| Lab 2 | FastAPI CRUD | 3 | 8% |
| Lab 3 | FastAPI + Database | 4 | 8% |
| Lab 4 | Frontend Basics | 5 | 8% |
| Lab 5 | Jinja2 + Integration | 6 | 8% |
| Lab 6 | Docker + Compose | 7 | 8% |
| Lab 7 | Testing + Jenkins CI | 8 | 8% |
| Lab 8 | Jenkins CD | 9 | 8% |
| **Total** | | | **64%** |

### Phase 2: Project (36%)

| Assessment | Week | Weight |
|------------|:----:|:------:|
| G1: Project Proposal | 10 | 5% |
| G2: System Design | 11 | 5% |
| Checkpoint Demo | 12 | 8% |
| Final Project | 15 | 12% |
| Oral Defense | 15 | 4% |
| Peer Evaluation | 15 | 2% |
| **Total** | | **36%** |

---

## 📁 Lab Files Structure

```
04-lab-exercises/
├── README.md                      # ไฟล์นี้
├── lab01-git-python-setup.md      # Week 2 - 8%
├── lab02-fastapi-crud.md          # Week 3 - 8%
├── lab03-fastapi-database.md      # Week 4 - 8%
├── lab04-frontend-basics.md       # Week 5 - 8%
├── lab05-jinja2-integration.md    # Week 6 - 8%
├── lab06-docker-compose.md        # Week 7 - 8%
├── lab07-testing-jenkins-ci.md    # Week 8 - 8%
└── lab08-jenkins-cd.md            # Week 9 - 8%
```

---

## 🎯 Learning Outcomes

เมื่อเรียนจบ Phase 1 (Week 2-9) นักศึกษาจะสามารถ:

1. ✅ ใช้ Git และ GitHub ได้อย่างคล่องแคล่ว
2. ✅ พัฒนา REST API ด้วย FastAPI
3. ✅ ทำงานกับ Database ผ่าน SQLAlchemy ORM
4. ✅ สร้าง Frontend ด้วย HTML/CSS/JS และ Bootstrap
5. ✅ ใช้ Jinja2 Template Engine
6. ✅ Containerize แอปพลิเคชันด้วย Docker
7. ✅ เขียน Unit Tests ด้วย pytest
8. ✅ ตั้งค่า CI/CD Pipeline ด้วย Jenkins

---

## 📤 Submission Guidelines

### ส่งงานอย่างไร

1. **ทุก Lab ส่งผ่าน GitHub Repository**
2. สร้าง Branch สำหรับแต่ละ Lab
3. ทำ Pull Request เมื่อเสร็จ
4. Merge to `main` branch

### Repository Structure

```
taskflow/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── templates/
│   └── static/
├── tests/
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

### Deadline

- **ส่งก่อนเที่ยงคืนวันอาทิตย์** ของสัปดาห์นั้น
- **Late Submission:** หัก 10% ต่อวัน (สูงสุด 3 วัน)
- หลังจาก 3 วัน = 0 คะแนน

---

## ✅ Grading Rubric (แต่ละ Lab)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| Functionality ทำงานได้ถูกต้อง | 4% |
| Code Quality สะอาด อ่านง่าย | 2% |
| Documentation (README, Comments) | 1% |
| Git Usage (Commits, Branches) | 1% |
| **รวม** | **8%** |

---

## ❓ FAQ

**Q: ส่งงานเป็นกลุ่มหรือรายบุคคล?**

A: **รายบุคคล** - ทุกคนต้องมี Repository ของตัวเอง

**Q: สามารถใช้ AI ช่วยเขียน Code ได้ไหม?**

A: ได้ แต่ต้องเข้าใจ Code ที่เขียน (อาจถูกถามใน Oral Defense)

**Q: ถ้าไม่ส่ง Lab บาง Lab จะเป็นอย่างไร?**

A: ได้ 0 คะแนนสำหรับ Lab นั้น (8% หายไป)

---

## 🗓️ Phase 2: Project (Week 10-15)

สัปดาห์ที่ 10-15 ไม่มี Lab ใหม่ - นักศึกษาทำ Group Project

| Week | กิจกรรม | Deliverable |
|:----:|---------|-------------|
| 10 | จัดทีม + G1 Proposal | G1 (5%) |
| 11 | G2 System Design | G2 (5%) |
| 12 | Checkpoint Demo | Checkpoint (8%) |
| 13 | Development Sprint | - |
| 14 | Development Sprint | - |
| 15 | Final Presentation | Final (12%) + Oral (4%) + Peer (2%) |

---

**© 2026 CSI403 Full Stack Development - SPU Chonburi**
