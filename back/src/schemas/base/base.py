from pydantic import Field, BaseModel


class BaseResponse(BaseModel):
    id: int = Field(1, title="id Доп.Услуги", example="1")
    detail: str = Field("succses", title="Ответ Сервера", example="1")
