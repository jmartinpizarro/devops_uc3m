from datetime import datetime
from ticket_management.db.models.ticket import Ticket
from ticket_management.schemas.ticket import TicketCreate
from ticket_management.repositories.ticket_repository import TicketRepository

class CreateTicketUseCase:
    def __init__(self, ticket_repository: TicketRepository):
        self.ticket_repository = ticket_repository

    def execute(self, ticket_data: TicketCreate) -> Ticket:
        ticket = Ticket(
            title=ticket_data.title,
            description=ticket_data.description,
            creation_date=datetime.utcnow(),
            tags=ticket_data.tags,
        )
        return self.ticket_repository.create(ticket)