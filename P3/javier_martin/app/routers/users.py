"""User API endpoints."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    description="Retrieve a list of all users with pagination support."
)
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[UserResponse]:
    """
    Retrieve all users.
    
    Args:
        skip: Number of records to skip (for pagination).
        limit: Maximum number of records to return (for pagination).
        db: Database session dependency.
        
    Returns:
        List of users.
    """
    users = UserService.get_all_users(db, skip=skip, limit=limit)
    return users


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get user by ID",
    description="Retrieve a specific user by their unique identifier."
)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    """
    Retrieve a user by ID.
    
    Args:
        user_id: User's unique identifier.
        db: Database session dependency.
        
    Returns:
        User data.
        
    Raises:
        HTTPException: 404 if user not found.
    """
    user = UserService.get_user_by_id(db, user_id)
    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Create a new user with the provided information."
)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    """
    Create a new user.
    
    Args:
        user: User data for creation.
        db: Database session dependency.
        
    Returns:
        Created user data.
        
    Raises:
        HTTPException: 400 if email already exists.
    """
    new_user = UserService.create_user(db, user)
    return new_user


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    description="Update an existing user's information."
)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
) -> UserResponse:
    """
    Update an existing user.
    
    Args:
        user_id: User's unique identifier.
        user_update: User data for update.
        db: Database session dependency.
        
    Returns:
        Updated user data.
        
    Raises:
        HTTPException: 404 if user not found, 400 if email already exists.
    """
    updated_user = UserService.update_user(db, user_id, user_update)
    return updated_user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a user",
    description="Delete a user by their unique identifier."
)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> None:
    """
    Delete a user.
    
    Args:
        user_id: User's unique identifier.
        db: Database session dependency.
        
    Raises:
        HTTPException: 404 if user not found.
    """
    UserService.delete_user(db, user_id)
