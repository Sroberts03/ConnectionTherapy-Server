from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from v1.quote.quote_routes import quote_router
from v1.quote.quote_dependencies import get_quote_service
from v1.quote.types.quote import Quote

# Create a test app and include our router
app = FastAPI()
app.include_router(quote_router)

client = TestClient(app)

def test_get_quote_route():
    # Arrange
    # We want to mock the service so we don't hit the real database
    mock_service = MagicMock()
    fake_quote = Quote(id=99, text="Route Test Quote", author="Route Test Author")
    mock_service.get_random_quote.return_value = fake_quote
    
    # Override the dependency in our FastAPI app
    app.dependency_overrides[get_quote_service] = lambda: mock_service
    
    # Act
    # Make a request to the route using the test client
    response = client.get("/quote/")
    
    # Assert
    assert response.status_code == 200
    
    # Check the JSON response format matches our GetRandomQuoteRes DTO
    json_data = response.json()
    assert "quote" in json_data
    assert json_data["quote"]["id"] == 99
    assert json_data["quote"]["text"] == "Route Test Quote"
    assert json_data["quote"]["author"] == "Route Test Author"
    
    # Verify our mock service was actually called by the route
    mock_service.get_random_quote.assert_called_once()
    
    # Clean up overrides after test
    app.dependency_overrides.clear()
