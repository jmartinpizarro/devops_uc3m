from ticket_management.repositories.ticket_repository import TicketRepository
from ticket_management.schemas.ticket import TicketDeleteResponse
from fastapi import HTTPException, Depends

async def delete_ticket(ticket_id: int, ticket_repository: TicketRepository = Depends()):
    ticket = await ticket_repository.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    await ticket_repository.delete_ticket(ticket_id)
    return TicketDeleteResponse(message="Ticket deleted successfully")