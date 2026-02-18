"""Integration tests for User endpoints."""

from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    """Test user creation endpoint."""
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    response = client.post("/users/", json=user_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert "id" in data


def test_get_user(client: TestClient):
    """Test getting a user by ID."""
    # First create a user
    user_data = {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    # Get the user
    response = client.get(f"/users/{user_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]


def test_get_nonexistent_user(client: TestClient):
    """Test getting a user that doesn't exist."""
    response = client.get("/users/999")
    
    assert response.status_code == 404


def test_update_user(client: TestClient):
    """Test updating a user."""
    # Create a user
    user_data = {
        "name": "Bob Johnson",
        "email": "bob.johnson@example.com"
    }
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    # Update the user
    update_data = {"name": "Robert Johnson"}
    response = client.put(f"/users/{user_id}", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["email"] == user_data["email"]


def test_delete_user(client: TestClient):
    """Test deleting a user."""
    # Create a user
    user_data = {
        "name": "Alice Williams",
        "email": "alice.williams@example.com"
    }
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    # Delete the user
    response = client.delete(f"/users/{user_id}")
    
    assert response.status_code == 204
    
    # Verify user is deleted
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404


def test_create_user_duplicate_email(client: TestClient):
    """Test creating a user with duplicate email."""
    user_data = {
        "name": "Test User",
        "email": "duplicate@example.com"
    }
    
    # Create first user
    client.post("/users/", json=user_data)
    
    # Try to create another user with the same email
    response = client.post("/users/", json=user_data)
    
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"].lower()
