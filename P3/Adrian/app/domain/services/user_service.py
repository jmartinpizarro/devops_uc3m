from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.models.user import User

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_users(self):
        return self.user_repo.get_all()

    def get_user(self, user_id: int):
        return self.user_repo.get_by_id(user_id)

    def create_user(self, name: str, email: str):
        user = User(name=name, email=email)
        return self.user_repo.create(user)

    def update_user(self, user_id: int, name: str = None, email: str = None):
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        return self.user_repo.update(user_id, data)

    def delete_user(self, user_id: int):
        return self.user_repo.delete(user_id)