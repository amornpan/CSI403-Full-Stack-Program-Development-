# CSI403 Full Stack Development

## 🎯 Course Philosophy

> **"Learn by Doing, Score by Completing"**
> 
> เรียนจบคาบ = งานเสร็จ = ได้คะแนน = ไม่มีการบ้าน!

คอร์สนี้ออกแบบมาให้:
- ✅ **ทำตามได้ทันที** - มี step-by-step ให้ทำระหว่างเรียน
- ✅ **เก็บคะแนนในคาบ** - ไม่มีการบ้านกลับบ้าน
- ✅ **เหมาะกับทุกคน** - นักศึกษาหรือคนทั่วไปก็เรียนได้
- ✅ **มี Extended Content** - อยากรู้เพิ่มก็ศึกษาต่อได้

---

## 📋 Course Information

| รายละเอียด | ข้อมูล |
|------------|--------|
| รหัสวิชา | CSI403 |
| ชื่อวิชา | Full Stack Development |
| หน่วยกิต | 3 (2-3-5) |
| ภาคการศึกษา | 1/2569 |
| รูปแบบ | Hands-on Workshop |

---

## 📊 Assessment (100%)

### ไม่มี Midterm / Final / การบ้าน!

| ส่วน | คะแนน | รายละเอียด |
|------|:-----:|------------|
| **Weekly Workshops** | 64% | 8 สัปดาห์ × 8% (ทำในคาบ) |
| **Group Project** | 36% | สร้างโปรเจคของตัวเอง |

---

## 🗓️ Weekly Workshop Structure

แต่ละสัปดาห์ใช้เวลา **3 ชั่วโมง** แบ่งเป็น:

```
┌─────────────────────────────────────────────────────────────┐
│  ⏰ 30 นาที    │  📖 Mini Lecture                           │
│               │  - สอนแนวคิดสั้นๆ กระชับ                    │
│               │  - ดู Demo ตัวอย่าง                         │
├───────────────┼─────────────────────────────────────────────┤
│  ⏰ 2 ชั่วโมง  │  💻 Hands-on Workshop                      │
│               │  - ทำตาม Step-by-step Guide                │
│               │  - ถามได้ตลอด มี TA ช่วย                    │
│               │  - Checkpoint ทุก 30 นาที                   │
├───────────────┼─────────────────────────────────────────────┤
│  ⏰ 30 นาที    │  ✅ Wrap-up & Scoring                      │
│               │  - ตรวจงาน เก็บคะแนน                        │
│               │  - Q&A สรุปสิ่งที่เรียน                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📅 Course Schedule

### Phase 1: Weekly Workshops (Week 1-9)

| Week | Workshop | คะแนน | สิ่งที่ได้ |
|:----:|----------|:-----:|-----------|
| 1 | 🚀 Setup & First API | 8% | โปรเจค + API แรก |
| 2 | 📝 CRUD Operations | 8% | Task API ครบ 5 endpoints |
| 3 | 🗄️ Database Connection | 8% | เชื่อมต่อ MSSQL |
| 4 | 🎨 Frontend Basics | 8% | หน้าเว็บ + Bootstrap |
| 5 | 🔗 Full Integration | 8% | Frontend + Backend |
| 6 | 🐳 Docker Deploy | 8% | Container + Compose |
| 7 | 🧪 Testing & CI | 8% | Tests + Jenkins |
| 8 | 🚀 CD & Go Live | 8% | Deploy อัตโนมัติ |

### Phase 2: Group Project (Week 9-15)

| Week | Activity | คะแนน |
|:----:|----------|:-----:|
| 9 | Team Formation + Idea | - |
| 10 | G1: Proposal | 5% |
| 11 | G2: Design + Sprint 1 | 5% |
| 12 | Checkpoint Demo | 8% |
| 13-14 | Development | - |
| 15 | Final Presentation | 18% |

---

## 📚 Workshop Details

### Week 1: 🚀 Setup & First API

**เป้าหมาย:** ติดตั้งเครื่องมือ + สร้าง API แรก

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | ติดตั้ง Python, Git, VS Code, Docker | 2% |
| CP2 | 30m | สร้าง GitHub repo + Clone | 2% |
| CP3 | 30m | สร้างโปรเจค + Virtual Environment | 2% |
| CP4 | 30m | สร้าง FastAPI Hello World | 2% |

**ผลลัพธ์:** `http://localhost:8000` ทำงานได้!

📖 [Extended: Git Advanced](./docs/extended/week01-git-advanced.md)

---

### Week 2: 📝 CRUD Operations

**เป้าหมาย:** สร้าง Task API ครบ 5 operations

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | สร้าง Pydantic Schemas | 2% |
| CP2 | 30m | POST /tasks (Create) | 2% |
| CP3 | 30m | GET /tasks, GET /tasks/{id} | 2% |
| CP4 | 30m | PUT + DELETE | 2% |

**ผลลัพธ์:** Swagger UI ทดสอบได้ครบทุก endpoint!

📖 [Extended: REST Best Practices](./docs/extended/week02-rest-best-practices.md)

---

### Week 3: 🗄️ Database Connection

**เป้าหมาย:** เชื่อมต่อ MSSQL + สร้าง Models

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | Run MSSQL Container | 2% |
| CP2 | 30m | SQLAlchemy Setup | 2% |
| CP3 | 30m | Create Task Model | 2% |
| CP4 | 30m | Update API to use DB | 2% |

**ผลลัพธ์:** Data บันทึกลง Database จริง!

📖 [Extended: Database Design](./docs/extended/week03-database-design.md)

---

### Week 4: 🎨 Frontend Basics

**เป้าหมาย:** สร้างหน้าเว็บด้วย HTML + Bootstrap

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | HTML Structure + Bootstrap | 2% |
| CP2 | 30m | Task List UI | 2% |
| CP3 | 30m | Create Task Form | 2% |
| CP4 | 30m | JavaScript + Fetch API | 2% |

**ผลลัพธ์:** หน้าเว็บสวยงาม ใช้งานได้!

📖 [Extended: CSS & Responsive](./docs/extended/week04-css-responsive.md)

---

### Week 5: 🔗 Full Integration

**เป้าหมาย:** รวม Frontend + Backend + Auth

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | Jinja2 Templates Setup | 2% |
| CP2 | 30m | Login/Register Pages | 2% |
| CP3 | 30m | Session Authentication | 2% |
| CP4 | 30m | Protected Routes | 2% |

**ผลลัพธ์:** Web App ที่ Login ได้!

📖 [Extended: Security Best Practices](./docs/extended/week05-security.md)

---

### Week 6: 🐳 Docker Deploy

**เป้าหมาย:** Containerize แอปทั้งหมด

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | Dockerfile สำหรับ App | 2% |
| CP2 | 30m | docker-compose.yml | 2% |
| CP3 | 30m | Network + Volumes | 2% |
| CP4 | 30m | docker-compose up ใช้งานได้ | 2% |

**ผลลัพธ์:** `docker-compose up` แล้วทุกอย่างทำงาน!

📖 [Extended: Docker Production](./docs/extended/week06-docker-production.md)

---

### Week 7: 🧪 Testing & CI

**เป้าหมาย:** เขียน Tests + Setup Jenkins

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | pytest Setup + First Test | 2% |
| CP2 | 30m | CRUD Tests (4 tests) | 2% |
| CP3 | 30m | Jenkins Setup | 2% |
| CP4 | 30m | Jenkinsfile CI Pipeline | 2% |

**ผลลัพธ์:** Push code → Jenkins runs tests!

📖 [Extended: Testing Strategies](./docs/extended/week07-testing-strategies.md)

---

### Week 8: 🚀 CD & Go Live

**เป้าหมาย:** Auto Deploy เมื่อ Push

| Checkpoint | เวลา | Task | คะแนน |
|:----------:|:----:|------|:-----:|
| CP1 | 30m | CD Stages in Jenkinsfile | 2% |
| CP2 | 30m | Build + Deploy Stage | 2% |
| CP3 | 30m | Health Check | 2% |
| CP4 | 30m | Full Pipeline Working | 2% |

**ผลลัพธ์:** Push → Test → Build → Deploy → Live! 🎉

📖 [Extended: DevOps Best Practices](./docs/extended/week08-devops.md)

---

## 📂 Repository Structure

```
CSI403-FullStack-Teaching/
├── README.md                     # This file
│
├── workshops/                    # 📋 Workshop Materials
│   ├── week01-setup/
│   │   ├── README.md            # Workshop guide
│   │   ├── CHECKLIST.md         # Checkpoint checklist
│   │   └── solution/            # Reference solution
│   ├── week02-crud/
│   ├── week03-database/
│   ├── week04-frontend/
│   ├── week05-integration/
│   ├── week06-docker/
│   ├── week07-testing/
│   └── week08-cicd/
│
├── docs/                         # 📖 Documentation
│   ├── setup/                   # Installation guides
│   │   ├── windows.md
│   │   ├── macos.md
│   │   └── linux.md
│   └── extended/                # Extended learning
│       ├── week01-git-advanced.md
│       ├── week02-rest-best-practices.md
│       └── ...
│
├── starter-code/                 # 🚀 Starter Templates
│   └── taskflow/                # TaskFlow starter
│
├── presentations/                # 🎬 Slides
│   └── lectures/
│
└── scoring/                      # ✅ Scoring Tools
    ├── checklist-template.md
    └── auto-check/              # Auto-grading scripts
```

---

## ✅ Scoring System

### Checkpoint Scoring (แต่ละ Workshop)

```
┌────────────────────────────────────────────────────────┐
│  Checkpoint 1  │  Checkpoint 2  │  Checkpoint 3  │  CP4 │
│      2%        │      2%        │      2%        │  2%  │
│   ┌─────┐      │   ┌─────┐      │   ┌─────┐      │ ┌───┐│
│   │ ✓/✗ │      │   │ ✓/✗ │      │   │ ✓/✗ │      │ │✓/✗││
│   └─────┘      │   └─────┘      │   └─────┘      │ └───┘│
└────────────────────────────────────────────────────────┘
                        Total: 8% per week
```

### Checkpoint Criteria

| Status | Meaning | Score |
|:------:|---------|:-----:|
| ✅ Complete | ทำได้ครบตาม checklist | 100% |
| 🔶 Partial | ทำได้บางส่วน | 50% |
| ❌ Incomplete | ไม่ได้ทำ / ทำไม่ทัน | 0% |

### ไม่ทันในคาบ?

- สามารถส่งภายใน **24 ชั่วโมง** หลังคาบ (ไม่หักคะแนน)
- หลัง 24 ชั่วโมง: -50%
- หลัง 48 ชั่วโมง: ไม่รับ

---

## 🎓 Learning Outcomes

เมื่อจบคอร์สนี้ คุณจะสามารถ:

1. ✅ สร้าง REST API ด้วย FastAPI
2. ✅ ออกแบบและใช้งาน Database
3. ✅ สร้าง Web UI ด้วย HTML/CSS/JS
4. ✅ รวม Frontend + Backend
5. ✅ Deploy ด้วย Docker
6. ✅ สร้าง CI/CD Pipeline
7. ✅ ทำงานเป็นทีมใน Group Project

---

## 💻 Required Software

ติดตั้งก่อน Week 1:

| Software | Version | Download |
|----------|---------|----------|
| Python | 3.11+ | [python.org](https://python.org) |
| Git | Latest | [git-scm.com](https://git-scm.com) |
| VS Code | Latest | [code.visualstudio.com](https://code.visualstudio.com) |
| Docker Desktop | Latest | [docker.com](https://docker.com) |

📖 [Installation Guide](./docs/setup/)

---

## 🤝 Contributing

พบข้อผิดพลาด หรืออยากเสนอแนะ?
- เปิด Issue บน GitHub
- หรือส่ง Pull Request

---

## 📞 Contact

- **Office Hours:** TBA
- **Discord:** TBA
- **GitHub Issues:** สำหรับคำถามเกี่ยวกับ Workshops

---

**© 2026 CSI403 Full Stack Development**

*"No Homework, Just Hands-on!"* 🚀
