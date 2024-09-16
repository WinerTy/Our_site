from typing import Optional
from sqlalchemy import ForeignKey, String, Enum
from .base_model import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column


class Service(Base):
    __tablename__ = "services"

    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    brifs: Mapped[list["Brif"]] = relationship(
        "Brif", secondary="brif_service_association", back_populates="services"
    )
