from __future__ import annotations

from fastapi import FastAPI

from app.core.config import settings
from app.presentation.api.routes import users_router, tickets_router

app = FastAPI(title=settings.app_name)

app.include_router(users_router, prefix=settings.api_prefix)
app.include_router(tickets_router, prefix=settings.api_prefix)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
