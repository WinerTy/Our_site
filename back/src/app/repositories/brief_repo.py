from src.repositories.sql_repo import SqlAlchemyRepository
from src.models.brief_model import Service, Brief
from src.config.database.db_helper import db_helper


from ..schemas.brief_schema import *


class ServiceRepository(SqlAlchemyRepository[Service, ServiceCreate, ServiceUpdate]):
    pass


class BriefRepository(SqlAlchemyRepository[Brief, BriefCreate, BriefUpdate]):
    pass


brief_repository = BriefRepository(Brief, db_helper.get_db_session)

service_repository = ServiceRepository(Service, db_helper.get_db_session)
