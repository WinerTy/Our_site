from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import current_user, get_session
from src.models.user import User
from src.schemas.base import BaseResponse
from src.schemas.brief import BriefCreate, BriefRead, BriefUpdate
from src.api.repository.brief import brief_repository
from src.api.repository.service import service_repository
from src.api.repository.additional_service import additional_repo

router = APIRouter(prefix="/brief", tags=["Briefs"])


async def check_services_exist(
    session: AsyncSession,
    services: Optional[List[int]] = None,
    additional_services: Optional[List[int]] = None,
):
    if services:
        for service_id in services:
            await service_repository.get_by_id(session, service_id)

    if additional_services:
        for additional_id in additional_services:
            await additional_repo.get_by_id(session, additional_id)


@router.post("/", response_model=BaseResponse)
async def create_brief(
    brief_data: BriefCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_session),
):
    await check_services_exist(
        session=session,
        services=brief_data.services,
        additional_services=brief_data.additional_services,
    )

    brief_data = BriefCreate.from_request(brief_data.model_dump(), user)
    brief = await brief_repository.create(session, brief_data)
    return BaseResponse(id=brief.id, detail="Succses")


@router.get("/", response_model=List[BriefRead])
async def briefs_list(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None,
    db: AsyncSession = Depends(get_session),
):
    filters = {}
    if user_id:
        filters["user_id"] = user_id
    briefs = await brief_repository.get_multi(
        db,
        skip=skip,
        limit=limit,
        filters=filters,
        load_relations=["services", "additional_services"],
    )
    return briefs


@router.get("/{brief_id}", response_model=BriefRead)
async def detail_brief(brief_id: int, session: AsyncSession = Depends(get_session)):
    brief = await brief_repository.get_by_id(
        session,
        id=brief_id,
        load_relations=["services", "additional_services"],
    )

    return brief


@router.put("/{brief_id}", response_model=BaseResponse)
async def update_brief(
    brief_id: int,
    update_data: BriefUpdate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_session),
):
    brief = await brief_repository.get_by_id(
        session,
        id=brief_id,
        load_relations=["services", "additional_services"],
    )
    await check_services_exist(
        session=session,
        services=update_data.services,
        additional_services=update_data.additional_services,
    )
    update_data = BriefUpdate.from_request(update_data.model_dump(), user)
    updated_brief = await brief_repository.update(session, brief, update_data)
    return BaseResponse(id=updated_brief.id, detail="Update succses")
