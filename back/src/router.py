from fastapi import APIRouter
from . import fastapi_users, auth_backend
from .schemas.user_schema import *

from .app.controllers.public.bibs_router import router as bib_router
from .app.controllers.public.service_router import router as service_router


def get_apps_router():
    router = APIRouter()
    router.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth",
        tags=["auth"],
    )
    router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )
    router.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["users"],
    )
    router.include_router(bib_router)
    router.include_router(service_router)
    return router
