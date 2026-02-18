from __future__ import annotations

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Ticketing API"
    environment: str = "local"

    # SQLite por defecto para desarrollo local.
    # En Docker Compose se inyectará Postgres.
    database_url: str = "sqlite+pysqlite:///./app.db"

    api_prefix: str = "/api/v1"


settings = Settings()
