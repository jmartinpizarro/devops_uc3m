from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class TicketCreate(BaseModel):
    author_id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=5000)
    tags: list[str] = Field(default_factory=list, max_length=50)


class TicketUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, min_length=1, max_length=5000)
    tags: list[str] | None = None


class TicketOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_id: int
    created_at: datetime
    title: str
    description: str
    tags: list[str]
