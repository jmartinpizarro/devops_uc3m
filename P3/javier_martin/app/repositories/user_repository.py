"""User repository for database operations."""

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    """Repository for User entity database operations."""

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """
        Retrieve all users with pagination.
        
        Args:
            db: Database session.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            
        Returns:
            List of User objects.
        """
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        """
        Retrieve a user by ID.
        
        Args:
            db: Database session.
            user_id: User's unique identifier.
            
        Returns:
            User object if found, None otherwise.
        """
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        """
        Retrieve a user by email.
        
        Args:
            db: Database session.
            email: User's email address.
            
        Returns:
            User object if found, None otherwise.
        """
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create(db: Session, user: UserCreate) -> User:
        """
        Create a new user.
        
        Args:
            db: Database session.
            user: User data for creation.
            
        Returns:
            Created User object.
        """
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """
        Update an existing user.
        
        Args:
            db: Database session.
            user_id: User's unique identifier.
            user_update: User data for update.
            
        Returns:
            Updated User object if found, None otherwise.
        """
        db_user = UserRepository.get_by_id(db, user_id)
        if not db_user:
            return None
        
        update_data = user_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete(db: Session, user_id: int) -> bool:
        """
        Delete a user by ID.
        
        Args:
            db: Database session.
            user_id: User's unique identifier.
            
        Returns:
            True if deleted successfully, False otherwise.
        """
        db_user = UserRepository.get_by_id(db, user_id)
        if not db_user:
            return False
        
        db.delete(db_user)
        db.commit()
        return True
