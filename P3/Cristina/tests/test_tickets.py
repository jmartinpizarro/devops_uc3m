from __future__ import annotations


def test_create_ticket(client):
    # Primero creamos un usuario (autor)
    user_resp = client.post(
        "/api/v1/users",
        json={"name": "Alice", "email": "alice@example.com"},
    )
    assert user_resp.status_code == 201
    user_id = user_resp.json()["id"]

    # Creamos ticket
    ticket_resp = client.post(
        "/api/v1/tickets",
        json={
            "author_id": user_id,
            "title": "No puedo iniciar sesión",
            "description": "Me da error 500 al loguearme.",
            "tags": ["login", "bug"],
        },
    )
    assert ticket_resp.status_code == 201
    body = ticket_resp.json()
    assert body["author_id"] == user_id
    assert body["title"] == "No puedo iniciar sesión"
    assert body["tags"] == ["login", "bug"]
    assert "created_at" in body
