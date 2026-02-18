# Ticket Management API

A FastAPI application for managing users and tickets using Clean Architecture.

## Features

- CRUD operations for Users and Tickets
- PostgreSQL database with SQLAlchemy
- Alembic migrations
- OpenAPI documentation at `/docs`
- Docker support

## Setup

### Prerequisites

- Python 3.11+
- Docker and Docker Compose

### Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   pip install -e .[dev]
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```
5. Run database migrations:
   ```bash
   alembic upgrade head
   ```
6. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Docker

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

The API will be available at `http://localhost:8000` and documentation at `http://localhost:8000/docs`.

## Testing

Run tests with pytest:
```bash
pytest
```

## API Endpoints

- `GET /users` - List all users
- `POST /users` - Create a user
- `GET /users/{id}` - Get user by ID
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

- `GET /tickets` - List all tickets
- `POST /tickets` - Create a ticket
- `GET /tickets/{id}` - Get ticket by ID
- `PUT /tickets/{id}` - Update ticket
- `DELETE /tickets/{id}` - Delete ticket