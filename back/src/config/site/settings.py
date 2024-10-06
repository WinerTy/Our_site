from pydantic_settings import BaseSettings

from dotenv import load_dotenv


load_dotenv()


class SiteSettings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool
    VERSION: str
    CORS_ALLOWED_ORIGINS: str

    SECRET: str
    LIFE_DAYS: int


settings = SiteSettings()
