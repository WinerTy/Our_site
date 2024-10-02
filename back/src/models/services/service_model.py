from typing import List
from sqlalchemy import String
from src.models.base.base import Base

from sqlalchemy.orm import Mapped, relationship, mapped_column


class Service(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    briefs: Mapped[List["Brief"]] = relationship(
        "Brief", secondary="brief_service_association", back_populates="services"
    )
