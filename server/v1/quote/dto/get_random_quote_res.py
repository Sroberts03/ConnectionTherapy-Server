from v1.quote.types.quote import Quote
from pydantic import BaseModel

class GetRandomQuoteRes(BaseModel):
    quote: Quote
