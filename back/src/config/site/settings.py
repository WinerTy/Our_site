from pydantic_settings import BaseSettings


class SiteSettings(BaseSettings):
    SECRET: str
    LIFE_TIME: int
    PROJECT_NAME: str
    DEBUG: bool
    VERSION: str
    CORS_ALLOWED_ORIGINS: str


settings = SiteSettings()
