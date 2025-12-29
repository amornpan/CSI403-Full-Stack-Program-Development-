# Workshop 6: 🐳 Docker Deployment

## 📋 Overview
| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | Dockerfile + Docker Compose |

---

## 💻 CP1: Dockerfile (2%)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

```bash
docker build -t taskflow:latest .
```

---

## 💻 CP2: Run Container (2%)

```bash
docker run -d -p 8000:8000 --name taskflow-app taskflow:latest
curl http://localhost:8000/health
```

---

## 💻 CP3: Docker Compose (2%)

### docker-compose.yml
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
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=TaskFlow@123
    ports:
      - "1433:1433"
```

---

## 💻 CP4: Full Stack (2%)

```bash
docker compose up -d
docker compose ps
```

Test at http://localhost:8000

```bash
git add . &amp;&amp; git commit -m "Add Docker" &amp;&amp; git push
```

---

[📖 Extended →](../../docs/extended/week06-docker-production.md)
