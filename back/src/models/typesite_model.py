from typing import Optional
from sqlalchemy import ForeignKey, String, Float
from .base_model import Base
from .user_model import User
from sqlalchemy.orm import Mapped, relationship, mapped_column


class TypeSite(Base):
    __tablename__ = "sitetypes"

    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    base_cost: Mapped[float] = mapped_column(
        Float(asdecimal=True, decimal_return_scale=2, precision=2)
    )
