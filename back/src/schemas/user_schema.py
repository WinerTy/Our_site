from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserSub(UserBase):
    id: int


class UserCreate(UserBase):
    name: str
    email: str


class UserRead(UserBase):
    id: int
    name: str
    email: str
