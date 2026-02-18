from sqlalchemy.orm import Session
from app.models.ticket import Ticket

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_ticket(self, ticket_id: int) -> Ticket | None:
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def get_tickets(self) -> list[Ticket]:
        return self.db.query(Ticket).all()

    def create_ticket(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
