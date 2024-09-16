from pydantic import BaseModel


from typing import Optional


class ServiceCreate(BaseModel):
    name: str


class ServiceUpdate(BaseModel):
    name: str


class ServiceResponce(BaseModel):
    id: int
    name: str
