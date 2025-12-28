# Lab Exercises - CSI403 Full Stack Development

## 📋 Overview

รายวิชานี้ใช้การประเมินจาก **ผลงานและโปรเจค** (ไม่มีการสอบ)

## 🎯 Course Structure

### Two-Phase Learning Model

| Phase | Weeks | Focus | Assessment |
|-------|-------|-------|------------|
| **Phase 1: Learning** | 1-9 | เนื้อหา + Lab | 30% |
| **Phase 2: Project** | 10-15 | ทำโปรเจคจริง | 70% |

---

## 📅 Lab Schedule (Phase 1: Week 1-9)

| Week | Lab File | Topic | Type | Weight |
|:----:|----------|-------|:----:|:------:|
| 1 | `lab01-python-basics.md` | Python & Environment Setup | Practice | - |
| 2 | `lab02-project-planning.md` | Agile, Notion, User Stories | Practice | - |
| 3 | `lab03-html-css-bootstrap.md` | HTML, CSS, Bootstrap 5 | Practice | - |
| 4 | `lab04-jinja2-templates.md` | Jinja2 Template Engine | Practice | - |
| 5 | **`lab05-fastapi-crud.md`** | **FastAPI CRUD** | **Assessment** | **5%** |
| 6 | `lab06-sqlalchemy.md` | SQLAlchemy ORM | Practice | - |
| 7 | `lab07-integration.md` | Full Stack Integration | Practice | - |
| 8 | (ใช้เนื้อหาใน Lab 09) | Docker Basics | Practice | - |
| 9 | **`lab09-docker-jenkins.md`** | **Docker + Jenkins** | **Assessment** | **5%** |

---

## 📊 Assessment Summary (100%)

### Phase 1: Learning (30%)
| Assessment | Week | Weight |
|------------|:----:|:------:|
| G1: Project Proposal | 3 | 10% |
| Lab1: API Design | 5 | 5% |
| G2: System Design | 7 | 10% |
| Lab2: Docker + Pipeline | 9 | 5% |

### Phase 2: Project (70%)
| Assessment | Week | Weight |
|------------|:----:|:------:|
| Checkpoint Review | 12 | 10% |
| Test Document | 13 | 10% |
| **Final Project** | 15 | **50%** |

---

## 📁 Active Lab Files

### ✅ ไฟล์ที่ใช้ (9 ไฟล์)

```
04-lab-exercises/
├── README.md                    # ไฟล์นี้
├── lab01-python-basics.md       # Week 1
├── lab02-project-planning.md    # Week 2 ⭐ NEW
├── lab03-html-css-bootstrap.md  # Week 3
├── lab04-jinja2-templates.md    # Week 4
├── lab05-fastapi-crud.md        # Week 5 ⭐ ASSESSMENT LAB 1
├── lab06-sqlalchemy.md          # Week 6
├── lab07-integration.md         # Week 7 ⭐ NEW
└── lab09-docker-jenkins.md      # Week 9 ⭐ ASSESSMENT LAB 2
```

### ❌ ไฟล์เก่าที่ไม่ใช้แล้ว (ให้ลบ)

```
# ลบไฟล์เหล่านี้:
lab02-python-advanced.md         # รวมเข้า lab01 แล้ว
lab07-validation-business-logic.md  # เปลี่ยนเป็น integration
lab08-authentication.md          # รวมเข้า lab07 แล้ว
lab09-docker-basics.md           # รวมเข้า lab09-docker-jenkins แล้ว
lab10-docker-compose-jenkins.md  # รวมเข้า lab09-docker-jenkins แล้ว
lab11-pytest-testing.md          # ย้ายไป Phase 2
```

---

## 🎯 Learning Outcomes

เมื่อเรียนจบ Phase 1 นักศึกษาจะสามารถ:

1. ✅ ตั้งค่า Development Environment
2. ✅ วางแผนโปรเจคด้วย Agile/Scrum
3. ✅ สร้าง Frontend ด้วย HTML/CSS/Bootstrap
4. ✅ ใช้ Jinja2 Template Engine
5. ✅ พัฒนา REST API ด้วย FastAPI
6. ✅ ทำงานกับ Database ผ่าน SQLAlchemy
7. ✅ เชื่อมต่อ Frontend + Backend
8. ✅ สร้าง Docker Container
9. ✅ ตั้งค่า CI/CD Pipeline

---

## 📤 Submission Guidelines

### Practice Labs
- ไม่ต้องส่ง แต่ควรทำเพื่อฝึกทักษะ
- ใช้เป็นพื้นฐานสำหรับ Assessment Labs และ Project

### Assessment Labs (Lab1, Lab2)
- ส่งผ่าน GitHub Repository ของกลุ่ม
- ส่งก่อนเที่ยงคืนของวันที่กำหนด

```
group-repo/
├── lab1-api-design/         # Week 5
│   ├── app/
│   ├── requirements.txt
│   └── README.md
└── lab2-docker-pipeline/    # Week 9
    ├── Dockerfile
    ├── docker-compose.yml
    ├── Jenkinsfile
    └── README.md
```

### Group Assignments (G1, G2)
- G1: Project Proposal → Notion Workspace
- G2: System Design → Documentation + Diagrams

---

## 🗓️ Phase 2: Project (Week 10-15)

สัปดาห์ที่ 10-15 ไม่มี Lab ใหม่ - นักศึกษาทำโปรเจคกลุ่มโดยมีอาจารย์เป็นที่ปรึกษา

| Week | Sprint | Milestone |
|:----:|--------|-----------|
| 10 | Sprint 1 | Core Setup (DB + Auth) |
| 11 | Sprint 2 | Main Features (CRUD) |
| 12 | Sprint 3 | Integration |
| 13 | Sprint 4 | Testing |
| 14 | Sprint 5 | Deployment |
| 15 | Final | Presentation |

---

## ❓ FAQ

**Q: Assessment Lab ส่งเป็นกลุ่มหรือรายบุคคล?**

A: ส่งเป็นกลุ่ม (กลุ่มเดียวกับที่ทำ Project)

**Q: สามารถส่งงานช้าได้ไหม?**

A: หักคะแนน 10% ต่อวันที่ช้า (สูงสุด 3 วัน หลังจากนั้นไม่รับ)

**Q: ถ้าไม่ส่ง Practice Lab จะมีผลอะไรไหม?**

A: ไม่มีผลต่อคะแนนโดยตรง แต่จะทำ Assessment Lab และ Project ได้ยากขึ้น

---

**© 2026 CSI403 Full Stack Development - SPU Chonburi**
