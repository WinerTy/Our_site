from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import current_user, get_session
from src.schemas.brief_schemas import BriefCreate, BriefList, BriefResponse
from src.schemas.service_schemas import ServiceCreate, ServiceList, ServiceResponse
from src.api.repository.brief_repo import brief_repository
from src.api.repository.service_repo import service_repository

router = APIRouter(prefix="/brief", tags=["Briefs"])


@router.post("/", response_model=BriefResponse)
async def create_brief(
    brief_data: BriefCreate,
    session: AsyncSession = Depends(get_session),
):
    for service_id in brief_data.services:
        service = await service_repository.get(session, service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service id not found")
    brief = await brief_repository.create(session, brief_data)
    return BriefResponse(id=brief.id, detail="Succses")


@router.get("/", response_model=List[BriefList])
async def read_briefs(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)
):
    briefs = await brief_repository.get_multi(db, skip=skip, limit=limit)
    return briefs
