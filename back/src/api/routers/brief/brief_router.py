from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import current_user, get_session
from src.models.user import User
from src.schemas.brief import BriefCreate, BriefList, BriefResponse
from src.api.repository.brief import brief_repository
from src.api.repository.service import service_repository
from src.api.repository.additional_service import additional_repo

router = APIRouter(prefix="/brief", tags=["Briefs"])


from icecream import ic


@router.post("/", response_model=BriefResponse)
async def create_brief(
    brief_data: BriefCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_session),
):
    if brief_data.services:
        for service_id in brief_data.services:
            await service_repository.get_by_id(session, service_id)

    if brief_data.additional_services:
        for additional_id in brief_data.additional_services:
            await additional_repo.get_by_id(session, additional_id)

    brief_data = BriefCreate.from_request(brief_data.model_dump(), user)
    brief = await brief_repository.create(session, brief_data)
    return BriefResponse(id=brief.id, detail="Succses")


@router.get("/", response_model=List[BriefList])
async def briefs_list(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)
):
    briefs = await brief_repository.get_multi(
        db, skip=skip, limit=limit, load_relations=["services", "additional_services"]
    )
    return briefs


@router.get("/{brief_id}", response_model=BriefList)
async def detail_brief(brief_id: int, session: AsyncSession = Depends(get_session)):
    brief = await brief_repository.get_by_id(
        session,
        id=brief_id,
        load_relations=["services", "additional_services"],
    )
    return brief
