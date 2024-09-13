from sqlalchemy import String
from .base_model import Base
from sqlalchemy.orm import mapped_column, Mapped


class User(Base):
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, index=True, unique=True)
