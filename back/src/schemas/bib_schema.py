from pydantic import BaseModel


from typing import Optional


class BibCreate(BaseModel):
    text: str
    user_id: Optional[int] = None


class BibResponse(BaseModel):
    id: int
    text: str
    user_id: Optional[int] = None
