# Ticket Management FastAPI

This project is a ticket management application built using FastAPI, following Clean Architecture principles. It provides a complete CRUD API for managing Users and Tickets, along with documentation via OpenAPI.

## Project Structure

```
ticket-management-fastapi
├── src
│   └── ticket_management
│       ├── __init__.py
│       ├── main.py
│       ├── api
│       │   ├── __init__.py
│       │   └── v1
│       │       ├── __init__.py
│       │       ├── routers
│       │       │   ├── users.py
│       │       │   └── tickets.py
│       │       └── deps.py
│       ├── core
│       │   ├── __init__.py
│       │   └── config.py
│       ├── db
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── session.py
│       │   └── models
│       │       ├── __init__.py
│       │       ├── user.py
│       │       └── ticket.py
│       ├── schemas
│       │   ├── __init__.py
│       │   ├── user.py
│       │   └── ticket.py
│       ├── repositories
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── user_repository.py
│       │   └── ticket_repository.py
│       ├── services
│       │   ├── __init__.py
│       │   ├── user_service.py
│       │   └── ticket_service.py
│       ├── use_cases
│       │   ├── user
│       │   │   ├── create_user.py
│       │   │   ├── get_user.py
│       │   │   ├── update_user.py
│       │   │   └── delete_user.py
│       │   └── ticket
│       │       ├── create_ticket.py
│       │       ├── get_ticket.py
│       │       ├── update_ticket.py
│       │       └── delete_ticket.py
│       └── utils
│           ├── __init__.py
│           └── pagination.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_users.py
│   └── test_tickets.py
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

## Features

- User Management: Create, Read, Update, and Delete users.
- Ticket Management: Create, Read, Update, and Delete tickets.
- OpenAPI Documentation: Automatically generated API documentation.
- Docker Support: Easily deployable using Docker.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ticket-management-fastapi
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   Copy `.env.example` to `.env` and update the values as needed.

### Running the Application

To run the application locally, execute:
```
uvicorn src.ticket_management.main:app --reload
```

### Docker

To build and run the application using Docker, execute:
```
docker-compose up --build
```

### API Documentation

The API documentation can be accessed at `http://localhost:8000/docs`.

## Testing

To run the tests, execute:
```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.