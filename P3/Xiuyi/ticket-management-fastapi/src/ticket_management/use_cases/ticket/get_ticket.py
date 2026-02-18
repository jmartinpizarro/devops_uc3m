from ticket_management.repositories.ticket_repository import TicketRepository
from ticket_management.schemas.ticket import TicketResponse
from ticket_management.db.models.ticket import Ticket

class GetTicket:
    def __init__(self, ticket_repository: TicketRepository):
        self.ticket_repository = ticket_repository

    def execute(self, ticket_id: int) -> TicketResponse:
        ticket: Ticket = self.ticket_repository.get(ticket_id)
        if not ticket:
            raise ValueError("Ticket not found")
        return TicketResponse.from_orm(ticket)