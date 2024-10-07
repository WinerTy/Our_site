from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin import DropDown, I18nConfig
from starlette_admin.views import Link
from src.config.site.settings import settings
from src.config.database.helper import db_helper
from src.models.note import Note
from src.models.user import User
from src.models.brief import Brief
from src.models.services import Service
from src.models.additional_service import AdditionalService
from src.models.tag import Tag


def get_admin_application() -> Admin:
    admin_app = Admin(
        db_helper.engine,
        title="SITE PROTOTYPE",
        # auth_provider=MyAuthProvider(),
        i18n_config=I18nConfig(default_locale="ru"),
    )
    admin_app.add_view(ModelView(User))
    admin_app.add_view(ModelView(Tag))
    admin_app.add_view(ModelView(Note))
    admin_app.add_view(ModelView(Brief))
    admin_app.add_view(Link(label="Home Page", icon="fa fa-link", url="/"))
    admin_app.add_view(
        DropDown(
            "Услуги",
            icon="fa fa-list",
            views=[ModelView(Service), ModelView(AdditionalService)],
        )
    )
