from fastapi import APIRouter, Depends, HTTPException
from app.schemas.ticket import TicketCreate, TicketRead
from app.services.ticket_service import TicketService
from app.repositories.ticket_repository import TicketRepository

router = APIRouter()

# Dependencia que crea un TicketService
def get_ticket_service() -> TicketService:
    repository = TicketRepository()
    return TicketService(repository)

@router.post("/tickets", response_model=TicketRead)
def create_ticket(ticket: TicketCreate, service: TicketService = Depends(get_ticket_service)):
    return service.create_ticket(ticket)

@router.get("/tickets/{ticket_id}", response_model=TicketRead)
def get_ticket(ticket_id: int, service: TicketService = Depends(get_ticket_service)):
    ticket = service.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.get("/tickets", response_model=list[TicketRead])
def get_tickets(service: TicketService = Depends(get_ticket_service)):
    return service.get_tickets()
