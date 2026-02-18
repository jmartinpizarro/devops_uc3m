from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserRead

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreate) -> UserRead:
        user = self.repository.create_user(user_data)
        return UserRead.from_orm(user)

    def get_user(self, user_id: int) -> UserRead | None:
        user = self.repository.get_user(user_id)
        return UserRead.from_orm(user) if user else None

    def get_users(self) -> list[UserRead]:
        users = self.repository.get_users()
        return [UserRead.from_orm(u) for u in users]
