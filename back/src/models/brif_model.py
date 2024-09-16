from typing import Optional
from sqlalchemy import ForeignKey, String, Enum
from .base_model import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column


class BrifServiceAssociation(Base):
    __tablename__ = "brif_service_association"

    brif_id: Mapped[int] = mapped_column(ForeignKey("brifs.id"), primary_key=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), primary_key=True)


class Brif(Base):
    __tablename__ = "brifs"
    services: Mapped[list["Service"]] = relationship(
        "Service", secondary="brif_service_association", back_populates="brifs"
    )
    client_name: Mapped[str] = mapped_column(String(length=255), nullable=False)
