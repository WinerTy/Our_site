from src.api.repository.base import BaseRepository

from src.models.additional_service import AdditionalService

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List, Optional


class AdditionalServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__(AdditionalService)


additional_service_repo = AdditionalServiceRepository()
