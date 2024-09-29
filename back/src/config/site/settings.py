from pydantic_settings import BaseSettings


class SiteSettings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool
    VERSION: str
    CORS_ALLOWED_ORIGINS: str

    SECRET: str
    LIFE_TIME: int


settings = SiteSettings()
