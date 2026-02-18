from typing import List
from sqlalchemy.orm import Session
from ticket_management.db.models.ticket import Ticket
from ticket_management.schemas.ticket import TicketCreate, TicketUpdate
from ticket_management.repositories.ticket_repository import TicketRepository

class TicketService:
    def __init__(self, db: Session):
        self.db = db
        self.ticket_repository = TicketRepository(db)

    def create_ticket(self, ticket_create: TicketCreate) -> Ticket:
        return self.ticket_repository.create(ticket_create)

    def get_ticket(self, ticket_id: int) -> Ticket:
        return self.ticket_repository.get(ticket_id)

    def get_all_tickets(self) -> List[Ticket]:
        return self.ticket_repository.get_all()

    def update_ticket(self, ticket_id: int, ticket_update: TicketUpdate) -> Ticket:
        return self.ticket_repository.update(ticket_id, ticket_update)

    def delete_ticket(self, ticket_id: int) -> None:
        self.ticket_repository.delete(ticket_id)