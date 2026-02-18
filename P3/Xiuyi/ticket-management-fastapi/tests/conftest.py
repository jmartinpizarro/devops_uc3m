import pytest

@pytest.fixture(scope="session")
def test_client():
    from src.ticket_management.main import app
    with TestClient(app) as client:
        yield client