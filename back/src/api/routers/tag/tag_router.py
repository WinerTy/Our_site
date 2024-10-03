from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import get_session
from src.schemas.tag import TagCreate, TagResponse, TagList, TagUpdate
from src.api.repository.tag import tag_repository

router = APIRouter(prefix="/tag", tags=["Tags"])


@router.post("/", response_model=TagResponse)
async def create_tag(tag_data: TagCreate, session: AsyncSession = Depends(get_session)):
    tag = await tag_repository.create(session, tag_data)
    return TagResponse(id=tag.id, detail="Succses")


@router.get("/", response_model=list[TagList])
async def tag_list(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session),
):
    tags = await tag_repository.get_multi(session, skip=skip, limit=limit)
    return tags


@router.put("/{tag_id}", response_model=TagResponse)
async def update_tag(
    tag_id: int, tag_data: TagUpdate, session: AsyncSession = Depends(get_session)
):
    tag = await tag_repository.get_by_id(session, id=tag_id)
    update_tag = await tag_repository.update(session, tag, tag_data)
    return TagResponse(id=update_tag.id, detail="succses")


@router.delete("/{tag_id}", response_model=TagResponse)
async def delete_tag(tag_id: int, session: AsyncSession = Depends(get_session)):
    delete_tag = await tag_repository.delete(session, id=tag_id)
    return TagResponse(id=delete_tag.id, detail="Delete succses")
