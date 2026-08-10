from v1.quote.quote_service import QuoteService
from v1.quote.quote_dao import QuoteDao
from v1.database import supabase_client

quote_dao = QuoteDao(db_connection=supabase_client)
quote_service = QuoteService(quote_dao=quote_dao)