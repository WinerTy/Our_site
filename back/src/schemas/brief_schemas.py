from pydantic import BaseModel, EmailStr
from typing import Optional, List

from src.schemas.service_schemas import ServiceList


class BriefUpdate(BaseModel):
    company_did: Optional[str]
    concompetitors: Optional[str]
    additional_comment: Optional[str]
    client_name: str
    client_phone: str
    client_email: EmailStr
    client_task: str
    client_company: Optional[str]
    client_site: Optional[str]
    services: List[int] = []


class BriefCreate(BaseModel):
    company_did: Optional[str]
    concompetitors: Optional[str]
    additional_comment: Optional[str]
    client_name: str
    client_phone: str
    client_email: EmailStr
    client_task: str
    client_company: Optional[str]
    client_site: Optional[str]
    services: List[int] = []


class BriefList(BaseModel):
    company_did: Optional[str]
    concompetitors: Optional[str]
    additional_comment: Optional[str]
    client_name: str
    client_phone: str
    client_email: EmailStr
    client_task: str
    client_company: Optional[str]
    client_site: Optional[str]
    services: List[ServiceList] = []


class BriefResponse(BaseModel):
    id: int
    detail: str
