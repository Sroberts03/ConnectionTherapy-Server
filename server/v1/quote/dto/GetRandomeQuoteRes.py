from v1.quote.types.Quote import Quote
from pydantic import BaseModel

class GetRandomeQuoteRes(BaseModel):
    quote: Quote
