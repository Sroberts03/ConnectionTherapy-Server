from v1.pillars.pillar_dao import PillarDao
from v1.pillars.types.pillar import ConnectionPillar

class PillarService:
    def __init__(self, pillar_dao: PillarDao):
        self.pillar_dao = pillar_dao
    
    def get_pillars(self) -> list[ConnectionPillar]:
        pillars: list[ConnectionPillar] = self.pillar_dao.get_all_pillars()
        return pillars