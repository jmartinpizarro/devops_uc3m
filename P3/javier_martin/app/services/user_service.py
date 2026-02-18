"""User service with business logic."""

from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository


class UserService:
    """Service layer for User business logic."""

    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """
        Retrieve all users with pagination.
        
        Args:
            db: Database session.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            
        Returns:
            List of User objects.
        """
        return UserRepository.get_all(db, skip, limit)

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        """
        Retrieve a user by ID.
        
        Args:
            db: Database session.
            user_id: User's unique identifier.
            
        Returns:
            User object.
            
        Raises:
            HTTPException: If user not found.
        """
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return user

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        """
        Create a new user.
        
        Args:
            db: Database session.
            user: User data for creation.
            
        Returns:
            Created User object.
            
        Raises:
            HTTPException: If email already exists.
        """
        # Check if email already exists
        existing_user = UserRepository.get_by_email(db, user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        return UserRepository.create(db, user)

    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User:
        """
        Update an existing user.
        
        Args:
            db: Database session.
            user_id: User's unique identifier.
            user_update: User data for update.
            
        Returns:
            Updated User object.
            
        Raises:
            HTTPException: If user not found or email already exists.
        """
        # Check if user exists
        existing_user = UserRepository.get_by_id(db, user_id)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        
        # Check if new email is already taken by another user
        if user_update.email:
            user_with_email = UserRepository.get_by_email(db, user_update.email)
            if user_with_email and user_with_email.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
        
        updated_user = UserRepository.update(db, user_id, user_update)
        return updated_user

    @staticmethod
    def delete_user(db: Session, user_id: int) -> None:
        """
        Delete a user by ID.
        
        Args:
            db: Database session.
            user_id: User's unique identifier.
            
        Raises:
            HTTPException: If user not found.
        """
        success = UserRepository.delete(db, user_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
