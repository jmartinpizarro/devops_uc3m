from ticket_management.repositories.user_repository import UserRepository
from ticket_management.schemas.user import UserSchema
from ticket_management.db.models.user import User

class GetUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> UserSchema:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return UserSchema.from_orm(user)