import pytest
from httpx import AsyncClient
from src.ticket_management.main import app

@pytest.mark.asyncio
async def test_create_ticket():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/tickets/", json={
            "title": "Test Ticket",
            "description": "This is a test ticket.",
            "tags": ["test", "ticket"]
        })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Ticket"

@pytest.mark.asyncio
async def test_get_ticket():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/tickets/1")
    assert response.status_code == 200
    assert "title" in response.json()

@pytest.mark.asyncio
async def test_update_ticket():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.put("/api/v1/tickets/1", json={
            "title": "Updated Ticket",
            "description": "This is an updated test ticket.",
            "tags": ["update", "ticket"]
        })
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Ticket"

@pytest.mark.asyncio
async def test_delete_ticket():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete("/api/v1/tickets/1")
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_get_all_tickets():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/tickets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)