from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_scheduled_post():
    # Define a sample post request data
    sample_post_data = {
        "link": "https://example.com",
        "comment": "Check out this example.",
        "schedule_time": "2024-01-01T00:00:00.000Z"
    }
    
    # Send a POST request to the create scheduled post endpoint
    response = client.post("/api/v1/posts/schedule", json=sample_post_data)
    
    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    
    # Assert that the response data matches the request data
    response_data = response.json()
    assert response_data["link"] == sample_post_data["link"]
    assert response_data["comment"] == sample_post_data["comment"]
    # Ensure the 'id' field is returned, which indicates a database entry was created
    assert "id" in response_data
