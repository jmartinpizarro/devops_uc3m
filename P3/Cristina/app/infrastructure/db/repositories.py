from __future__ import annotations

from typing import Sequence, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.ports import UserRepository, TicketRepository
from app.infrastructure.db.models import UserModel, TicketModel


class SqlAlchemyUserRepository(UserRepository):
    def create(self, db: Session, *, name: str, email: str) -> UserModel:
        user = UserModel(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get(self, db: Session, user_id: int) -> Optional[UserModel]:
        return db.get(UserModel, user_id)

    def list(self, db: Session) -> Sequence[UserModel]:
        return list(db.scalars(select(UserModel).order_by(UserModel.id)).all())

    def update(self, db: Session, user: UserModel, *, name: str | None, email: str | None) -> UserModel:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user: UserModel) -> None:
        db.delete(user)
        db.commit()


class SqlAlchemyTicketRepository(TicketRepository):
    def create(self, db: Session, *, author_id: int, title: str, description: str, tags: list[str]) -> TicketModel:
        ticket = TicketModel(author_id=author_id, title=title, description=description, tags=tags)
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    def get(self, db: Session, ticket_id: int) -> Optional[TicketModel]:
        return db.get(TicketModel, ticket_id)

    def list(self, db: Session) -> Sequence[TicketModel]:
        return list(db.scalars(select(TicketModel).order_by(TicketModel.id)).all())

    def update(
        self,
        db: Session,
        ticket: TicketModel,
        *,
        title: str | None,
        description: str | None,
        tags: list[str] | None,
    ) -> TicketModel:
        if title is not None:
            ticket.title = title
        if description is not None:
            ticket.description = description
        if tags is not None:
            ticket.tags = tags
        db.commit()
        db.refresh(ticket)
        return ticket

    def delete(self, db: Session, ticket: TicketModel) -> None:
        db.delete(ticket)
        db.commit()
