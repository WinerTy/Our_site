from typing import List, Optional
from sqlalchemy import String, ForeignKey
from src.models.base.base import Base

from sqlalchemy.orm import Mapped, relationship, mapped_column


class AdditionalService(Base):
    __tablename__ = "additional_services"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=124), unique=True)
    tag_id: Mapped[Optional[int]] = mapped_column(ForeignKey("tags.id"), nullable=True)
    tag: Mapped[Optional["Tag"]] = relationship(
        "Tag", back_populates="additional_services"
    )
