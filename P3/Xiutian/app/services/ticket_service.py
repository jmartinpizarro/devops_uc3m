from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import TicketCreate, TicketRead

class TicketService:
    def __init__(self, repository: TicketRepository):
        self.repository = repository

    def create_ticket(self, ticket_data: TicketCreate) -> TicketRead:
        ticket = self.repository.create_ticket(ticket_data)
        return TicketRead.from_orm(ticket)

    def get_ticket(self, ticket_id: int) -> TicketRead | None:
        ticket = self.repository.get_ticket(ticket_id)
        return TicketRead.from_orm(ticket) if ticket else None

    def get_tickets(self) -> list[TicketRead]:
        tickets = self.repository.get_tickets()
        return [TicketRead.from_orm(t) for t in tickets]
