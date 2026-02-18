from __future__ import annotations

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.domain.ports import UserRepository
from app.infrastructure.db.models import UserModel


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def create(self, db: Session, *, name: str, email: str) -> UserModel:
        try:
            return self.repo.create(db, name=name, email=email)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

    def get(self, db: Session, user_id: int) -> UserModel:
        user = self.repo.get(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def list(self, db: Session) -> list[UserModel]:
        return list(self.repo.list(db))

    def update(self, db: Session, user_id: int, *, name: str | None, email: str | None) -> UserModel:
        user = self.get(db, user_id)
        try:
            return self.repo.update(db, user, name=name, email=email)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

    def delete(self, db: Session, user_id: int) -> None:
        user = self.get(db, user_id)
        self.repo.delete(db, user)
