from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Task Management System",
    version=settings.APP_VERSION,
)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
