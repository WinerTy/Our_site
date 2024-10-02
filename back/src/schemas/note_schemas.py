from pydantic import BaseModel, EmailStr, field_validator

from typing import Optional

from src.models.users.user_model import User
from src.schemas.user_schemas import UserRead


class NoteCreate(BaseModel):
    user_id: Optional[int] = None
    email: EmailStr
    text: str

    @classmethod
    def from_request(cls, data: dict, user: User):
        if user:
            data["user_id"] = user.id
        else:
            data["user_id"] = None
        return cls(**data)

    @field_validator("text")
    def validate_text(cls, value):
        if len(value) > 512:
            raise ValueError("Text so long, max size 512 symbols")
        return value


class NoteUpdate(BaseModel):
    user_id: Optional[int] = None
    email: EmailStr
    text: str

    @field_validator("text")
    def validate_text(cls, value):
        if len(value) > 512:
            raise ValueError("Text so long, max size 512 symbols")
        return value


class NoteResponse(BaseModel):
    id: int
    detail: str


class NoteResponses(BaseModel):
    id: int
    user_id: Optional[int] = None
    email: EmailStr
    text: str


class NoteDetailResponse(BaseModel):
    id: int
    email: EmailStr
    text: str
    user: Optional[UserRead] = None
