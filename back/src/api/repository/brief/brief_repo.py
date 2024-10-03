from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List, Optional
from fastapi import HTTPException, status

from src.api.repository.base.base import BaseRepository
from src.models.additional_service.additional_service_model import AdditionalService
from src.models.brief.brief_model import (
    Brief,
    BriefAdditionalServiceAssociation,
    BriefServiceAssociation,
)
from src.models.services.service_model import Service
from src.schemas.brief import BriefRead, BriefCreate
from src.schemas.brief.brief_schemas import BriefUpdate


class BriefRepository(BaseRepository):
    def __init__(self):
        super().__init__(Brief)

    async def get_by_id(
        self, db: AsyncSession, id: int, load_relations: Optional[List[str]] = None
    ):
        query = select(self.model).where(self.model.id == id)
        if load_relations:
            for relation in load_relations:
                if relation == "services":
                    query = query.options(
                        selectinload(self.model.services).selectinload(Service.tag)
                    )
                elif relation == "additional_services":
                    query = query.options(
                        selectinload(self.model.additional_services).selectinload(
                            AdditionalService.tag
                        )
                    )
                else:
                    query = query.options(selectinload(getattr(self.model, relation)))
        result = await db.execute(query)
        obj = result.scalars().first()
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Object not found"
            )
        return obj

    async def get_multi(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[dict] = None,
        load_relations: Optional[List[str]] = None,
    ) -> List[BriefRead]:
        query = select(self.model).offset(skip).limit(limit)

        if filters:
            for key, value in filters.items():
                query = query.filter(getattr(self.model, key) == value)

        if load_relations:
            for relation in load_relations:
                if relation == "services":
                    query = query.options(
                        selectinload(self.model.services).selectinload(Service.tag)
                    )
                elif relation == "additional_services":
                    query = query.options(
                        selectinload(self.model.additional_services).selectinload(
                            AdditionalService.tag
                        )
                    )
                else:
                    query = query.options(selectinload(getattr(self.model, relation)))

        result = await db.execute(query)
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: BriefCreate) -> Brief:
        db_obj = Brief(**obj_in.model_dump(exclude={"services", "additional_services"}))
        db.add(db_obj)
        await db.flush()
        if obj_in.services:
            for service_id in obj_in.services:
                service_association = BriefServiceAssociation(
                    brief_id=db_obj.id, service_id=service_id
                )
                db.add(service_association)
        if obj_in.additional_services:
            for additional_id in obj_in.additional_services:
                additional_assotiation = BriefAdditionalServiceAssociation(
                    brief_id=db_obj.id, additional_service_id=additional_id
                )
                db.add(additional_assotiation)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, db_obj: Brief, obj_in: BriefUpdate
    ) -> Brief:
        update_data = obj_in.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_obj, key, value)

        # Обновляем услуги
        if obj_in.services is not None:
            # Удаляем текущие ассоциации с услугами, которых нет в новом списке
            db_obj.services = [
                service
                for service in db_obj.services
                if service.id not in obj_in.services
            ]
            # Добавляем новые ассоциации
            for service_id in obj_in.services:
                if service_id not in [service.id for service in db_obj.services]:
                    service_association = BriefServiceAssociation(
                        brief_id=db_obj.id, service_id=service_id
                    )
                    db.add(service_association)

        # Обновляем дополнительные услуги
        if obj_in.additional_services is not None:
            # Удаляем текущие ассоциации с дополнительными услугами, которых нет в новом списке
            db_obj.additional_services = [
                additional_service
                for additional_service in db_obj.additional_services
                if additional_service.id not in obj_in.additional_services
            ]
            # Добавляем новые ассоциации
            for additional_id in obj_in.additional_services:
                if additional_id not in [
                    additional_service.id
                    for additional_service in db_obj.additional_services
                ]:
                    additional_assotiation = BriefAdditionalServiceAssociation(
                        brief_id=db_obj.id, additional_service_id=additional_id
                    )
                    db.add(additional_assotiation)

        await db.commit()
        await db.refresh(db_obj)
        return db_obj


brief_repository = BriefRepository()
