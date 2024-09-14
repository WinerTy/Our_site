from fastapi import APIRouter, Depends
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
):
    data = bib_data.dict()
    if user:
        data["user_id"] = user.id
    bib = await bib_repository.create(data)
    return bib
