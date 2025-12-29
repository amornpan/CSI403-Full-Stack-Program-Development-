# Extended: Docker Production

## Multi-stage Build
```dockerfile
FROM python:3.11 AS builder
COPY requirements.txt .
RUN pip wheel -r requirements.txt -w /wheels

FROM python:3.11-slim
COPY --from=builder /wheels /wheels
RUN pip install /wheels/*
```

## Health Checks
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
  interval: 30s
```

## Resource Limits
```yaml
deploy:
  resources:
    limits:
      cpus: '0.5'
      memory: 512M
```
