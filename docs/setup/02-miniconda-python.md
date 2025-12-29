# 📖 Miniconda &amp; Python Setup Guide

<div align="center">

![Conda](https://img.shields.io/badge/Conda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)

**เวลาที่ใช้: ~20 นาที**

</div>

---

## 📑 Table of Contents

1. [ทำไมต้อง Miniconda?](#1-ทำไมต้อง-miniconda)
2. [ติดตั้ง Miniconda](#2-ติดตั้ง-miniconda)
3. [คำสั่ง Conda เบื้องต้น](#3-คำสั่ง-conda-เบื้องต้น)
4. [สร้าง Environment สำหรับ Course](#4-สร้าง-environment-สำหรับ-course)
5. [Troubleshooting](#5-troubleshooting)

---

## 1. ทำไมต้อง Miniconda?

### ปัญหาของ Python ปกติ

```
Project A: ต้องการ numpy 1.20
Project B: ต้องการ numpy 1.24

😱 ติดตั้งทับกันไปมา = พัง!
```

### Conda แก้ปัญหานี้!

```
┌─────────────────────────────────────────────────────────────┐
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Project A   │  │ Project B   │  │ Project C   │        │
│  │ Python 3.11 │  │ Python 3.11 │  │ Python 3.9  │        │
│  │ numpy 1.20  │  │ numpy 1.24  │  │ pandas 1.5  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│       env: A           env: B           env: C             │
│                                                             │
│  ✅ แยก environment = ไม่ชนกัน!                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. ติดตั้ง Miniconda

### Windows

#### Step 1: Download Miniconda

1. ไปที่ https://docs.conda.io/en/latest/miniconda.html
2. เลือก **Windows** → **Miniconda3 Windows 64-bit**

#### Step 2: Install

1. รัน installer
2. **License Agreement** → I Agree
3. **Install for** → Just Me
4. **Destination Folder** → ใช้ค่า default
5. **Advanced Options:**
   - ✅ **Add Miniconda3 to my PATH** (สำคัญ!)
   - ✅ Register Miniconda3 as my default Python
6. Click Install

#### Step 3: Verify Installation

**ปิด Command Prompt แล้วเปิดใหม่!**

```bash
conda --version
# conda 23.x.x

python --version
# Python 3.11.x
```

---

### macOS

```bash
# Download
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh

# Install
bash Miniconda3-latest-MacOSX-arm64.sh
# ตอบ yes ทั้งหมด

# Restart terminal
conda --version
```

### Linux

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
```

---

## 3. คำสั่ง Conda เบื้องต้น

### 🔹 จัดการ Environment

```bash
# ดู environments ทั้งหมด
conda env list

# สร้าง environment ใหม่
conda create -n myenv python=3.11

# activate environment
conda activate myenv

# deactivate (กลับไป base)
conda deactivate

# ลบ environment
conda remove -n myenv --all
```

### 🔹 ติดตั้ง Packages

```bash
# ติดตั้งผ่าน conda
conda install numpy pandas

# ติดตั้งผ่าน pip (ใน activated env)
pip install fastapi uvicorn

# ดู packages ที่ติดตั้ง
conda list
pip list
```

### 🔹 Export / Import Environment

```bash
# Export
conda env export > environment.yml

# Import
conda env create -f environment.yml
```

---

## 4. สร้าง Environment สำหรับ Course

### Step 1: สร้าง Environment

```bash
conda create -n csi403 python=3.11 -y
```

### Step 2: Activate Environment

```bash
conda activate csi403
```

จะเห็น prompt เปลี่ยนเป็น:
```
(csi403) C:\Users\YourName>
```

### Step 3: ติดตั้ง Packages

```bash
pip install fastapi uvicorn pydantic pydantic-settings
pip install sqlalchemy pyodbc
pip install jinja2 python-multipart
pip install pytest pytest-cov httpx
```

### Step 4: ตรวจสอบ

```bash
python --version
# Python 3.11.x

pip list | grep fastapi
# fastapi    0.109.0
```

---

## 5. Troubleshooting

### ❌ "conda is not recognized"

**แก้ไข (Windows):**
1. เปิด **Anaconda Prompt** แทน Command Prompt

หรือ

2. เพิ่ม PATH:
   - Search "Environment Variables"
   - Edit "Path"
   - Add: `C:\miniconda3`
   - Add: `C:\miniconda3\Scripts`

### ❌ Environment ไม่ activate

**แก้ไข:**
```bash
conda init
# ปิด terminal แล้วเปิดใหม่
```

---

## 📖 Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│  conda create -n NAME python=3.11   # สร้าง env            │
│  conda activate NAME                 # เข้า env             │
│  conda deactivate                    # ออกจาก env           │
│  conda env list                      # ดู env ทั้งหมด       │
│  pip install PACKAGE                 # ติดตั้ง package      │
│  pip list                            # ดู packages          │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist

- [ ] ติดตั้ง Miniconda แล้ว (`conda --version` ทำงาน)
- [ ] สร้าง environment `csi403` แล้ว
- [ ] Activate/Deactivate ได้
- [ ] ติดตั้ง packages ด้วย pip ได้

---

## ➡️ Next Step

[📖 Docker Setup →](./03-docker.md)
