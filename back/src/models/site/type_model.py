from typing import List
from src.models.base.base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Float


class SiteType(Base):
    __tablename__ = "site_types"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=512), nullable=False)
    base_cost: Mapped[float] = mapped_column(
        Float(precision=2, asdecimal=True), nullable=False
    )
    briefs: Mapped[List["Brief"]] = relationship(
        "Brief", secondary="brief_site_types_association", back_populates="site_types"
    )
