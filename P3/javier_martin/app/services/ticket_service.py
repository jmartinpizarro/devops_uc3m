"""Ticket service with business logic."""

from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException, status

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate
from app.repositories.ticket_repository import TicketRepository
from app.repositories.user_repository import UserRepository


class TicketService:
    """Service layer for Ticket business logic."""

    @staticmethod
    def get_all_tickets(db: Session, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Retrieve all tickets with pagination.
        
        Args:
            db: Database session.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            
        Returns:
            List of Ticket objects.
        """
        return TicketRepository.get_all(db, skip, limit)

    @staticmethod
    def get_ticket_by_id(db: Session, ticket_id: int) -> Ticket:
        """
        Retrieve a ticket by ID.
        
        Args:
            db: Database session.
            ticket_id: Ticket's unique identifier.
            
        Returns:
            Ticket object.
            
        Raises:
            HTTPException: If ticket not found.
        """
        ticket = TicketRepository.get_by_id(db, ticket_id)
        if not ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ticket with id {ticket_id} not found"
            )
        return ticket

    @staticmethod
    def get_tickets_by_author(db: Session, author_id: int, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Retrieve all tickets by author.
        
        Args:
            db: Database session.
            author_id: Author's user ID.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            
        Returns:
            List of Ticket objects.
            
        Raises:
            HTTPException: If author not found.
        """
        # Verify author exists
        author = UserRepository.get_by_id(db, author_id)
        if not author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {author_id} not found"
            )
        
        return TicketRepository.get_by_author(db, author_id, skip, limit)

    @staticmethod
    def create_ticket(db: Session, ticket: TicketCreate) -> Ticket:
        """
        Create a new ticket.
        
        Args:
            db: Database session.
            ticket: Ticket data for creation.
            
        Returns:
            Created Ticket object.
            
        Raises:
            HTTPException: If author not found.
        """
        # Verify author exists
        author = UserRepository.get_by_id(db, ticket.author_id)
        if not author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {ticket.author_id} not found"
            )
        
        return TicketRepository.create(db, ticket)

    @staticmethod
    def update_ticket(db: Session, ticket_id: int, ticket_update: TicketUpdate) -> Ticket:
        """
        Update an existing ticket.
        
        Args:
            db: Database session.
            ticket_id: Ticket's unique identifier.
            ticket_update: Ticket data for update.
            
        Returns:
            Updated Ticket object.
            
        Raises:
            HTTPException: If ticket not found.
        """
        # Check if ticket exists
        existing_ticket = TicketRepository.get_by_id(db, ticket_id)
        if not existing_ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ticket with id {ticket_id} not found"
            )
        
        updated_ticket = TicketRepository.update(db, ticket_id, ticket_update)
        return updated_ticket

    @staticmethod
    def delete_ticket(db: Session, ticket_id: int) -> None:
        """
        Delete a ticket by ID.
        
        Args:
            db: Database session.
            ticket_id: Ticket's unique identifier.
            
        Raises:
            HTTPException: If ticket not found.
        """
        success = TicketRepository.delete(db, ticket_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ticket with id {ticket_id} not found"
            )
