from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.services.user_service import UserService
from app.presentation.schemas.user_schemas import User, UserCreate, UserUpdate

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return UserService(user_repo)

@router.get("/users", response_model=list[User])
def read_users(service: UserService = Depends(get_user_service)):
    return service.get_users()

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=User)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user.name, user.email)

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, service: UserService = Depends(get_user_service)):
    updated_user = service.update_user(user_id, user.name, user.email)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    deleted_user = service.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}