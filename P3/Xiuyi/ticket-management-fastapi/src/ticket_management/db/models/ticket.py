from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ticket_management.db.base import Base

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    title = Column(String, index=True)
    description = Column(Text)
    tags = Column(String)  # You may want to use a more complex type for tags

    author = relationship("User", back_populates="tickets")