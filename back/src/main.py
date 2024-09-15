from typing import Optional
from fastapi_users import FastAPIUsers
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from .schemas.bib_schema import BibResponse, BibCreate
from .database.db import get_session
from .models.bid_model import Bib

from .router import get_apps_router


from .models.base_model import Base
from .config.database.db_helper import db_helper
from .config.config import settings


app = FastAPI()


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION
    )
    application.include_router(get_apps_router())

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = get_application()


# current_user = fastapi_users.current_user(active=True)


@app.on_event("startup")
async def startup():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/test/", response_model=list[BibResponse])
async def get_bibs(session: AsyncSession = Depends(get_session)):
    try:
        query = select(Bib)
        result = await session.execute(query)
        bibs = result.scalars().all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return bibs


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
