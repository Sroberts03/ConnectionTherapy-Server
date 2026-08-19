from v1.pillars.types.pillar import ConnectionPillar
from fastapi import APIRouter, Depends
from v1.pillars.dto.get_pillars_res import GetPillarsRes
from v1.pillars.pillar_service import PillarService
from v1.pillars.pillar_dependencies import get_pillar_service

pillar_router = APIRouter(prefix="/pillar")

@pillar_router.get("/all")
def get_pillars(service: PillarService = Depends(get_pillar_service)) -> GetPillarsRes:
    pillars: list[ConnectionPillar] = service.get_pillars()
    return {"pillars": pillars}