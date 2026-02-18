"""User Pydantic schemas for validation and serialization."""

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    """Base user schema with common attributes."""

    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    email: EmailStr = Field(..., description="User's email address")


class UserCreate(UserBase):
    """Schema for creating a new user."""

    pass


class UserUpdate(BaseModel):
    """Schema for updating an existing user."""

    name: Optional[str] = Field(None, min_length=1, max_length=100, description="User's full name")
    email: Optional[EmailStr] = Field(None, description="User's email address")


class UserResponse(UserBase):
    """Schema for user response with database fields."""

    id: int = Field(..., description="User's unique identifier")

    model_config = ConfigDict(from_attributes=True)
