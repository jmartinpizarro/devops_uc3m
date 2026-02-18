from sqlalchemy.orm import Session
from app.domain.models.ticket import Ticket

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Ticket).all()

    def get_by_id(self, ticket_id: int):
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def create(self, ticket: Ticket):
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def update(self, ticket_id: int, ticket_data: dict):
        ticket = self.get_by_id(ticket_id)
        if ticket:
            for key, value in ticket_data.items():
                setattr(ticket, key, value)
            self.db.commit()
            self.db.refresh(ticket)
        return ticket

    def delete(self, ticket_id: int):
        ticket = self.get_by_id(ticket_id)
        if ticket:
            self.db.delete(ticket)
            self.db.commit()
        return ticket