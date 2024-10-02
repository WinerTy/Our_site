from pydantic import BaseModel, EmailStr
from typing import Optional, List

from src.models.users.user_model import User
from src.schemas.service_schemas import ServiceList
from src.schemas.site_type_schemas import SiteTypeList
from src.schemas.user_schemas import UserRead


class BriefUpdate(BaseModel):
    company_did: Optional[str]
    concompetitors: Optional[str]
    additional_comment: Optional[str]
    budget: str
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
    user_id: Optional[int] = None

    @classmethod
    def from_request(cls, data: dict, user: User):
        if user:
            data["user_id"] = user.id
        else:
            data["user_id"] = None
        print(data)
        return cls(**data)


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
    user_id: Optional[int] = None


class BriefResponse(BaseModel):
    id: int
    detail: str
