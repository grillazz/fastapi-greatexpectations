from typing import Generator

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.models.base import Base

url = "postgresql://user:secret@db:5432/gxshakezz"

# query_cache_size=0 will disable sqlalchemy cache
# engine = create_engine(url, echo=True, echo_pool=True, query_cache_size=0)
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


# In [40]: from sqlalchemy.ext.automap import automap_base
# In [41]: Base = automap_base()
# In [42]: Base.prepare(engine, reflect=True, schema='shakespeare')
# In [43]: c = Base.classes.chapter
# In [44]: c.__table__
# Out[44]: Table('chapter', MetaData(), Column('id', INTEGER(), table=<chapter>, primary_key=True, nullable=False), Column('work_id', VARCHAR(length=32), ForeignKey('shakespeare.work.id'), table=<chapter>, nullable=False), Column('section_number', INTEGER(), table=<chapter>, nullable=False), Column('chapter_number', INTEGER(), table=<chapter>, nullable=False), Column('description', VARCHAR(length=256), table=<chapter>, nullable=False), schema='shakespeare')
