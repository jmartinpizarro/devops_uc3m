from sqlalchemy.orm import Session
from ticket_management.db.models.user import User
from ticket_management.repositories.base import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(self.model).filter(self.model.id == user_id).first()

    def get_all_users(self) -> list[User]:
        return self.db.query(self.model).all()

    def create_user(self, user_data: dict) -> User:
        user = self.model(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, user_data: dict) -> User:
        user = self.get_user_by_id(user_id)
        for key, value in user_data.items():
            setattr(user, key, value)
        self.db.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        self.db.delete(user)
        self.db.commit()