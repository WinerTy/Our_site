from fastapi import Depends, FastAPI
import uvicorn
from .models.base_model import Base
from .config.database.db_helper import db_helper
from .schemas.user_schema import UserRead, UserCreate

from sqlalchemy.ext.asyncio import AsyncSession
from .models.user_model import User
from sqlalchemy.future import select
from .config.database.db_settings import settings_db

print(settings_db.SQLITE_DB)

app = FastAPI()


async def get_session() -> AsyncSession:
    async with db_helper.get_db_session() as session:
        yield session


@app.on_event("startup")
async def startup():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    db_user = User(**user.dict())
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


@app.get("/users/", response_model=list[UserRead])
async def read_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
