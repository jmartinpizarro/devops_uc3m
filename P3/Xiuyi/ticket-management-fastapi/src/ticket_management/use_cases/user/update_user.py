from ticket_management.repositories.user_repository import UserRepository
from ticket_management.schemas.user import UserUpdate
from ticket_management.services.user_service import UserService

class UpdateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int, user_update: UserUpdate):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        updated_user = self.user_repository.update_user(user_id, user_update)
        return updated_user