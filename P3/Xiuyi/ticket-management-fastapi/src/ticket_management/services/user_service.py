from typing import List
from sqlalchemy.orm import Session
from ticket_management.db.models.user import User
from ticket_management.schemas.user import UserCreate, UserUpdate
from ticket_management.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def create_user(self, user_create: UserCreate) -> User:
        user = User(**user_create.dict())
        return self.user_repository.create(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get(user_id)

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        user = self.user_repository.get(user_id)
        if user:
            for key, value in user_update.dict(exclude_unset=True).items():
                setattr(user, key, value)
            return self.user_repository.update(user)
        return None

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete(user_id)

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all()