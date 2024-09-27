from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_session
from src.models.brief_model import Brief, Service
from src.models.user_model import User

from ...schemas.brief_schema import *
from ...repositories.brief_repo import (
    service_repository,
)
from src import current_user

router = APIRouter(prefix="/service", tags=["service"])


@router.post("/", response_model=ServiceResponce)
async def create_service(service_data: ServiceCreate) -> ServiceResponce:
    data = service_data.dict()
    service = await service_repository.create(data)
    return service


@router.get("/", response_model=list[ServiceResponce])
async def get_all_services(
    order: Annotated[list, Query()] = [],
    limit: int = 100,
    offset: int = 0,
) -> list[ServiceResponce]:
    services = await service_repository.get_multi(
        order=order, limit=limit, offset=offset
    )
    return services


@router.post("/briefs/", response_model=BriefResponse)
async def create_brief(
    brief_data: BriefCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_session),
) -> BriefResponse:
    await session.begin()  # Начать транзакцию
    try:
        data = brief_data.dict(exclude={"services"})
        if user:
            data["user_id"] = user.id
        brief = Brief(**data)  # Используйте **data для распаковки словаря

        for service_id in brief_data.services:
            service = await session.get(Service, service_id)
            if not service:
                raise HTTPException(
                    status_code=404, detail=f"Service with id {service_id} not found"
                )
            brief.services.append(service)

        session.add(brief)
        await session.flush()
        await session.commit()
    except Exception as e:
        await session.rollback()
        # raise HTTPException(status_code=400, detail="Something wrong, try again")
        raise e

    return BriefResponse(detail="success")
