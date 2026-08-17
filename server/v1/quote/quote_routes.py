from v1.quote.dto.get_random_quote_res import GetRandomQuoteRes
from v1.quote.quote_service import QuoteService
from v1.quote.quote_dependencies import get_quote_service
from fastapi import APIRouter, Depends
from v1.quote.types.quote import Quote

quote_router = APIRouter(prefix="/quote")

@quote_router.get("/")
def get_quote(service: QuoteService = Depends(get_quote_service)) -> GetRandomQuoteRes:
    quote: Quote = service.get_random_quote()
    return {"quote": quote}