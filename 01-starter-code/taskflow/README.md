# TaskFlow - Task Management System

CSI403 Full Stack Development - Starter Code

## 📋 Description

ระบบจัดการงาน (Task Management System) สำหรับวิชา CSI403

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python 3.11+, SQLAlchemy
- **Database:** MSSQL (Docker)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5, Jinja2
- **DevOps:** Docker, Docker Compose, Jenkins

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker Desktop

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run MSSQL Docker
docker-compose up -d db

# Run development server
uvicorn app.main:app --reload
```

### Access

- App: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📁 Project Structure

```
taskflow/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── config.py         # Settings
│   ├── database.py       # DB connection
│   ├── models/           # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   └── task.py
│   ├── schemas/          # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   └── task.py
│   ├── routes/           # API routes
│   │   ├── __init__.py
│   │   ├── tasks.py
│   │   ├── categories.py
│   │   └── users.py
│   ├── templates/        # Jinja2 templates
│   └── static/           # CSS, JS, images
├── tests/                # Test files
├── .env                  # Environment variables
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

## 🔧 Environment Variables

Create `.env` file:

```
DATABASE_URL=mssql+pyodbc://sa:YourStrong@Password123@localhost:1433/taskflow?driver=ODBC+Driver+17+for+SQL+Server
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## 📝 License

MIT License
