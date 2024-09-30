from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import current_user, get_session
from src.schemas.site_type_schemas import (
    SiteTypeList,
    SiteTypeCreate,
    SiteTypeUpdate,
    SiteTypeResponse,
)
from src.api.repository.site_type_repo import site_type_repository


router = APIRouter(prefix="/site_types", tags=["SiteTypes"])


@router.post("", response_model=SiteTypeResponse)
async def create_type(
    type_data: SiteTypeCreate, session: AsyncSession = Depends(get_session)
):
    type = await site_type_repository.create(session, type_data)
    return SiteTypeResponse(id=type.id, detail="Succses")
