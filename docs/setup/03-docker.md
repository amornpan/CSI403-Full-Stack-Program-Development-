# 📖 Docker Setup Guide

<div align="center">

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**เวลาที่ใช้: ~30 นาที**

</div>

---

## 📑 Table of Contents

1. [Docker คืออะไร?](#1-docker-คืออะไร)
2. [ติดตั้ง Docker Desktop](#2-ติดตั้ง-docker-desktop)
3. [คำสั่ง Docker เบื้องต้น](#3-คำสั่ง-docker-เบื้องต้น)
4. [Docker Compose](#4-docker-compose)
5. [ทดลองใช้งาน](#5-ทดลองใช้งาน)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Docker คืออะไร?

Docker เหมือน "กล่อง" ที่บรรจุ app + ทุกอย่างที่ต้องใช้

```
┌─────────────────────────────────────────────────────────────┐
│                         Container                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Your App + Python + FastAPI + Dependencies          │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  รันได้เหมือนกันทุกที่! (Windows, Mac, Linux, Server)       │
└─────────────────────────────────────────────────────────────┘
```

### คำศัพท์สำคัญ

| Term | คืออะไร |
|------|---------|
| **Image** | Template สำหรับสร้าง container |
| **Container** | Instance ที่รันจาก image |
| **Dockerfile** | Script สำหรับสร้าง image |
| **Docker Hub** | Registry เก็บ images |

---

## 2. ติดตั้ง Docker Desktop

### Windows

#### Prerequisites
- Windows 10/11 64-bit
- WSL 2

#### Step 1: Enable WSL 2

เปิด **PowerShell as Administrator**:

```powershell
wsl --install
# Restart computer
```

หลัง restart:
```powershell
wsl --set-default-version 2
```

#### Step 2: Download Docker Desktop

1. ไปที่ https://www.docker.com/products/docker-desktop/
2. Click **Download for Windows**

#### Step 3: Install

1. รัน installer
2. ✅ Use WSL 2 instead of Hyper-V
3. Click **Ok** → **Restart**

#### Step 4: Verify

```bash
docker --version
# Docker version 24.x.x

docker compose version
# Docker Compose version v2.x.x
```

#### Step 5: Test

```bash
docker run hello-world
```

✅ ถ้าเห็น "Hello from Docker!" = สำเร็จ!

---

### macOS

1. Download จาก https://www.docker.com/products/docker-desktop/
2. เปิดไฟล์ `.dmg` และลาก Docker ไป Applications
3. เปิด Docker จาก Applications

### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2
sudo usermod -aG docker $USER
# Logout and login again
```

---

## 3. คำสั่ง Docker เบื้องต้น

### 🔹 ดูข้อมูล

```bash
docker --version          # version
docker images             # ดู images
docker ps                 # ดู containers ที่รัน
docker ps -a              # ดู containers ทั้งหมด
```

### 🔹 จัดการ Images

```bash
docker pull python:3.11   # ดึง image
docker images             # ดู images
docker rmi python:3.11    # ลบ image
```

### 🔹 จัดการ Containers

```bash
docker run -d --name my-app python:3.11 sleep infinity
docker stop my-app
docker start my-app
docker rm my-app
```

### 🔹 รันแบบต่างๆ

```bash
# Interactive mode
docker run -it python:3.11 bash

# Background + Port mapping
docker run -d -p 8000:8000 --name api my-image

# Mount volume
docker run -d -v $(pwd):/app my-image
```

### 🔹 Logs และ Execute

```bash
docker logs my-container
docker logs -f my-container      # follow
docker exec -it my-container bash
```

---

## 4. Docker Compose

### Docker Compose คืออะไร?

เครื่องมือสำหรับรันหลาย containers พร้อมกัน

### ตัวอย่าง docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
```

### คำสั่ง Docker Compose

```bash
docker compose up -d        # รันทุก services
docker compose down         # หยุดทุก services
docker compose logs         # ดู logs
docker compose ps           # ดู status
docker compose exec app bash
```

---

## 5. ทดลองใช้งาน

### 🎯 Exercise 1: รัน Python

```bash
docker run -it python:3.11 python
>>> print("Hello from Docker!")
>>> exit()
```

### 🎯 Exercise 2: รัน Web Server

```bash
docker run -d -p 8080:80 --name nginx-test nginx

# เปิด browser: http://localhost:8080

docker stop nginx-test
docker rm nginx-test
```

### 🎯 Exercise 3: รัน MSSQL

```bash
docker run -d \
  --name mssql-test \
  -e "ACCEPT_EULA=Y" \
  -e "SA_PASSWORD=YourStrong@Pass123" \
  -p 1433:1433 \
  mcr.microsoft.com/mssql/server:2022-latest

# รอ ~30 วินาที
docker logs mssql-test

docker stop mssql-test
docker rm mssql-test
```

---

## 6. Troubleshooting

### ❌ "docker: command not found"

**แก้ไข:** ตรวจสอบว่า Docker Desktop กำลังรัน

### ❌ "Cannot connect to the Docker daemon"

**แก้ไข:** เปิด Docker Desktop และรอจน icon ไม่กระพริบ

### ❌ "WSL 2 installation is incomplete"

**แก้ไข:**
```powershell
wsl --update
wsl --set-default-version 2
# Restart
```

### ❌ "port is already allocated"

**แก้ไข:** ใช้ port อื่น เช่น `-p 8001:8000`

---

## 📖 Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│  docker images                       # list images          │
│  docker pull IMAGE                   # download image       │
│  docker run -d --name N IMAGE        # run container        │
│  docker stop NAME                    # stop container       │
│  docker rm NAME                      # remove container     │
│  docker logs NAME                    # view logs            │
│  docker exec -it NAME bash           # enter container      │
│                                                             │
│  docker compose up -d                # start services       │
│  docker compose down                 # stop services        │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist

- [ ] Docker Desktop ติดตั้งแล้ว
- [ ] `docker --version` ทำงาน
- [ ] `docker compose version` ทำงาน
- [ ] `docker run hello-world` สำเร็จ

---

## ➡️ Next Step

[📖 VS Code Setup →](./04-vscode.md)
