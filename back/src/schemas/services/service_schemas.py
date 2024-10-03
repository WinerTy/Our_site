from typing import Optional
from pydantic import BaseModel, field_validator, Field
from src.schemas.tag import TagRead


class ServiceBase(BaseModel):
    name: str = Field(
        "Develop web-site", title="Название услуги", example="Develop web-site"
    )

    @field_validator("name")
    def check_name(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        if len(v) > 124:
            raise ValueError("Field so long, max size 124")
        return v


class ServiceCreate(ServiceBase):
    tag_id: Optional[int] = Field(1, title="id Тэга", example=1)


class ServiceRead(ServiceBase):
    id: int = Field(1, title="id Доп.Услуги", example=1)
    tag: Optional[TagRead] = Field(None, title="Объект Тэга", example={"id": 1})


class ServiceUpdate(ServiceBase):
    is_active: bool = Field(True, title="Услуга активна", example=True)
    tag_id: Optional[int] = Field(1, title="id Тэга", example=1)
