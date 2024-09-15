from .utils.user_manager import get_user_manager
from .models.user_model import User
from .schemas.user_schema import *
from .config.config import settings
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend,
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET, lifetime_seconds=settings.LIFE_TIME)


bearer_transport = BearerTransport(tokenUrl="auth/login")


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True, optional=True)
admin_user = fastapi_users.current_user(superuser=True)
