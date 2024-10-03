from typing import List
from src.models.base.base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=124), unique=True, nullable=False)
    services: Mapped[List["Service"]] = relationship("Service", back_populates="tag")
    additional_services: Mapped[List["AdditionalService"]] = relationship(
        "AdditionalService", back_populates="tag"
    )
