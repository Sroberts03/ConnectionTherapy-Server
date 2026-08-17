from fastapi import Depends
from v1.database import supabase_client
from v1.quote.quote_dao import QuoteDao
from v1.quote.quote_service import QuoteService
from v1.database import get_db

def get_quote_dao(db = Depends(get_db)) -> QuoteDao:
    return QuoteDao(db_connection=db)

def get_quote_service(dao: QuoteDao = Depends(get_quote_dao)) -> QuoteService:
    return QuoteService(quote_dao=dao)
