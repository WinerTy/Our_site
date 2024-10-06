# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates


# from src.router import get_apps_router
# from src.config.site.settings import settings

# from starlette.middleware.sessions import SessionMiddleware


# def get_application() -> FastAPI:
#     application = FastAPI(
#         title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION
#     )
#     application.include_router(get_apps_router())

#     application.add_middleware(
#         CORSMiddleware,
#         allow_origins=settings.CORS_ALLOWED_ORIGINS,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
#     application.add_middleware(SessionMiddleware, secret_key=settings.SECRET)
#     application.mount("/static", StaticFiles(directory="src/static"), name="static")
#     templates = Jinja2Templates(directory="src/templates")
#     application.templates = templates

#     return application
