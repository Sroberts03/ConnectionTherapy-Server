import pytest
from unittest.mock import MagicMock
from v1.quote.quote_dao import QuoteDao
from v1.quote.types.quote import Quote

def test_get_all_quotes():
    # Arrange
    mock_db = MagicMock()
    
    # We need to mock the chain: table("quotes").select("*").eq("approved", True).execute()
    mock_table = MagicMock()
    mock_select = MagicMock()
    mock_eq = MagicMock()
    mock_execute = MagicMock()
    
    # Set up the chain
    mock_db.table.return_value = mock_table
    mock_table.select.return_value = mock_select
    mock_select.eq.return_value = mock_eq
    mock_eq.execute.return_value = mock_execute
    
    # Define what the final .execute() should return
    # Supabase returns an object with a .data attribute containing a list of dictionaries
    mock_execute.data = [
        {"id": 1, "text": "DB Quote 1", "author": "DB Author 1"},
        {"id": 2, "text": "DB Quote 2", "author": "DB Author 2"}
    ]
    
    # Inject the mock DB into the DAO
    dao = QuoteDao(db_connection=mock_db)
    
    # Act
    results = dao.get_all_quotes()
    
    # Assert
    assert len(results) == 2
    assert isinstance(results[0], Quote)
    assert results[0].id == 1
    assert results[0].text == "DB Quote 1"
    
    # Verify the chain was called correctly
    mock_db.table.assert_called_once_with("quotes")
    mock_table.select.assert_called_once_with("*")
    mock_select.eq.assert_called_once_with("approved", True)
    mock_eq.execute.assert_called_once()
