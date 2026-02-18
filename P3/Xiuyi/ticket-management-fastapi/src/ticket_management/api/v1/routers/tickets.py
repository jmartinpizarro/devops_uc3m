from fastapi import APIRouter, HTTPException, Depends
from ticket_management.schemas.ticket import TicketCreate, TicketUpdate, Ticket
from ticket_management.services.ticket_service import TicketService
from ticket_management.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=Ticket)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return TicketService.create_ticket(db=db, ticket=ticket)

@router.get("/{ticket_id}", response_model=Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = TicketService.get_ticket(db=db, ticket_id=ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    updated_ticket = TicketService.update_ticket(db=db, ticket_id=ticket_id, ticket=ticket)
    if updated_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated_ticket

@router.delete("/{ticket_id}", response_model=dict)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    result = TicketService.delete_ticket(db=db, ticket_id=ticket_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"detail": "Ticket deleted successfully"}