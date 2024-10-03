from typing import List, Optional
from sqlalchemy import ForeignKey, String
from src.models.base import Base

from sqlalchemy.orm import Mapped, relationship, mapped_column


class BriefServiceAssociation(Base):
    __tablename__ = "brief_service_association"
    brief_id: Mapped[int] = mapped_column(ForeignKey("briefs.id"), primary_key=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), primary_key=True)


class BriefAdditionalServiceAssociation(Base):
    __tablename__ = "brief_additional_service_association"
    brief_id: Mapped[int] = mapped_column(ForeignKey("briefs.id"), primary_key=True)
    additional_service_id: Mapped[int] = mapped_column(
        ForeignKey("additional_services.id"), primary_key=True
    )


class Brief(Base):
    __tablename__ = "briefs"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    company_did: Mapped[Optional[str]] = mapped_column(
        String(length=1024), nullable=True
    )
    concompetitors: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_comment: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    client_name: Mapped[str] = mapped_column(String(length=124), nullable=False)
    client_phone: Mapped[str] = mapped_column(String(length=20), nullable=False)
    client_email: Mapped[str] = mapped_column(String(length=124), nullable=False)
    client_task: Mapped[str] = mapped_column(String, nullable=False)
    client_company: Mapped[Optional[str]] = mapped_column(
        String(length=1024), nullable=True
    )
    client_site: Mapped[Optional[str]] = mapped_column(
        String(length=1024), nullable=True
    )
    services: Mapped[List["Service"]] = relationship(
        "Service", secondary="brief_service_association", back_populates="briefs"
    )
    additional_services: Mapped[List["AdditionalService"]] = relationship(
        "AdditionalService",
        secondary="brief_additional_service_association",
        back_populates="briefs",
    )
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
    user: Mapped[Optional["User"]] = relationship("User", back_populates="brief")
