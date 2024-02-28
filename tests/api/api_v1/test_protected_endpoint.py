import pytest
from fastapi.testclient import TestClient
from app.main import app  # Ensure this imports your FastAPI app correctly
from unittest.mock import patch
from firebase_admin import auth

# Your FastAPI test client
client = TestClient(app)

@pytest.fixture
def mock_verify_id_token(mocker):
    """Fixture to mock Firebase Admin's verify_id_token method."""
    yield mocker.patch('firebase_admin.auth.verify_id_token', return_value={"uid": "test_user_id"})

@pytest.mark.asyncio
async def test_protected_endpoint(mock_verify_id_token):
    # Simulate a Firebase ID token being sent in the Authorization header
    test_token = "fakeToken"
    headers = {"Authorization": f"Bearer {test_token}"}
    
    response = client.get("/api/v1/posts/protected", headers=headers)

    print("Response JSON:", response.json())  # Print the response JSON to the console
    
    assert response.status_code == 200
    assert response.json() == {"message": "Protected route", "user": {"uid": "test_user_id"}}
