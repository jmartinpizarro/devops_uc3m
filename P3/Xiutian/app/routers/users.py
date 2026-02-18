
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserRead
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repository(db=Depends(get_db)):
    return UserRepository(db)

def get_user_service(repo=Depends(get_user_repository)):
    return UserService(repo)

@router.post("/users", response_model=UserRead)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=list[UserRead])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()
