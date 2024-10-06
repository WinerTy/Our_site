from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Request

from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import MetaData, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.base.base import Base
from src.schemas.note.note_schemas import NoteCreate, NoteRead
from src.schemas.user import UserCreate
from src.schemas.base import BaseResponse
from src.dependencies.auth_depend import admin_user, get_session, current_user
from src.models.user import User

from src.api.repository.note import note_repository
from src.api.repository.user import user_repository
from passlib.context import CryptContext
from src.config.database.helper import db_helper

router = APIRouter(prefix="/admin", tags=["Admin"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", response_class=HTMLResponse)
async def admin_page(request: Request, user: User = Depends(admin_user)):
    if not user:
        return RedirectResponse(url="/admin/login")
    return request.app.templates.TemplateResponse(
        "pages/admin.html", {"request": request, "user": user}
    )


@router.get("/super")
async def create_super(session: AsyncSession = Depends(get_session)):
    email = "Admin@admin.ru"
    password = "Admin"

    # Хешируем пароль
    hashed_password = pwd_context.hash(password)

    try:
        # Проверяем, существует ли уже пользователь с таким email
        existing_user = await session.execute(select(User).where(User.email == email))
        existing_user = existing_user.scalar_one_or_none()

        if existing_user:
            raise HTTPException(
                status_code=400, detail="User with this email already exists"
            )

        # Создаем нового пользователя
        user = User(email=email, hashed_password=hashed_password, is_superuser=True)
        session.add(user)
        await session.commit()
        await session.refresh(user)

        return {"message": "Superuser created successfully", "user": user}

    except HTTPException as e:
        raise e

    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail="An error occurred while creating the superuser"
        )

    finally:
        await session.close()


@router.get("/dashboard")
async def render_dashboard(request: Request):
    data = {"request": request}
    data["models"] = ["Note", "Brief", "Users", "Service"]
    return request.app.templates.TemplateResponse("admin/pages/dashboard.html", data)
