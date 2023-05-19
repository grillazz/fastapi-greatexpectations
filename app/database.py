from typing import Generator

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.models.base import Base

engine = create_engine(
    settings.pg_url.__str__(),
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
