from typing import Optional
from sqlalchemy import ForeignKey, String
from ..base.base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
    user: Mapped[Optional["User"]] = relationship("User", back_populates="note")  # type: ignore
    email: Mapped[str] = mapped_column(String(length=124), nullable=False)
    text: Mapped[str] = mapped_column(String(length=512))
