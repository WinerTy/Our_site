from typing import Optional
from sqlalchemy import ForeignKey, String
from .base_model import Base
from .user_model import User
from sqlalchemy.orm import Mapped, relationship, mapped_column


class Bib(Base):
    __tablename__ = "bibs"

    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
    user: Mapped[Optional[User]] = relationship("User", back_populates="bibs")
    text: Mapped[str] = mapped_column(String(length=512))
