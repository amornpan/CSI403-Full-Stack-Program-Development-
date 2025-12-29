# 📖 Git &amp; GitHub Setup Guide

**เวลาที่ใช้: ~30 นาที**

---

## 1. Git คืออะไร?

Git = Version Control System ช่วยเก็บประวัติการแก้ไขโค้ด

```
Your Computer          GitHub.com
┌──────────────┐       ┌──────────────┐
│     Git      │ push  │   GitHub     │
│   (local)    │ ────▶ │   (remote)   │
│              │ ◀──── │              │
└──────────────┘ pull  └──────────────┘
```

---

## 2. ติดตั้ง Git

### Windows

1. Download จาก https://git-scm.com/download/win
2. รัน installer (ใช้ค่า default)
3. เลือก "Override default branch" → `main`

### Verify

```bash
git --version
# git version 2.43.0
```

---

## 3. สมัคร GitHub

1. ไปที่ https://github.com/
2. Click **Sign up**
3. กรอก email, password, username
4. Verify email

---

## 4. ตั้งค่า Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main
```

ตรวจสอบ:
```bash
git config --list
```

---

## 5. คำสั่งเบื้องต้น

```bash
# สร้าง repo ใหม่
git init

# clone repo
git clone https://github.com/user/repo.git

# ดูสถานะ
git status

# stage files
git add .

# commit
git commit -m "message"

# push
git push

# pull
git pull
```

---

## 6. ทดลองใช้งาน

1. สร้าง repo บน GitHub ชื่อ `hello-git`
2. Clone มาที่เครื่อง
3. สร้างไฟล์ `hello.py`
4. Add, Commit, Push

```bash
git clone https://github.com/YOUR_USERNAME/hello-git.git
cd hello-git
echo "print('Hello')" > hello.py
git add .
git commit -m "Add hello.py"
git push
```

---

## ✅ Checklist

- [ ] Git installed
- [ ] GitHub account created
- [ ] Git configured
- [ ] Can push to GitHub

---

[➡️ Next: Miniconda Setup](./02-miniconda-python.md)
