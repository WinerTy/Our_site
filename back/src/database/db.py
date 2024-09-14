from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from ..config.database.db_helper import db_helper
from ..models.user_model import User


async def get_session() -> AsyncSession:
    async with db_helper.get_db_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)
