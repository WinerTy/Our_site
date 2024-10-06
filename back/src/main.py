from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from starlette_admin import CustomView, DropDown, I18nConfig
from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin.views import Link

from src.router import get_apps_router
from src.config.site.settings import settings
from src.config.database.helper import db_helper
from src.models.base.base import Base
from src.models.note import Note
from src.models.user import User
from src.models.brief import Brief
from src.models.services import Service
from src.models.additional_service import AdditionalService
from src.models.tag import Tag
from starlette.middleware.sessions import SessionMiddleware
from src.admin.models.tag import AdminTagView


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
    application.add_middleware(SessionMiddleware, secret_key=settings.SECRET)
    application.mount("/static", StaticFiles(directory="src/static"), name="static")
    templates = Jinja2Templates(directory="src/templates")
    application.templates = templates

    return application


app = get_application()
admin = Admin(
    db_helper.engine,
    title="SITE PROTOTYPE",
    # base_url="/admin",
    # route_name="admin",
    # statics_dir="static/admin",
    # templates_dir="templates/admin",
    # auth_provider=MyAuthProvider(),
    i18n_config=I18nConfig(default_locale="ru", language_switcher=["ru", "en"]),
)

admin.add_view(ModelView(User))
admin.add_view(AdminTagView(Tag, icon="fa-solid fa-tags"))
admin.add_view(
    DropDown(
        "Список Услуг",
        icon="fa fa-list",
        views=[
            ModelView(Service, name="Услугу", label="Услуги"),
            ModelView(AdditionalService, name="Доп.Услугу", label="Доп.Услуги"),
        ],
    )
)
admin.add_view(ModelView(Note))
admin.add_view(ModelView(Brief))


@app.on_event("startup")
async def startup():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


admin.mount_to(app)
