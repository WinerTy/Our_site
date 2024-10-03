from pydantic import BaseModel


class TagCreate(BaseModel):
    name: str


class TagUpdate(BaseModel):
    name: str


class TagList(BaseModel):
    id: int
    name: str


class TagResponse(BaseModel):
    id: int
    detail: str
