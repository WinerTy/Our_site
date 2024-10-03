from pydantic import BaseModel, EmailStr, field_validator

from typing import Optional
from src.schemas.tag import TagList


class AdditionalServiceCreate(BaseModel):
    name: str
    tag_id: Optional[int] = None


class AdditionalServiceUpdate(BaseModel):
    name: str
    tag_id: Optional[int]


class AdditionalServiceResponse(BaseModel):
    id: int
    detail: str


class AdditionalServiceList(BaseModel):
    id: int
    name: str
    tag: Optional[TagList] = None
