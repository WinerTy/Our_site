from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from ...schemas.note_schemas import (
    NoteResponse,
    NoteCreate,
    NoteDetailResponse,
    NoteResponses,
)
from ...dependencies import current_user, get_session
from ...models.user_model import User

from ..repository.note_repo import note_repository
from ..repository.user_repo import user_repository


router = APIRouter(prefix="/note", tags=["Notes"])


@router.post("/", response_model=NoteResponse)
async def create_note(
    note_data: NoteCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_session),
):
    note_data = NoteCreate.from_request(note_data.model_dump(), user)
    note = await note_repository.create(session, note_data)
    return NoteResponse(id=note.id, detail="succses")


@router.get("/", response_model=List[NoteResponses])
async def get_notes(
    skip: int = 0,
    limit: int = 100,
    email: Optional[str] = None,
    user_id: Optional[int] = None,
    session: AsyncSession = Depends(get_session),
):
    filters = {}
    if email:
        filters["email"] = email
    if user_id:
        filters["user_id"] = user_id
    notes = await note_repository.get_multi(
        session, skip=skip, limit=limit, filters=filters
    )
    return notes


@router.get("/{note_id}", response_model=NoteDetailResponse)
async def detail_note(
    note_id: int,
    session: AsyncSession = Depends(get_session),
):
    note = await note_repository.get(session, id=note_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    user = await user_repository.get(session, id=note.user_id)
    note.user = user
    return note
