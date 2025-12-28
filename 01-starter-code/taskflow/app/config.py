# app/config.py
"""Application configuration settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    APP_NAME: str = "TaskFlow"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "mssql+pyodbc://sa:YourStrong@Password123@localhost:1433/taskflow?driver=ODBC+Driver+17+for+SQL+Server"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    
    class Config:
        env_file = ".env"


settings = Settings()
