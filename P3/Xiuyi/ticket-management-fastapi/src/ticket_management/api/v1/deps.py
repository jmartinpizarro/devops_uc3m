from sqlalchemy.orm import Session
from ticket_management.db.session import get_db
from ticket_management.repositories.user_repository import UserRepository
from ticket_management.repositories.ticket_repository import TicketRepository

def get_user_repository(db: Session = next(get_db())) -> UserRepository:
    return UserRepository(db)

def get_ticket_repository(db: Session = next(get_db())) -> TicketRepository:
    return TicketRepository(db)