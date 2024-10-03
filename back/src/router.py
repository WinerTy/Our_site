from fastapi import APIRouter

from src.api.routers.note import note_router
from src.api.routers.service import service_router
from src.api.routers.brief import brief_router
from src.api.routers.tag import tag_router

from src.dependencies import fastapi_users, auth_backend
from src.schemas.user import UserRead, UserCreate, UserUpdate


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
    router.include_router(note_router)
    router.include_router(service_router)
    router.include_router(brief_router)
    router.include_router(tag_router)
    return router
