"""Application configuration settings."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings with environment variables support."""

    database_url: str = "sqlite:///./tickets.db"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = True
    
    class Config:
        """Pydantic configuration."""
        
        env_file = ".env"
        case_sensitive = False


settings = Settings()
