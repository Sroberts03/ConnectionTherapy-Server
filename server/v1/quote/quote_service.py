from v1.quote.quote_dao import QuoteDao
from v1.quote.types.Quote import Quote
import random

class QuoteService:
    def __init__(self, quote_dao: QuoteDao):
        self.quote_dao = quote_dao
    
    def get_random_quote(self) -> Quote:
        quotes = self.quote_dao.get_all_quotes()
        random_quote_data = random.choice(quotes)
        return Quote(**random_quote_data)