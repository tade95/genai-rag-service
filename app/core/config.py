"""
Configuración por environment
Docstring for demo-genai-service.app.core.config
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Demo GenAI Service"
    environment: str = "development"
    log_level: str = "info"
    app_version: str = "0.1.0"
    
    class Config:
        env_file = ".env"

settings = Settings()   
