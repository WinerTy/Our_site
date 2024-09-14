from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable


from .base_model import Base
from sqlalchemy.orm import Mapped, relationship


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    bibs: Mapped[list["Bib"]] = relationship("Bib", back_populates="user")
