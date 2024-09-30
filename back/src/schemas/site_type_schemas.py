from pydantic import BaseModel


class SiteTypeCreate(BaseModel):
    name: str
    base_cost: float


class SiteTypeUpdate(BaseModel):
    name: str
    base_cost: float


class SiteTypeResponse(BaseModel):
    id: int
    detail: str


class SiteTypeList(BaseModel):
    id: int
    name: str
    base_cost: float
