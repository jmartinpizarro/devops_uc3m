"""Ticket Pydantic schemas for validation and serialization."""

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List


class TicketBase(BaseModel):
    """Base ticket schema with common attributes."""

    title: str = Field(..., min_length=1, max_length=200, description="Ticket title")
    description: str = Field(..., min_length=1, description="Ticket detailed description")
    tags: List[str] = Field(default_factory=list, description="List of tags/keywords")


class TicketCreate(TicketBase):
    """Schema for creating a new ticket."""

    author_id: int = Field(..., gt=0, description="ID of the ticket author")


class TicketUpdate(BaseModel):
    """Schema for updating an existing ticket."""

    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Ticket title")
    description: Optional[str] = Field(None, min_length=1, description="Ticket detailed description")
    tags: Optional[List[str]] = Field(None, description="List of tags/keywords")


class TicketResponse(TicketBase):
    """Schema for ticket response with database fields."""

    id: int = Field(..., description="Ticket's unique identifier")
    created_at: datetime = Field(..., description="Ticket creation timestamp")
    author_id: int = Field(..., description="ID of the ticket author")

    model_config = ConfigDict(from_attributes=True)
