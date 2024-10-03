from typing import Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import get_session
from src.schemas.services import ServiceCreate, ServiceRead
from src.schemas.base import BaseResponse
from src.api.repository.service import service_repository
from src.api.repository.tag import tag_repository

router = APIRouter(prefix="/service", tags=["Services"])


@router.post("/", response_model=BaseResponse)
async def create_service(
    service_data: ServiceCreate, session: AsyncSession = Depends(get_session)
):
    if service_data.tag_id:
        await tag_repository.get_by_id(session, service_data.tag_id)
    service = await service_repository.create(session, service_data)
    return BaseResponse(id=service.id, detail="Succses")


@router.get("/", response_model=list[ServiceRead])
async def services_list(
    skip: int = 0,
    limit: int = 100,
    is_active: bool = True,
    tag_id: Optional[int] = None,
    session: AsyncSession = Depends(get_session),
):
    filters = {"is_active": is_active}
    if tag_id:
        filters["tag_id"] = tag_id
    services = await service_repository.get_multi(
        session, skip=skip, limit=limit, filters=filters, load_relations=["tag"]
    )
    return services
