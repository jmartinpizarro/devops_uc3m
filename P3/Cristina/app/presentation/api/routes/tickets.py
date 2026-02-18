from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.presentation.api.deps import db_session, get_ticket_service
from app.application.services.tickets import TicketService
from app.schemas.tickets import TicketCreate, TicketUpdate, TicketOut

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=TicketOut, status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate, db: Session = Depends(db_session), svc: TicketService = Depends(get_ticket_service)):
    return svc.create(db, author_id=payload.author_id, title=payload.title, description=payload.description, tags=payload.tags)


@router.get("", response_model=list[TicketOut])
def list_tickets(db: Session = Depends(db_session), svc: TicketService = Depends(get_ticket_service)):
    return svc.list(db)


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int, db: Session = Depends(db_session), svc: TicketService = Depends(get_ticket_service)):
    return svc.get(db, ticket_id)


@router.patch("/{ticket_id}", response_model=TicketOut)
def update_ticket(
    ticket_id: int,
    payload: TicketUpdate,
    db: Session = Depends(db_session),
    svc: TicketService = Depends(get_ticket_service),
):
    return svc.update(db, ticket_id, title=payload.title, description=payload.description, tags=payload.tags)


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: int, db: Session = Depends(db_session), svc: TicketService = Depends(get_ticket_service)):
    svc.delete(db, ticket_id)
    return None
