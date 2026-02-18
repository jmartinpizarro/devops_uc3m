"""Ticket API endpoints."""

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketResponse
from app.services.ticket_service import TicketService

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.get(
    "/",
    response_model=List[TicketResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all tickets",
    description="Retrieve a list of all tickets with optional filtering by author and pagination support."
)
def get_tickets(
    author_id: Optional[int] = Query(None, description="Filter tickets by author ID"),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[TicketResponse]:
    """
    Retrieve all tickets or filter by author.
    
    Args:
        author_id: Optional author ID to filter tickets.
        skip: Number of records to skip (for pagination).
        limit: Maximum number of records to return (for pagination).
        db: Database session dependency.
        
    Returns:
        List of tickets.
        
    Raises:
        HTTPException: 404 if author not found (when filtering by author).
    """
    if author_id:
        tickets = TicketService.get_tickets_by_author(db, author_id, skip=skip, limit=limit)
    else:
        tickets = TicketService.get_all_tickets(db, skip=skip, limit=limit)
    return tickets


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse,
    status_code=status.HTTP_200_OK,
    summary="Get ticket by ID",
    description="Retrieve a specific ticket by its unique identifier."
)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)) -> TicketResponse:
    """
    Retrieve a ticket by ID.
    
    Args:
        ticket_id: Ticket's unique identifier.
        db: Database session dependency.
        
    Returns:
        Ticket data.
        
    Raises:
        HTTPException: 404 if ticket not found.
    """
    ticket = TicketService.get_ticket_by_id(db, ticket_id)
    return ticket


@router.post(
    "/",
    response_model=TicketResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new ticket",
    description="Create a new ticket with the provided information."
)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)) -> TicketResponse:
    """
    Create a new ticket.
    
    Args:
        ticket: Ticket data for creation.
        db: Database session dependency.
        
    Returns:
        Created ticket data.
        
    Raises:
        HTTPException: 404 if author not found.
    """
    new_ticket = TicketService.create_ticket(db, ticket)
    return new_ticket


@router.put(
    "/{ticket_id}",
    response_model=TicketResponse,
    status_code=status.HTTP_200_OK,
    summary="Update a ticket",
    description="Update an existing ticket's information."
)
def update_ticket(
    ticket_id: int,
    ticket_update: TicketUpdate,
    db: Session = Depends(get_db)
) -> TicketResponse:
    """
    Update an existing ticket.
    
    Args:
        ticket_id: Ticket's unique identifier.
        ticket_update: Ticket data for update.
        db: Database session dependency.
        
    Returns:
        Updated ticket data.
        
    Raises:
        HTTPException: 404 if ticket not found.
    """
    updated_ticket = TicketService.update_ticket(db, ticket_id, ticket_update)
    return updated_ticket


@router.delete(
    "/{ticket_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a ticket",
    description="Delete a ticket by its unique identifier."
)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)) -> None:
    """
    Delete a ticket.
    
    Args:
        ticket_id: Ticket's unique identifier.
        db: Database session dependency.
        
    Raises:
        HTTPException: 404 if ticket not found.
    """
    TicketService.delete_ticket(db, ticket_id)
