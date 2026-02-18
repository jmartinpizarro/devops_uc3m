"""Ticket database model."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from typing import List

from app.database import Base


class Ticket(Base):
    """Ticket model representing support tickets."""

    __tablename__ = "tickets"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(Text, nullable=False)
    tags: List[str] = Column(JSON, default=list)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    author_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship with user
    author = relationship("User", back_populates="tickets")

    def __repr__(self) -> str:
        """String representation of Ticket."""
        return f"<Ticket(id={self.id}, title='{self.title}', author_id={self.author_id})>"
