from typing import Optional
from pydantic import BaseModel
from src.schemas.tag import TagList


class ServiceCreate(BaseModel):
    name: str
    tag_id: Optional[int] = None


class ServiceResponse(BaseModel):
    id: int
    detail: str


class ServiceList(BaseModel):
    id: int
    name: str
    tag: Optional[TagList] = None


class ServiceUpdate(BaseModel):
    name: str
    is_active: bool
