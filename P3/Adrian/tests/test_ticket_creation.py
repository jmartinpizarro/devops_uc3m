import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_ticket():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        # First create a user
        user_response = await client.post("/users", json={"name": "Test User", "email": "test@example.com"})
        assert user_response.status_code == 200
        user_data = user_response.json()

        # Then create a ticket
        ticket_response = await client.post("/tickets", json={
            "author_id": user_data["id"],
            "title": "Test Ticket",
            "description": "This is a test ticket",
            "tags": ["test", "example"]
        })
        assert ticket_response.status_code == 200
        ticket_data = ticket_response.json()
        assert ticket_data["title"] == "Test Ticket"
        assert ticket_data["author_id"] == user_data["id"]