from app.infrastructure.repositories.ticket_repository import TicketRepository
from app.domain.models.ticket import Ticket

class TicketService:
    def __init__(self, ticket_repo: TicketRepository):
        self.ticket_repo = ticket_repo

    def get_tickets(self):
        return self.ticket_repo.get_all()

    def get_ticket(self, ticket_id: int):
        return self.ticket_repo.get_by_id(ticket_id)

    def create_ticket(self, author_id: int, title: str, description: str = None, tags: list = None):
        ticket = Ticket(author_id=author_id, title=title, description=description, tags=tags or [])
        return self.ticket_repo.create(ticket)

    def update_ticket(self, ticket_id: int, title: str = None, description: str = None, tags: list = None):
        data = {}
        if title:
            data["title"] = title
        if description is not None:
            data["description"] = description
        if tags is not None:
            data["tags"] = tags
        return self.ticket_repo.update(ticket_id, data)

    def delete_ticket(self, ticket_id: int):
        return self.ticket_repo.delete(ticket_id)