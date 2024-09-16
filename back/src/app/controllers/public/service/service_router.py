from fastapi import APIRouter, Depends
from ....schemas.service_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_session
from ....repositories.service_repo import service_repository

router = APIRouter(prefix="/service", tags=["service"])


@router.post("/", response_model=ServiceResponce)
async def create_service(
    service_data: ServiceCreate, session: AsyncSession = Depends(get_session)
) -> ServiceResponce:
    data = service_data.dict()
    service = await service_repository.create(data)
    return service
