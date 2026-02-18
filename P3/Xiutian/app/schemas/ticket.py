from pydantic import BaseModel
from typing import List
from datetime import datetime

class TicketBase(BaseModel):
    title: str
    description: str
    tags: List[str] = []

class TicketCreate(TicketBase):
    author_id: int

class TicketRead(TicketBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True  # <- Cambiar from_attributes por orm_mode
