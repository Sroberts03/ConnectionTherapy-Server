from v1.quote.dto.GetRandomeQuoteRes import GetRandomeQuoteRes
from v1.quote.types.Quote import Quote
from fastapi import APIRouter
from v1.config import quote_service

quote_router = APIRouter(prefix="/quote")

@quote_router.get("/")
def get_quote() -> GetRandomeQuoteRes:
    quote: Quote = quote_service.get_random_quote()
    return {"quote": quote}