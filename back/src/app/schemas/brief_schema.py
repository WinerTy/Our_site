from pydantic import BaseModel


from typing import List, Optional


class ServiceBase(BaseModel):
    id: int


class ServiceCreate(BaseModel):
    name: str


class ServiceResponce(BaseModel):
    id: int
    name: str


class ServiceUpdate(BaseModel):
    name: str


class BriefCreate(BaseModel):
    company_did: Optional[str] = None
    concompetitors: Optional[str] = None
    additional_comment: Optional[str] = None

    client_name: str
    client_phone: str
    client_email: str

    client_task: str
    client_company: Optional[str] = None
    client_site: Optional[str] = None

    services: List[ServiceBase]


class BriefUpdate(BaseModel):
    company_did: Optional[str] = None
    concompetitors: Optional[str] = None
    additional_comment: Optional[str] = None

    client_name: str
    client_phone: str
    client_email: str

    client_task: str
    client_company: Optional[str] = None
    client_site: Optional[str] = None

    services: List[ServiceBase]
