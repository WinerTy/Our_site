from typing import Type, TypeVar, List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.base.base import Base
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == id)
        result = await db.execute(query)
        return result.scalars().first()

    async def get_multi(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[dict] = None,
    ) -> List[ModelType]:
        query = select(self.model).offset(skip).limit(limit)

        if filters:
            for key, value in filters.items():
                query = query.filter(getattr(self.model, key) == value)

        result = await db.execute(query)
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, db_obj: ModelType, obj_in: UpdateSchemaType
    ) -> ModelType:
        for field in obj_in.model_dump(exclude_unset=True):
            setattr(db_obj, field, getattr(obj_in, field))
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        obj = await self.get(db, id)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj
