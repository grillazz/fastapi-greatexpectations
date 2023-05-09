from typing import Generator

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app import config
from app.models.base import Base

global_vars = config.get_settings()

url: str = f"postgresql://{global_vars.sql_user}:{global_vars.postgres_password}@{global_vars.sql_host}:5432/{global_vars.sql_db}"

engine = create_engine(
    url,
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db_session() -> Generator:
    # TODO: add logging
    session = SessionLocal()
    try:
        yield session
    except SQLAlchemyError as sql_ex:
        session.rollback()
        raise sql_ex
    except HTTPException as http_ex:
        session.rollback()
        raise http_ex
    finally:
        session.close()


# Dependency
def get_db() -> Generator:
    yield engine


def start_db():
    Base.metadata.create_all(engine)
