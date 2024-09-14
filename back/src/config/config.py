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


settings = SiteSettings()
