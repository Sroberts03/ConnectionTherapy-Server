from fastapi import APIRouter
from v1.health.route import health_router
from v1.quote.quote_routes import quote_router
from v1.pillars.pillar_routes import pillar_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(quote_router)
api_router.include_router(pillar_router)

