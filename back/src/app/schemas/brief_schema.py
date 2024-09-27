import re
from pydantic import BaseModel, EmailStr, validator, field_validator, HttpUrl


from typing import List, Optional

from src.models.user_model import User


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
    client_email: EmailStr

    client_task: str
    client_company: Optional[str] = None
    client_site: Optional[HttpUrl] = None

    services: List[int]
    user_id: Optional[int] = None

    @field_validator("client_phone")
    def validate_phone(cls, value):
        phone_regex = r"^\+\d{1,3} \(\d{3}\) \d{3} \d{2}-\d{2}$"
        if not re.match(phone_regex, value):
            raise ValueError("client_phone is not correct")
        return value

    @field_validator("services")
    def validate_services(cls, value):
        if not all(isinstance(service, int) and service > 0 for service in value):
            raise ValueError("Service id can't be negative")
        if len(value) != len(set(value)):
            raise ValueError("Service id must be unique")
        return value

    @field_validator("client_name", "client_task")
    @classmethod
    def validate_not_empty(cls, value):
        if not value:
            raise ValueError(f"Field can't be pass")
        return value

    # @field_validator("client_site")
    # def validate_url(cls, value):
    #     site_regex = r"^https?://"
    #     if not re.match(site_regex, value):
    #         raise ValueError("Site url starting with http://")
    #     return value


class BriefUpdate(BaseModel):
    company_did: Optional[str] = None
    concompetitors: Optional[str] = None
    additional_comment: Optional[str] = None

    client_name: str
    client_phone: str
    client_email: EmailStr

    client_task: str
    client_company: Optional[str] = None
    client_site: Optional[str] = None

    services: List[int]


class ServiceResponse(BaseModel):
    id: int
    name: str


class BriefResponse(BaseModel):
    detail: str
