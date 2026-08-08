from fastapi import APIRouter
from v1.health.route import health_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)

