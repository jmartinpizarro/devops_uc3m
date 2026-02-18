from sqlalchemy.orm import Session
from ticket_management.db.models.ticket import Ticket
from ticket_management.schemas.ticket import TicketCreate, TicketUpdate

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, ticket: TicketCreate) -> Ticket:
        db_ticket = Ticket(**ticket.dict())
        self.db.add(db_ticket)
        self.db.commit()
        self.db.refresh(db_ticket)
        return db_ticket

    def get_ticket(self, ticket_id: int) -> Ticket:
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def update_ticket(self, ticket_id: int, ticket: TicketUpdate) -> Ticket:
        db_ticket = self.get_ticket(ticket_id)
        if db_ticket:
            for key, value in ticket.dict(exclude_unset=True).items():
                setattr(db_ticket, key, value)
            self.db.commit()
            self.db.refresh(db_ticket)
        return db_ticket

    def delete_ticket(self, ticket_id: int) -> bool:
        db_ticket = self.get_ticket(ticket_id)
        if db_ticket:
            self.db.delete(db_ticket)
            self.db.commit()
            return True
        return False

    def get_all_tickets(self):
        return self.db.query(Ticket).all()