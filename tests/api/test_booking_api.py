import pytest
import requests
import json

BASE_URL = "https://automationintesting.online"

def create_headers_with_cookie():
    """Authenticate and create headers with the session cookie."""
    auth_payload = {
        "username": "admin",
        "password": "password"
    }

    response = requests.post(f"{BASE_URL}/auth/login", json=auth_payload)
    assert response.status_code == 200, "Failed to authenticate. Check the credentials."


@pytest.fixture(scope="session")
def authenticate():
    """Fixture to return headers with the authentication token."""
    return create_headers_with_cookie()


@pytest.mark.api
def test_get_rooms(authenticate):
    """Test to retrieve all rooms."""
    response = requests.get(f"{BASE_URL}/room", headers=authenticate)
    assert response.status_code == 200, "Failed to retrieve rooms."
    assert isinstance(response.json(), dict), "Expected a list of rooms."
