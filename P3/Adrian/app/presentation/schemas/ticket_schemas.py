from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None
    tags: List[str] = []

class TicketCreate(TicketBase):
    author_id: int

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None

class Ticket(TicketBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        from_attributes = True