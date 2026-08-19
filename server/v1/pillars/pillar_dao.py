from v1.pillars.types.pillar import ConnectionPillar
from typing import List

class PillarDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_pillars(self) -> List[ConnectionPillar]:
        response = self.db_connection.table("pillars") \
            .select("*") \
            .execute()
        return [ConnectionPillar(**pillar) for pillar in response.data]

        