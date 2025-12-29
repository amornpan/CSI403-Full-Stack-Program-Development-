# 📖 Git &amp; GitHub Setup Guide

<div align="center">

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

**เวลาที่ใช้: ~30 นาที**

</div>

---

## 📑 Table of Contents

1. [Git คืออะไร?](#1-git-คืออะไร)
2. [ติดตั้ง Git](#2-ติดตั้ง-git)
3. [สมัคร GitHub](#3-สมัคร-github)
4. [ตั้งค่า Git](#4-ตั้งค่า-git)
5. [คำสั่ง Git เบื้องต้น](#5-คำสั่ง-git-เบื้องต้น)
6. [ทดลองใช้งาน](#6-ทดลองใช้งาน)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Git คืออะไร?

### Version Control System

Git ช่วยให้เรา:
- ✅ **Track Changes** - เก็บประวัติการแก้ไขทั้งหมด
- ✅ **Backup** - ไม่มีวัน "ลบไฟล์หาย"
- ✅ **Collaborate** - ทำงานร่วมกับคนอื่นได้
- ✅ **Branching** - ทดลองโค้ดใหม่โดยไม่กระทบของเดิม

### Git vs GitHub

| Git | GitHub |
|-----|--------|
| โปรแกรมบนเครื่องคุณ | เว็บไซต์บน Cloud |
| เก็บประวัติ code | เก็บ code online |
| ทำงาน offline ได้ | ต้องมี internet |
| Free &amp; Open Source | Free (public repos) |

```
Your Computer          GitHub.com
┌──────────────┐       ┌──────────────┐
│     Git      │ push  │   GitHub     │
│  (local)     │ ───▶  │   (remote)   │
│              │ ◀───  │              │
└──────────────┘ pull  └──────────────┘
```

---

## 2. ติดตั้ง Git

### Windows

#### Step 1: Download Git

1. ไปที่ https://git-scm.com/download/win
2. Download จะเริ่มอัตโนมัติ (เลือก 64-bit)

#### Step 2: Install Git

1. รัน installer ที่ download มา
2. ทำตามขั้นตอน:

**หน้า Select Components:**
- ✅ ใช้ค่า default ทั้งหมด

**หน้า Choosing the default editor:**
- เลือก **Use Visual Studio Code as Git's default editor**

**หน้า Adjusting the name of the initial branch:**
- เลือก **Override the default branch name**
- ใส่ `main`

**หน้าอื่นๆ:** ใช้ค่า default กด Next ไปเรื่อยๆ

#### Step 3: Verify Installation

เปิด **Command Prompt** หรือ **PowerShell**:

```bash
git --version
```

ต้องเห็น:
```
git version 2.43.0.windows.1
```

✅ ถ้าเห็น version = ติดตั้งสำเร็จ!

---

### macOS

```bash
# Option 1: Xcode Command Line Tools
xcode-select --install

# Option 2: Homebrew
brew install git
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git -y
```

---

## 3. สมัคร GitHub

### Step 1: ไปที่ GitHub.com

1. เปิด https://github.com/
2. Click **Sign up**

### Step 2: สร้าง Account

1. **Enter your email** - ใช้ email มหาวิทยาลัย (แนะนำ)
2. **Create a password** - อย่างน้อย 8 ตัว มีตัวเลข
3. **Enter a username** - จะเป็นชื่อ URL ของคุณ
4. **Verify your account** - ทำตาม puzzle
5. Click **Create account**

### Step 3: Verify Email

เปิด email และ click link ยืนยันจาก GitHub

---

## 4. ตั้งค่า Git

### 4.1 ตั้งชื่อและ Email

```bash
# ตั้งชื่อ (ใช้ชื่อจริง)
git config --global user.name "Somchai Jaidee"

# ตั้ง email (ใช้ email เดียวกับ GitHub)
git config --global user.email "somchai@email.com"
```

### 4.2 ตั้ง Default Branch

```bash
git config --global init.defaultBranch main
```

### 4.3 ตรวจสอบการตั้งค่า

```bash
git config --list
```

---

## 5. คำสั่ง Git เบื้องต้น

### 🔹 สร้าง Repository ใหม่

```bash
mkdir my-project
cd my-project
git init
```

### 🔹 Clone Repository ที่มีอยู่

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 🔹 ดูสถานะ

```bash
git status
```

### 🔹 เพิ่มไฟล์เข้า Staging

```bash
git add filename.py    # เพิ่มไฟล์เดียว
git add .              # เพิ่มทุกไฟล์
```

### 🔹 Commit

```bash
git commit -m "Add new feature"
```

### 🔹 Push ขึ้น GitHub

```bash
git push -u origin main    # ครั้งแรก
git push                   # ครั้งถัดไป
```

### 🔹 Pull จาก GitHub

```bash
git pull
```

### 🔹 ดูประวัติ

```bash
git log --oneline
```

---

## 6. ทดลองใช้งาน

### 🎯 Mini Exercise: สร้าง Repo แรก

#### Step 1: สร้าง Repo บน GitHub

1. ไปที่ https://github.com/new
2. Repository name: `hello-git`
3. ✅ Add a README file
4. Click **Create repository**

#### Step 2: Clone มาที่เครื่อง

```bash
git clone https://github.com/YOUR_USERNAME/hello-git.git
cd hello-git
```

#### Step 3: สร้างไฟล์ใหม่

```bash
echo "print('Hello, Git!')" > hello.py
git status
```

#### Step 4: Add และ Commit

```bash
git add hello.py
git commit -m "Add hello.py"
```

#### Step 5: Push ขึ้น GitHub

```bash
git push
```

✅ ถ้าทำได้ครบ = พร้อมใช้ Git!

---

## 7. Troubleshooting

### ❌ "git is not recognized"

**แก้ไข:** ปิด Terminal แล้วเปิดใหม่ หรือติดตั้ง Git ใหม่

### ❌ "Permission denied" เวลา push

**แก้ไข:** Login GitHub ผ่าน popup ที่ขึ้นมา

### ❌ "fatal: not a git repository"

**แก้ไข:** ตรวจสอบว่าอยู่ถูก folder และรัน `git init`

---

## 📖 Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│  git init                    # สร้าง repo ใหม่              │
│  git clone <url>             # clone repo                   │
│  git status                  # ดูสถานะ                      │
│  git add .                   # stage ทุกไฟล์                │
│  git commit -m "message"     # commit                       │
│  git push                    # ส่งขึ้น remote               │
│  git pull                    # ดึงจาก remote                │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist

- [ ] ติดตั้ง Git แล้ว (`git --version` ทำงาน)
- [ ] มี GitHub account แล้ว
- [ ] ตั้งค่า user.name และ user.email แล้ว
- [ ] Clone repo จาก GitHub ได้
- [ ] Push ขึ้น GitHub ได้

---

## ➡️ Next Step

[📖 Miniconda &amp; Python Setup →](./02-miniconda-python.md)
