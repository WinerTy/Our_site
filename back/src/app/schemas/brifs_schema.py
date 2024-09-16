from pydantic import BaseModel


from typing import Optional


class BrifServiceAssociationCreate(BaseModel):
    brif_id: int
    service_id: int


class BrifCreate(BaseModel):
    client_name: str
    services: list[BrifServiceAssociationCreate]


class BrifUpdate(BaseModel):
    client_name: str
