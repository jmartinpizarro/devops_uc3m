"""Repositories exports."""

from app.repositories.user_repository import UserRepository
from app.repositories.ticket_repository import TicketRepository

__all__ = ["UserRepository", "TicketRepository"]
