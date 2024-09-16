from src.repositories.sql_repo import SqlAlchemyRepository
from src.models.service_model import Service
from src.config.database.db_helper import db_helper


from ..schemas.service_schema import *


class ServiceRepository(SqlAlchemyRepository[Service, ServiceCreate, ServiceUpdate]):
    pass


service_repository = ServiceRepository(
    model=Service, db_session=db_helper.get_db_session
)
