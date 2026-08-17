from typing import List
from v1.quote.quote_dao import QuoteDao
from v1.quote.types.quote import Quote
import random

class QuoteService:
    def __init__(self, quote_dao: QuoteDao):
        self.quote_dao = quote_dao
    
    def get_random_quote(self) -> Quote:
        quotes: List[Quote] = self.quote_dao.get_all_quotes()
        random_quote = random.choice(quotes)
        return random_quote