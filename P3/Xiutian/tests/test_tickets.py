import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_ticket():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tickets", json={
            "title": "Test Ticket",
            "description": "Test Description",
            "tags": ["test", "example"],
            "author_id": 1
        })
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test Ticket"
