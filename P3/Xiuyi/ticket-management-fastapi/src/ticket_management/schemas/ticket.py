from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TicketBase(BaseModel):
    title: str
    description: str
    tags: List[str] = []

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    pass

class TicketInDB(TicketBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Ticket(TicketInDB):
    pass