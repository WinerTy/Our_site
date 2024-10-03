from pydantic import BaseModel, EmailStr, field_validator, Field

from typing import Optional

from src.models.user import User
from src.schemas.user.user_schemas import UserRead


class NoteBase(BaseModel):
    email: EmailStr = Field(
        "john.doe@example.com", title="Почта клиента", example="john.doe@example.com"
    )
    text: str = Field(
        "Some text for send", title="Текстовое поле", example="Some text for send"
    )

    @classmethod
    def from_request(cls, data: dict, user: User):
        if user:
            data["user_id"] = user.id
        else:
            data["user_id"] = None
        return cls(**data)

    @field_validator("text")
    def validate_text(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        if len(v) > 124:
            raise ValueError("Field so long, max size 512")
        return v

    @field_validator("email")
    def validate_email(cls, v):
        if len(v) > 124:
            raise ValueError("Email so long, max size 124 symbols")
        return v


class NoteCreate(NoteBase):
    user_id: Optional[int] = Field(None, title="id Пользователя", example=None)


class NoteUpdate(NoteBase):
    user_id: Optional[int] = Field(None, title="id Пользователя", example=None)


class NoteRead(NoteBase):
    id: int = Field(1, title="id Записи", example=1)
