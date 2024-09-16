from fastapi import APIRouter, Depends
from ....schemas.service_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_session
from ....repositories.service_repo import service_repository

router = APIRouter(prefix="/service", tags=["service"])


# @router.post("/", response_model=ServiceResponce)
# async def create_bib(
#     bib_data: BibCreate,
#     user: User = Depends(current_user),
#     session: AsyncSession = Depends(get_session),
# ) -> BibResponse:
#     data = bib_data.dict()
#     if user:
#         data["user_id"] = user.id
#     bib = await bib_repository.create(data)
#     return bib


@router.post("/", response_model=ServiceResponce)
async def create_service(
    service_data: ServiceCreate, session: AsyncSession = Depends(get_session)
) -> ServiceResponce:
    data = service_data.dict()
    service = await service_repository.create(data)
    return service
