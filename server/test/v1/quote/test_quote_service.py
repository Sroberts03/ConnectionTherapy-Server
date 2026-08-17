import pytest
from unittest.mock import MagicMock
from v1.quote.quote_service import QuoteService
from v1.quote.types.quote import Quote

def test_get_random_quote():
    # Arrange
    mock_dao = MagicMock()
    # Provide a list of fake quotes
    fake_quotes = [
        Quote(id=1, text="Test Quote 1", author="Author 1"),
        Quote(id=2, text="Test Quote 2", author="Author 2")
    ]
    mock_dao.get_all_quotes.return_value = fake_quotes
    
    # Inject the mock DAO into the service
    service = QuoteService(quote_dao=mock_dao)
    
    # Act
    result = service.get_random_quote()
    
    # Assert
    # We expect the result to be one of the quotes in our fake list
    assert result in fake_quotes
    mock_dao.get_all_quotes.assert_called_once()
