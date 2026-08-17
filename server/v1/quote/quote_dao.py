from ast import Dict
from v1.quote.types.quote import Quote
from typing import List

class QuoteDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_quotes(self) -> List[Quote]:
        response = self.db_connection.table("quotes") \
            .select("*") \
            .eq("approved", True) \
            .execute()
        return [Quote(**quote) for quote in response.data]

        