from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable


from .base_model import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    bibs: Mapped[list["Bib"]] = relationship("Bib", back_populates="user")
