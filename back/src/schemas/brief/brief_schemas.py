import re
from pydantic import BaseModel, EmailStr, field_validator, Field, HttpUrl
from typing import Optional, List

from src.models.user import User


class BriefServices(BaseModel):
    services: Optional[List[int]] = Field(
        None, title="Массив id услуг", example=[1, 2, 3]
    )
    additional_services: Optional[List[int]] = Field(
        None, title="Массив id доп.услуг", example=[1, 2, 3, 4, 5]
    )


class BriefBase(BaseModel):
    company_did: Optional[str] = Field(
        None, title="Занятость компании", example="company123"
    )
    concompetitors: Optional[str] = Field(
        None, title="Конкуренты", example="Competitor A, Competitor B"
    )
    additional_comment: Optional[str] = Field(
        None, title="Дополньтельная информация", example="Some additional comment"
    )
    budget: str = Field("1000", title="Бюджет", example="1000")
    client_name: str = Field("John Doe", title="Имя клиента", example="John Doe")
    client_phone: str = Field(
        "+1 (123) 456-78-90", title="Номер клиента", example="+1 (123) 456-78-90"
    )
    client_email: EmailStr = Field(
        "john.doe@example.com", title="Почта клиента", example="john.doe@example.com"
    )
    client_task: str = Field(
        "Create a website", title="Задача клиента", example="Create a website"
    )
    client_company: Optional[str] = Field(
        None, title="Компания клиента", example="Example Company"
    )
    client_site: Optional[HttpUrl] = Field(
        None, title="Сайт клиента", example="https://example.com"
    )
    user_id: Optional[int] = Field(None, title="id Пользователя", example=1)

    @classmethod
    def from_request(cls, data: dict, user: User):
        if user:
            data["user_id"] = user.id
        else:
            data["user_id"] = None
        return cls(**data)

    @field_validator("budget", "client_name", "client_email", "client_task")
    def check_empty(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        return v

    @field_validator("client_phone")
    def phone_validation(cls, v):
        if len(v) > 20:
            raise ValueError("Номер телефона не может быть длиннее 20 символов")
        phone_regex = re.compile(r"^\+\d{1,3} \(\d{3}\) \d{3}-\d{2}-\d{2}$")
        if not phone_regex.match(v):
            raise ValueError("Неверный формат телефона")
        return v

    @field_validator("client_email")
    def email_validation(cls, v):
        if len(v) > 124:
            raise ValueError("Email не может быть длиннее 124 символов")
        return v

    @field_validator("company_did", "client_company")
    def company_validate(cls, v):
        if len(v) > 1024:
            raise ValueError("Field so long")
        return v


class BriefUpdate(BriefServices, BriefBase):
    pass


class BriefCreate(BriefServices, BriefBase):
    pass


class BriefRead(BriefServices, BriefBase):
    id: int = Field("1", title="id Брифа", example="1")
