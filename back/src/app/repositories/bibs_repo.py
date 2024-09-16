from src.repositories.sql_repo import SqlAlchemyRepository
from src.models.bid_model import Bib
from src.config.database.db_helper import db_helper


from ..schemas.bib_schema import *


class BibRepository(SqlAlchemyRepository[Bib, BibCreate, BibUpdate]):
    pass


bib_repository = BibRepository(model=Bib, db_session=db_helper.get_db_session)
