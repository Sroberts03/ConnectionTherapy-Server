import random

class QuoteDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_quotes(self):
        response = self.db_connection.table("quotes") \
            .select("*") \
            .eq("approved", True) \
            .execute()
        quotes = response.data
        return quotes


        