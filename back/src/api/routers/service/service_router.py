from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import get_session
from src.schemas.services import ServiceCreate, ServiceList, ServiceResponse
from src.api.repository.service import service_repository

router = APIRouter(prefix="/service", tags=["Services"])


@router.post("/", response_model=ServiceResponse)
async def create_service(
    service_data: ServiceCreate, session: AsyncSession = Depends(get_session)
):
    service = await service_repository.create(session, service_data)
    return ServiceResponse(id=service.id, detail="Succses")


@router.get("/", response_model=list[ServiceList])
async def services_list(
    skip: int = 0,
    limit: int = 100,
    is_active: bool = True,
    session: AsyncSession = Depends(get_session),
):
    filters = {}
    filters["is_active"] = is_active
    services = await service_repository.get_multi(
        session, skip=skip, limit=limit, filters=filters
    )
    return services
