import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    sql_user: str
    postgres_password: str
    sql_host: str
    sql_db: str


@lru_cache
def get_settings():
    return Settings()
