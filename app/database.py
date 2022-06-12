from typing import Generator

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.models.base import Base

url = "postgresql://user:secret@db:5432/gxshakezz"

engine = create_engine(url, echo=True, echo_pool=True)

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
def get_db():
    return engine


def start_db():
    Base.metadata.create_all(engine)
