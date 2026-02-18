from sqlalchemy.orm import Session
from ticket_management.db.models.user import User
from ticket_management.repositories.user_repository import UserRepository

class DeleteUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> None:
        user = self.user_repository.get_user_by_id(user_id)
        if user is None:
            raise ValueError("User not found")
        self.user_repository.delete_user(user)