import os

from pydantic_core import Url
from pydantic_settings import BaseSettings


class SqlServerUrl(Url):
    allowed_schemes = {
        "mssql+pyodbc",
    }
    user_required = True
    password_required = True
    host_required = True


class Settings(BaseSettings):
    sqlserver_url: SqlServerUrl = SqlServerUrl.build(
        scheme="mssql+pyodbc",
        username=os.getenv("MSSQL_USER"),
        password=os.getenv("MSSQL_SA_PASSWORD"),
        host=os.getenv("MSSQL_HOST"),
        port=1433,
        path=f"{os.getenv('MSSQL_DB') or ''}",
        query="driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes",
    )
    sql_datasource_name: str = os.getenv("SQL_DATASOURCE_NAME", "default")


settings = Settings()
