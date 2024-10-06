from fastapi import HTTPException, Request, Depends

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend,
)

from src.config.database.helper import db_helper
from src.config.site.settings import settings
from src.models.user import User

from starlette_admin.auth import AdminUser, AuthProvider
from starlette.requests import Request


async def get_session() -> AsyncSession:
    async with db_helper.get_db_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET, lifetime_seconds=settings.LIFE_DAYS * 86400
    )


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

current_user = fastapi_users.current_user(active=True, optional=True)
admin_user = fastapi_users.current_user(active=True, superuser=True, optional=True)


class MyAuthProvider(AuthProvider):
    async def login(self, username: str, password: str, request: Request) -> bool:
        user = await fastapi_users.authenticator.authenticate(username, password)
        if user and user.is_superuser:
            request.session["user"] = user.id
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.pop("user", None)
        return True

    async def authenticate(self, request: Request) -> AdminUser:
        user_id = request.session.get("user")
        if user_id:
            user = await get_user_manager().get(user_id)
            if user and user.is_superuser:
                return AdminUser(username=user.email)
        return None

    async def is_authenticated(self, request: Request) -> bool:
        return await self.authenticate(request) is not None

    async def get_admin_user(self, request: Request) -> AdminUser:
        user = await self.authenticate(request)
        if user:
            return user
        return None
