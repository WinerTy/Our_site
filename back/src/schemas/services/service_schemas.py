from pydantic import BaseModel


class ServiceCreate(BaseModel):
    name: str


class ServiceResponse(BaseModel):
    id: int
    detail: str


class ServiceList(BaseModel):
    id: int
    name: str


class ServiceUpdate(BaseModel):
    name: str
    is_active: bool
