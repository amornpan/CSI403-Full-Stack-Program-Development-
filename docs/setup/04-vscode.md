# 📖 VS Code Setup Guide

<div align="center">

![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

**เวลาที่ใช้: ~15 นาที**

</div>

---

## 📑 Table of Contents

1. [ติดตั้ง VS Code](#1-ติดตั้ง-vs-code)
2. [Essential Extensions](#2-essential-extensions)
3. [ตั้งค่า Settings](#3-ตั้งค่า-settings)
4. [Keyboard Shortcuts](#4-keyboard-shortcuts)

---

## 1. ติดตั้ง VS Code

1. ไปที่ https://code.visualstudio.com/
2. Click **Download**
3. รัน installer

**Windows Options:**
- ✅ Add "Open with Code" to context menu
- ✅ Add to PATH

### Verify

```bash
code --version
```

---

## 2. Essential Extensions

### วิธีติดตั้ง

1. กด `Ctrl+Shift+X`
2. Search ชื่อ extension
3. Click **Install**

### 🔴 Required

| Extension | รายละเอียด |
|-----------|-----------|
| **Python** (Microsoft) | Python support |
| **Pylance** | IntelliSense |

### 🟡 Recommended

| Extension | รายละเอียด |
|-----------|-----------|
| **GitLens** | Git history |
| **Docker** | Docker support |
| **Thunder Client** | API testing |
| **Prettier** | Code formatter |

### Quick Install

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-docker
```

---

## 3. ตั้งค่า Settings

กด `Ctrl+Shift+P` → "Open User Settings (JSON)"

```json
{
    "editor.fontSize": 14,
    "editor.tabSize": 4,
    "editor.formatOnSave": true,
    "editor.wordWrap": "on",
    "files.autoSave": "afterDelay",
    "python.defaultInterpreterPath": "python",
    "git.autofetch": true
}
```

---

## 4. Keyboard Shortcuts

### General

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+P` | Quick Open |
| `Ctrl+`` ` | Toggle Terminal |
| `Ctrl+B` | Toggle Sidebar |

### Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl+D` | Select next occurrence |
| `Ctrl+/` | Toggle comment |
| `Alt+Up/Down` | Move line |
| `Ctrl+Shift+K` | Delete line |

---

## 💡 Tips

### เปิด Folder

```bash
code .           # เปิด folder ปัจจุบัน
code my-project  # เปิด folder ที่ระบุ
```

### Select Python Interpreter

1. กด `Ctrl+Shift+P`
2. พิมพ์ "Python: Select Interpreter"
3. เลือก conda environment

---

## ✅ Checklist

- [ ] ติดตั้ง VS Code แล้ว
- [ ] ติดตั้ง Python + Pylance extensions
- [ ] ตั้งค่า settings

---

## 🎉 Setup Complete!

คุณพร้อมเริ่มเรียนแล้ว!

[🚀 กลับไป Course Home →](../../README.md)
