from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "TaskFlow"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

settings = Settings()
