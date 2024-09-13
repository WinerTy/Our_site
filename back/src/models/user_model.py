from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from .base_model import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
