"""Routers exports."""

from app.routers.users import router as users_router
from app.routers.tickets import router as tickets_router

__all__ = ["users_router", "tickets_router"]
