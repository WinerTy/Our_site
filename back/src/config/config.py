from pydantic_settings import BaseSettings

from dotenv import load_dotenv


load_dotenv()


class SiteSettings(BaseSettings):
    SECRET: str
    LIFE_TIME: int
    PROJECT_NAME: str
    DEBUG: bool
    VERSION: str
    CORS_ALLOWED_ORIGINS: str
    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_HOST: str
    SMTP_PORT: int
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    CELERY_NUMBER_OF_WORKERS: int


settings = SiteSettings()
