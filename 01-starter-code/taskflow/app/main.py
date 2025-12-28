# app/main.py
"""TaskFlow - Task Management System."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="Task Management System for CSI403 Full Stack Development",
    version=settings.APP_VERSION,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: Mount static files (after creating static folder)
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

# TODO: Include routers (after creating routes)
# from app.routes import tasks_router, categories_router, users_router
# app.include_router(tasks_router)
# app.include_router(categories_router)
# app.include_router(users_router)


@app.get("/", tags=["Health"])
def root():
    """Root endpoint - Welcome message."""
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "running"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
