import pytest
from fastapi.testclient import TestClient
from src.ticket_management.main import app
from src.ticket_management.db.models.user import User
from src.ticket_management.db.session import get_db
from sqlalchemy.orm import Session

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def db_session():
    db = next(get_db())
    yield db

def test_create_user(client, db_session):
    response = client.post("/api/v1/users/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "test@example.com"

def test_get_user(client, db_session):
    response = client.post("/api/v1/users/", json={"name": "Test User", "email": "test@example.com"})
    user_id = response.json()["id"]
    
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_update_user(client, db_session):
    response = client.post("/api/v1/users/", json={"name": "Test User", "email": "test@example.com"})
    user_id = response.json()["id"]
    
    response = client.put(f"/api/v1/users/{user_id}", json={"name": "Updated User", "email": "updated@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

def test_delete_user(client, db_session):
    response = client.post("/api/v1/users/", json={"name": "Test User", "email": "test@example.com"})
    user_id = response.json()["id"]
    
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404