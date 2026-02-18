from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence, Optional
from sqlalchemy.orm import Session

from app.infrastructure.db.models import UserModel, TicketModel


class UserRepository(ABC):
    @abstractmethod
    def create(self, db: Session, *, name: str, email: str) -> UserModel: ...

    @abstractmethod
    def get(self, db: Session, user_id: int) -> Optional[UserModel]: ...

    @abstractmethod
    def list(self, db: Session) -> Sequence[UserModel]: ...

    @abstractmethod
    def update(self, db: Session, user: UserModel, *, name: str | None, email: str | None) -> UserModel: ...

    @abstractmethod
    def delete(self, db: Session, user: UserModel) -> None: ...


class TicketRepository(ABC):
    @abstractmethod
    def create(
        self,
        db: Session,
        *,
        author_id: int,
        title: str,
        description: str,
        tags: list[str],
    ) -> TicketModel: ...

    @abstractmethod
    def get(self, db: Session, ticket_id: int) -> Optional[TicketModel]: ...

    @abstractmethod
    def list(self, db: Session) -> Sequence[TicketModel]: ...

    @abstractmethod
    def update(
        self,
        db: Session,
        ticket: TicketModel,
        *,
        title: str | None,
        description: str | None,
        tags: list[str] | None,
    ) -> TicketModel: ...

    @abstractmethod
    def delete(self, db: Session, ticket: TicketModel) -> None: ...
