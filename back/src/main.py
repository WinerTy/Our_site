from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


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


@app.on_event("startup")
async def startup():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
