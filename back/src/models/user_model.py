from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from .base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    bibs: Mapped[list["Note"]] = relationship("Note", back_populates="user")
