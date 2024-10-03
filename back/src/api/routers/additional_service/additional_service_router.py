from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.additional_service import (
    AdditionalServiceCreate,
    AdditionalServiceResponse,
    AdditionalServiceList,
)
from src.dependencies import get_session


from src.api.repository.additional_service import additional_repo
from src.api.repository.tag import tag_repository


router = APIRouter(prefix="/additional_service", tags=["Additional Service"])


@router.post("/", response_model=AdditionalServiceResponse)
async def create_additional_service(
    additional_data: AdditionalServiceCreate,
    session: AsyncSession = Depends(get_session),
):
    if additional_data.tag_id:
        await tag_repository.get_by_id(session, id=additional_data.tag_id)
    additional_service = await additional_repo.create(session, additional_data)
    return AdditionalServiceResponse(id=additional_service.id, detail="Succses")


@router.get("/", response_model=List[AdditionalServiceList])
async def additional_service_list(
    skip: int = 0,
    limit: int = 100,
    tag_id: Optional[int] = None,
    session: AsyncSession = Depends(get_session),
):
    filters = {}
    if tag_id:
        filters["tag_id"] = tag_id
    additional_services = await additional_repo.get_multi(
        session, skip=skip, limit=limit, filters=filters, load_relations=["tag"]
    )
    return additional_services
