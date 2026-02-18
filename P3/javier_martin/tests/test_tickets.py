"""Integration tests for Ticket endpoints."""

from fastapi.testclient import TestClient


def test_create_ticket(client: TestClient):
    """Test ticket creation endpoint."""
    # First create a user
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]
    
    # Create a ticket
    ticket_data = {
        "title": "Bug in login page",
        "description": "Users cannot login with valid credentials",
        "tags": ["bug", "urgent", "login"],
        "author_id": user_id
    }
    
    response = client.post("/tickets/", json=ticket_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == ticket_data["title"]
    assert data["description"] == ticket_data["description"]
    assert data["tags"] == ticket_data["tags"]
    assert data["author_id"] == user_id
    assert "id" in data
    assert "created_at" in data


def test_get_ticket(client: TestClient):
    """Test getting a ticket by ID."""
    # Create user and ticket
    user_data = {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]
    
    ticket_data = {
        "title": "Feature request",
        "description": "Add dark mode support",
        "tags": ["feature", "ui"],
        "author_id": user_id
    }
    create_response = client.post("/tickets/", json=ticket_data)
    ticket_id = create_response.json()["id"]
    
    # Get the ticket
    response = client.get(f"/tickets/{ticket_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == ticket_id
    assert data["title"] == ticket_data["title"]


def test_get_nonexistent_ticket(client: TestClient):
    """Test getting a ticket that doesn't exist."""
    response = client.get("/tickets/999")
    
    assert response.status_code == 404


def test_get_all_tickets(client: TestClient):
    """Test getting all tickets."""
    # Create user
    user_data = {
        "name": "Test User",
        "email": "test@example.com"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]
    
    # Create multiple tickets
    for i in range(3):
        ticket_data = {
            "title": f"Ticket {i+1}",
            "description": f"Description for ticket {i+1}",
            "tags": [f"tag{i+1}"],
            "author_id": user_id
        }
        client.post("/tickets/", json=ticket_data)
    
    # Get all tickets
    response = client.get("/tickets/")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


def test_get_tickets_by_author(client: TestClient):
    """Test filtering tickets by author."""
    # Create two users
    user1_data = {"name": "User 1", "email": "user1@example.com"}
    user2_data = {"name": "User 2", "email": "user2@example.com"}
    
    user1_response = client.post("/users/", json=user1_data)
    user2_response = client.post("/users/", json=user2_data)
    
    user1_id = user1_response.json()["id"]
    user2_id = user2_response.json()["id"]
    
    # Create tickets for both users
    client.post("/tickets/", json={
        "title": "User 1 Ticket",
        "description": "Description",
        "tags": [],
        "author_id": user1_id
    })
    
    client.post("/tickets/", json={
        "title": "User 2 Ticket",
        "description": "Description",
        "tags": [],
        "author_id": user2_id
    })
    
    # Get tickets by user1
    response = client.get(f"/tickets/?author_id={user1_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["author_id"] == user1_id


def test_update_ticket(client: TestClient):
    """Test updating a ticket."""
    # Create user and ticket
    user_data = {
        "name": "Bob Johnson",
        "email": "bob.johnson@example.com"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]
    
    ticket_data = {
        "title": "Original Title",
        "description": "Original description",
        "tags": ["original"],
        "author_id": user_id
    }
    create_response = client.post("/tickets/", json=ticket_data)
    ticket_id = create_response.json()["id"]
    
    # Update the ticket
    update_data = {
        "title": "Updated Title",
        "tags": ["updated", "modified"]
    }
    response = client.put(f"/tickets/{ticket_id}", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["tags"] == update_data["tags"]
    assert data["description"] == ticket_data["description"]  # Unchanged


def test_delete_ticket(client: TestClient):
    """Test deleting a ticket."""
    # Create user and ticket
    user_data = {
        "name": "Alice Williams",
        "email": "alice.williams@example.com"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]
    
    ticket_data = {
        "title": "Ticket to delete",
        "description": "This ticket will be deleted",
        "tags": [],
        "author_id": user_id
    }
    create_response = client.post("/tickets/", json=ticket_data)
    ticket_id = create_response.json()["id"]
    
    # Delete the ticket
    response = client.delete(f"/tickets/{ticket_id}")
    
    assert response.status_code == 204
    
    # Verify ticket is deleted
    get_response = client.get(f"/tickets/{ticket_id}")
    assert get_response.status_code == 404


def test_create_ticket_nonexistent_author(client: TestClient):
    """Test creating a ticket with non-existent author."""
    ticket_data = {
        "title": "Invalid ticket",
        "description": "This ticket has no valid author",
        "tags": [],
        "author_id": 999
    }
    
    response = client.post("/tickets/", json=ticket_data)
    
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
