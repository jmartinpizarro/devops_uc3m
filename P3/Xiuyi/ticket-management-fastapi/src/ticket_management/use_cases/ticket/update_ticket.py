from ticket_management.db.models.ticket import Ticket
from ticket_management.repositories.ticket_repository import TicketRepository
from ticket_management.schemas.ticket import TicketUpdate
from sqlalchemy.orm import Session

class UpdateTicket:
    def __init__(self, ticket_repository: TicketRepository):
        self.ticket_repository = ticket_repository

    def execute(self, ticket_id: int, ticket_update: TicketUpdate, db: Session) -> Ticket:
        ticket = self.ticket_repository.get_ticket_by_id(ticket_id, db)
        if not ticket:
            raise ValueError("Ticket not found")

        for key, value in ticket_update.dict(exclude_unset=True).items():
            setattr(ticket, key, value)

        self.ticket_repository.update_ticket(ticket, db)
        return ticket