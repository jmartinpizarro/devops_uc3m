from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.infrastructure.database.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(ARRAY(String), default=list)

    # Relationship
    author = relationship("User", back_populates="tickets")