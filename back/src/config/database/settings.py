from typing import Optional

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    IS_DEV: bool = True
    SQLITE_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DB_ECHO_LOG: bool = False

    @property
    def sqlite_url(self) -> Optional[str]:
        return f"sqlite+aiosqlite:///{self.SQLITE_DB}"

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings_db = ConfigDataBase()
