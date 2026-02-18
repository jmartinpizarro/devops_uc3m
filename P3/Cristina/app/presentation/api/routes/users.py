from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.presentation.api.deps import db_session, get_user_service
from app.application.services.users import UserService
from app.schemas.users import UserCreate, UserUpdate, UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(db_session), svc: UserService = Depends(get_user_service)):
    return svc.create(db, name=payload.name, email=payload.email)


@router.get("", response_model=list[UserOut])
def list_users(db: Session = Depends(db_session), svc: UserService = Depends(get_user_service)):
    return svc.list(db)


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(db_session), svc: UserService = Depends(get_user_service)):
    return svc.get(db, user_id)


@router.patch("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(db_session),
    svc: UserService = Depends(get_user_service),
):
    return svc.update(db, user_id, name=payload.name, email=payload.email)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(db_session), svc: UserService = Depends(get_user_service)):
    svc.delete(db, user_id)
    return None
