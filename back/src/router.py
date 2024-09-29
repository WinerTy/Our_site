from fastapi import APIRouter
from src.api.routers.note_router import router as note_router
from src.dependencies import fastapi_users, auth_backend
from src.schemas.user_schemas import UserRead, UserCreate, UserUpdate


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
    return router
