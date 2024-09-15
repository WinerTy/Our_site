from typing import Annotated
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.bib_schema import BibResponse, BibCreate
from src.models.user_model import User
from src.database.db import get_session
from src.app.repositories.bibs_repo import bib_repository
from src import current_user

router = APIRouter(prefix="/bibs", tags=["bibs"])


@router.post("/", response_model=BibResponse)
async def create_bib(
    bib_data: BibCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_session),
) -> BibResponse:
    data = bib_data.dict()
    if user:
        data["user_id"] = user.id
    bib = await bib_repository.create(data)
    return bib


@router.get("/", response_model=list[BibResponse])
async def get_all_bibs(
    order: Annotated[list, Query()] = [],
    limit: int = 100,
    offset: int = 0,
    db_session: AsyncSession = Depends(get_session),
) -> list[BibResponse]:
    bibs = await bib_repository.get_multi(order=order, limit=limit, offset=offset)
    return bibs
