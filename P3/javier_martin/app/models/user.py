"""User database model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    """User model representing system users."""

    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String(100), nullable=False)
    email: str = Column(String(255), unique=True, nullable=False, index=True)

    # Relationship with tickets
    tickets = relationship("Ticket", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """String representation of User."""
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
