from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.ticket_repository import TicketRepository
from app.domain.services.ticket_service import TicketService
from app.presentation.schemas.ticket_schemas import Ticket, TicketCreate, TicketUpdate

router = APIRouter()

def get_ticket_service(db: Session = Depends(get_db)):
    ticket_repo = TicketRepository(db)
    return TicketService(ticket_repo)

@router.get("/tickets", response_model=list[Ticket])
def read_tickets(service: TicketService = Depends(get_ticket_service)):
    return service.get_tickets()

@router.get("/tickets/{ticket_id}", response_model=Ticket)
def read_ticket(ticket_id: int, service: TicketService = Depends(get_ticket_service)):
    ticket = service.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.post("/tickets", response_model=Ticket)
def create_ticket(ticket: TicketCreate, service: TicketService = Depends(get_ticket_service)):
    return service.create_ticket(ticket.author_id, ticket.title, ticket.description, ticket.tags)

@router.put("/tickets/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, ticket: TicketUpdate, service: TicketService = Depends(get_ticket_service)):
    updated_ticket = service.update_ticket(ticket_id, ticket.title, ticket.description, ticket.tags)
    if not updated_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated_ticket

@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, service: TicketService = Depends(get_ticket_service)):
    deleted_ticket = service.delete_ticket(ticket_id)
    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted"}