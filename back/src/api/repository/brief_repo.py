from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy import select

from src.schemas.brief_schemas import BriefCreate
from .base import BaseRepository
from src.models.services.service_model import Service
from src.models.brief.brief_model import (
    Brief,
    BriefServiceAssociation,
    BriefSiteTypeAssociation,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload, selectinload


class BriefRepository(BaseRepository):
    def __init__(self):
        super().__init__(Brief)

    async def get(self, db: AsyncSession, id: int) -> Optional[Brief]:
        try:
            query = (
                select(self.model)
                .options(
                    joinedload(self.model.services), joinedload(self.model.site_types)
                )
                .where(self.model.id == id)
            )
            result = await db.execute(query)
            return result.scalars().first()
        except SQLAlchemyError as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        except Exception as e:
            await db.rollback()
            raise HTTPException(
                status_code=500, detail=f"An unexpected error occurred: {str(e)}"
            )

    async def get_multi(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[dict] = None,
    ) -> List[Brief]:
        try:
            query = (
                select(self.model)
                .options(
                    selectinload(self.model.services),
                    selectinload(self.model.site_types),
                )
                .offset(skip)
                .limit(limit)
            )

            if filters:
                for key, value in filters.items():
                    query = query.filter(getattr(self.model, key) == value)

            result = await db.execute(query)
            return result.scalars().all()
        except SQLAlchemyError as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        except Exception as e:
            await db.rollback()
            raise HTTPException(
                status_code=500, detail=f"An unexpected error occurred: {str(e)}"
            )

    async def create(self, db: AsyncSession, obj_in: BriefCreate) -> Brief:
        db_obj = Brief(**obj_in.model_dump(exclude={"services", "site_types"}))
        db.add(db_obj)
        await db.flush()

        for service_id in obj_in.services:
            service_association = BriefServiceAssociation(
                brief_id=db_obj.id, service_id=service_id
            )
            db.add(service_association)

        for site_type_id in obj_in.site_types:
            site_type_association = BriefSiteTypeAssociation(
                brief_id=db_obj.id, site_type_id=site_type_id
            )
            db.add(site_type_association)

        await db.commit()
        await db.refresh(db_obj)
        return db_obj


brief_repository = BriefRepository()
