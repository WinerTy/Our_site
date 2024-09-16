from typing import Optional
from sqlalchemy import Float, String
from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column


class AdditionalService(Base):
    __tablename__ = "additionalservices"

    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    base_cost: Mapped[float] = mapped_column(
        Float(asdecimal=True, decimal_return_scale=2, precision=2)
    )
