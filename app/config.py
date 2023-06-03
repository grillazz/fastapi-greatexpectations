import os
from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_url: PostgresDsn = PostgresDsn.build(
        scheme="postgresql",
        user=os.getenv("SQL_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("SQL_HOST"),
        port="5432",
        path=f"/{os.getenv('SQL_DB') or ''}",
    )
    pg_url_csearch_path: str = os.getenv("SQL_CSEARCH_PATH")
    sql_datasource_name: str = os.getenv("SQL_DATASOURCE_NAME", "default")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
