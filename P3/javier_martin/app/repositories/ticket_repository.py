"""Ticket repository for database operations."""

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate


class TicketRepository:
    """Repository for Ticket entity database operations."""

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Retrieve all tickets with pagination.
        
        Args:
            db: Database session.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            
        Returns:
            List of Ticket objects.
        """
        return db.query(Ticket).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, ticket_id: int) -> Optional[Ticket]:
        """
        Retrieve a ticket by ID.
        
        Args:
            db: Database session.
            ticket_id: Ticket's unique identifier.
            
        Returns:
            Ticket object if found, None otherwise.
        """
        return db.query(Ticket).filter(Ticket.id == ticket_id).first()

    @staticmethod
    def get_by_author(db: Session, author_id: int, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Retrieve all tickets by author.
        
        Args:
            db: Database session.
            author_id: Author's user ID.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            
        Returns:
            List of Ticket objects.
        """
        return db.query(Ticket).filter(Ticket.author_id == author_id).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, ticket: TicketCreate) -> Ticket:
        """
        Create a new ticket.
        
        Args:
            db: Database session.
            ticket: Ticket data for creation.
            
        Returns:
            Created Ticket object.
        """
        db_ticket = Ticket(**ticket.model_dump())
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    @staticmethod
    def update(db: Session, ticket_id: int, ticket_update: TicketUpdate) -> Optional[Ticket]:
        """
        Update an existing ticket.
        
        Args:
            db: Database session.
            ticket_id: Ticket's unique identifier.
            ticket_update: Ticket data for update.
            
        Returns:
            Updated Ticket object if found, None otherwise.
        """
        db_ticket = TicketRepository.get_by_id(db, ticket_id)
        if not db_ticket:
            return None
        
        update_data = ticket_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_ticket, field, value)
        
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    @staticmethod
    def delete(db: Session, ticket_id: int) -> bool:
        """
        Delete a ticket by ID.
        
        Args:
            db: Database session.
            ticket_id: Ticket's unique identifier.
            
        Returns:
            True if deleted successfully, False otherwise.
        """
        db_ticket = TicketRepository.get_by_id(db, ticket_id)
        if not db_ticket:
            return False
        
        db.delete(db_ticket)
        db.commit()
        return True
