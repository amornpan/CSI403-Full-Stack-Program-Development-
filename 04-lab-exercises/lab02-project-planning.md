# Lab 02: Project Planning & Notion

**Week 2 | Practice Lab (ไม่มีคะแนน)**

## 🎯 Objectives
- เข้าใจ Agile/Scrum Methodology
- ใช้ Notion สำหรับ Project Management
- เขียน User Stories และ Acceptance Criteria
- สร้าง Kanban Board สำหรับ Sprint Planning

## 📋 Prerequisites
- มี Notion Account (ฟรี)
- เข้าใจ Loan Management System ที่จะพัฒนา

## 💻 Part 1: Agile/Scrum Overview (20 min)

### 1.1 Scrum Framework
```
┌─────────────────────────────────────────────────────────────────┐
│                      SCRUM FRAMEWORK                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Product    ──▶   Sprint    ──▶   Sprint   ──▶   Increment    │
│   Backlog         Planning         (1-4 weeks)    (Working     │
│                                                    Software)    │
│                        │                                        │
│                        ▼                                        │
│                 ┌─────────────┐                                │
│                 │   Daily     │                                │
│                 │   Standup   │                                │
│                 │  (15 min)   │                                │
│                 └─────────────┘                                │
│                                                                 │
│   Roles: Product Owner, Scrum Master, Development Team         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Key Concepts

| Concept | Description |
|---------|-------------|
| **Sprint** | ช่วงเวลาการพัฒนา 1-4 สัปดาห์ |
| **Product Backlog** | รายการ Features ทั้งหมดที่ต้องทำ |
| **Sprint Backlog** | รายการงานที่จะทำใน Sprint นี้ |
| **Daily Standup** | ประชุมสั้น 15 นาที ทุกวัน |
| **Sprint Review** | Demo ผลงานให้ Stakeholder ดู |
| **Sprint Retrospective** | ทบทวนว่าอะไรดี/ต้องปรับปรุง |

## 💻 Part 2: Notion Setup (30 min)

### 2.1 Create Workspace
1. ไปที่ https://notion.so และ Sign up
2. Create New Workspace: `CSI403-GroupX` (X = เลขกลุ่ม)
3. Invite team members

### 2.2 Create Project Board
สร้างหน้าใหม่ชื่อ "Loan Management System"

**Page Structure:**
```
📁 Loan Management System
├── 📋 Product Backlog (Database)
├── 🏃 Sprint Board (Kanban)
├── 📝 Meeting Notes
├── 📖 Documentation
│   ├── SRS Document
│   ├── Database Design
│   └── API Specification
└── 👥 Team Members
```

### 2.3 Create Product Backlog Database
สร้าง Database ใหม่แบบ Table:

**Properties:**
| Property | Type | Options |
|----------|------|---------|
| Title | Title | - |
| Status | Select | Backlog, To Do, In Progress, Review, Done |
| Priority | Select | High, Medium, Low |
| Sprint | Select | Sprint 1, Sprint 2, Sprint 3, ... |
| Assignee | Person | Team members |
| Story Points | Number | 1, 2, 3, 5, 8, 13 |
| Epic | Select | Auth, Loan, Payment, Admin, UI |
| Due Date | Date | - |

## 💻 Part 3: User Stories (40 min)

### 3.1 User Story Format
```
As a [role],
I want to [action],
So that [benefit].

Acceptance Criteria:
- Given [context]
- When [action]
- Then [expected result]
```

### 3.2 Example User Stories for Loan System

**Epic: Authentication**

```markdown
## US-001: User Registration

**As a** new user,
**I want to** create an account,
**So that** I can access the loan application system.

**Acceptance Criteria:**
- [ ] User can enter username, email, and password
- [ ] Password must be at least 8 characters with uppercase, lowercase, and number
- [ ] Email must be unique in the system
- [ ] After registration, user is redirected to login page
- [ ] Confirmation message is displayed

**Story Points:** 3
**Priority:** High
**Epic:** Authentication
```

```markdown
## US-002: User Login

**As a** registered user,
**I want to** log in to my account,
**So that** I can access my loan information.

**Acceptance Criteria:**
- [ ] User can enter username and password
- [ ] Invalid credentials show error message
- [ ] Successful login redirects to dashboard
- [ ] Session is created for 24 hours
- [ ] "Remember me" option extends session

**Story Points:** 2
**Priority:** High
**Epic:** Authentication
```

**Epic: Loan Management**

```markdown
## US-003: View My Loans

**As a** borrower,
**I want to** see a list of my loans,
**So that** I can track my borrowing status.

**Acceptance Criteria:**
- [ ] Display all loans for logged-in user
- [ ] Show loan amount, status, monthly payment
- [ ] Can filter by status (current, paid, late)
- [ ] Can sort by date or amount
- [ ] Click on loan shows details

**Story Points:** 3
**Priority:** High
**Epic:** Loan
```

```markdown
## US-004: Apply for New Loan

**As a** borrower,
**I want to** apply for a new loan,
**So that** I can get financing for my needs.

**Acceptance Criteria:**
- [ ] Form with amount, term, purpose
- [ ] Amount range: 10,000 - 1,000,000 THB
- [ ] Term options: 12, 24, 36, 48, 60 months
- [ ] Show estimated monthly payment
- [ ] Validation before submission
- [ ] Confirmation after successful submission

**Story Points:** 5
**Priority:** High
**Epic:** Loan
```

```markdown
## US-005: Make Payment

**As a** borrower,
**I want to** make a payment on my loan,
**So that** I can reduce my debt.

**Acceptance Criteria:**
- [ ] Select loan to pay
- [ ] Enter payment amount
- [ ] Show remaining balance
- [ ] Generate payment receipt
- [ ] Update loan status if paid off

**Story Points:** 5
**Priority:** High
**Epic:** Payment
```

**Epic: Admin**

```markdown
## US-006: Approve/Reject Loan

**As an** admin,
**I want to** approve or reject loan applications,
**So that** I can manage lending risk.

**Acceptance Criteria:**
- [ ] See list of pending applications
- [ ] View applicant details and history
- [ ] Approve with assigned interest rate
- [ ] Reject with reason
- [ ] Notification sent to applicant

**Story Points:** 5
**Priority:** High
**Epic:** Admin
```

### 3.3 Exercise: Write More User Stories

เขียน User Stories เพิ่มเติมสำหรับ:

1. **US-007:** View Payment History
2. **US-008:** Update Profile
3. **US-009:** Admin Dashboard
4. **US-010:** Generate Reports

## 💻 Part 4: Sprint Planning (20 min)

### 4.1 Create Kanban Board View
ใน Notion ให้สร้าง Board View จาก Product Backlog:

**Columns:**
```
| Backlog | To Do | In Progress | Review | Done |
|---------|-------|-------------|--------|------|
| US-007  | US-003| US-001      | US-002 | -    |
| US-008  | US-004|             |        |      |
| US-009  | US-005|             |        |      |
| US-010  | US-006|             |        |      |
```

### 4.2 Sprint 1 Planning (สำหรับโปรเจค)

**Sprint 1 Goal:** Core Authentication & Basic Loan View

**Sprint Backlog:**
- US-001: User Registration (3 points)
- US-002: User Login (2 points)
- US-003: View My Loans (3 points)

**Total:** 8 Story Points

### 4.3 Velocity Planning

| Sprint | Planned Points | Notes |
|--------|---------------|-------|
| Sprint 1 (Week 10) | 8 | Auth + Basic View |
| Sprint 2 (Week 11) | 10 | CRUD Operations |
| Sprint 3 (Week 12) | 8 | Integration |
| Sprint 4 (Week 13) | 5 | Testing |
| Sprint 5 (Week 14) | 5 | Deployment |

## 💻 Part 5: Meeting Notes Template (10 min)

### 5.1 Daily Standup Template
```markdown
# Daily Standup - [Date]

## Team Members Present
- [ ] Member 1
- [ ] Member 2
- [ ] Member 3

## Updates

### Member 1
- **Yesterday:** What did you complete?
- **Today:** What will you work on?
- **Blockers:** Any impediments?

### Member 2
- **Yesterday:** 
- **Today:** 
- **Blockers:** 

### Member 3
- **Yesterday:** 
- **Today:** 
- **Blockers:** 
```

### 5.2 Sprint Review Template
```markdown
# Sprint [X] Review - [Date]

## Sprint Goal
[What was the goal?]

## Completed Items
- [ ] US-001: User Registration ✅
- [ ] US-002: User Login ✅
- [ ] US-003: View My Loans ✅

## Demo Notes
[Key points from demo]

## Feedback
[Stakeholder feedback]

## Carry Over
[Items not completed]
```

## 📝 Assignment (For G1: Project Proposal)

สำหรับ **G1: Project Proposal (10%)** ใน Week 3:

### Deliverables:
1. **Notion Workspace** พร้อม:
   - Product Backlog (อย่างน้อย 15 User Stories)
   - Sprint Board
   - Team Members page

2. **SRS Document** ใน Notion:
   - Project Overview
   - Functional Requirements
   - Non-functional Requirements
   - Use Case Diagram

3. **Project Timeline**:
   - Sprint Planning (5 Sprints)
   - Milestones

### Grading Rubric (10%):
| Criteria | Points |
|----------|:------:|
| User Stories (15+) | 3% |
| SRS Document | 3% |
| Notion Organization | 2% |
| Sprint Planning | 2% |

## 📚 Resources

- [Notion Templates](https://www.notion.so/templates)
- [Scrum Guide](https://scrumguides.org/)
- [User Story Mapping](https://www.jpattonassociates.com/user-story-mapping/)
- [Agile Manifesto](https://agilemanifesto.org/)

---
**Next:** Lab 03 - HTML, CSS & Bootstrap
