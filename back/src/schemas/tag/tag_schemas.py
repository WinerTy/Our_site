from pydantic import BaseModel, Field, field_validator


class TagBase(BaseModel):
    name: str = Field("Sites", title="Название Тэга", example="Sites")

    @field_validator("name")
    def validate_text(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        if len(v) > 124:
            raise ValueError("Field so long, max size 512")
        return v


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class TagRead(TagBase):
    id: int
