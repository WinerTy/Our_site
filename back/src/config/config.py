from pydantic_settings import BaseSettings

from dotenv import load_dotenv


load_dotenv()


class SiteSettings(BaseSettings):
    pass


settings = SiteSettings()
