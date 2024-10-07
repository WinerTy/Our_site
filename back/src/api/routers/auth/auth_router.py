from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.note.note_schemas import NoteCreate, NoteRead
from src.schemas.base import BaseResponse
from src.dependencies.auth_depend import current_user, get_session
from src.models.user import User

from src.api.repository.note import note_repository
from src.api.repository.user import user_repository


router = APIRouter(prefix="/auth", tags=["Auth"])


# @router.post("/auth/jwt/login")
# async def login(user: models.UP, password: str, user_manager: UserManager = Depends(fastapi_users.get_user_manager)):
#     user = await user_manager.authenticate(user, password)
#     if user is None:
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     access_token = jwt_authentication.create_access_token(user)
#     refresh_token = jwt_authentication.create_refresh_token(user)

#     return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
