from pydantic import BaseModel, EmailStr
from typing import Optional, List

from src.schemas.service_schemas import ServiceList
from src.schemas.site_type_schemas import SiteTypeList


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
    site_types: List[int] = []


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
    site_types: List[SiteTypeList] = []


class BriefResponse(BaseModel):
    id: int
    detail: str
