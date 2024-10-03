from pydantic import BaseModel, field_validator, Field

from typing import Optional
from src.schemas.tag import TagRead


class AdditionalServiceBase(BaseModel):
    name: str = Field("Add SEO", title="Название доп.услуги", example="Add SEO")

    @field_validator("name")
    def check_name(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        if len(v) > 124:
            raise ValueError("Field so long, max size 124")
        return v


class AdditionalServiceCreate(AdditionalServiceBase):
    tag_id: Optional[int] = Field(None, title="id Тэга", example=1)


class AdditionalServiceUpdate(AdditionalServiceBase):
    is_active: bool = Field(True, title="Доп.Услуга активна", example=True)
    tag_id: Optional[int] = Field(1, title="id Тэга", example=1)


class AdditionalServiceRead(AdditionalServiceBase):
    id: int = Field(1, title="id Доп.Услуги", example=1)
    tag: Optional[TagRead] = Field(None, title="Объект Тэга", example={"id": 1})
