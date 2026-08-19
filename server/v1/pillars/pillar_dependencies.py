from fastapi import Depends
from v1.database import supabase_client
from v1.pillars.pillar_dao import PillarDao
from v1.pillars.pillar_service import PillarService
from v1.database import get_db

def get_pillar_dao(db = Depends(get_db)) -> PillarDao:
    return PillarDao(db_connection=db)

def get_pillar_service(dao: PillarDao = Depends(get_pillar_dao)) -> PillarService:
    return PillarService(pillar_dao=dao)
