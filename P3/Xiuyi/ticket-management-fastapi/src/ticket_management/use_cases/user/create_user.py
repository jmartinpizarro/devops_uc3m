from sqlalchemy.orm import Session
from ticket_management.db.models.user import User
from ticket_management.schemas.user import UserCreate
from ticket_management.repositories.user_repository import UserRepository

class CreateUser:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def execute(self, user_create: UserCreate) -> User:
        user = User(**user_create.dict())
        return self.user_repository.create(user)