from v1.pillars.types.pillar import ConnectionPillar
from pydantic import BaseModel

class GetPillarsRes(BaseModel):
    pillars: list[ConnectionPillar]