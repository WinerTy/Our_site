from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from ..base.base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    note: Mapped[list["Note"]] = relationship("Note", back_populates="user")
    brief: Mapped[list["Brief"]] = relationship("Brief", back_populates="user")
