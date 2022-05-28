from fastapi import Request, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

url = "postgresql://user:secret@db:5432/gxshakezz"

engine = create_engine(url, echo=False, echo_pool=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db_session():
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


def get_db(request: Request):
    return request.state.db_engine


# In [40]: from sqlalchemy.ext.automap import automap_base
# In [41]: Base = automap_base()
# In [42]: Base.prepare(engine, reflect=True, schema='shakespeare')
# In [43]: c = Base.classes.chapter
# In [44]: c.__table__
# Out[44]: Table('chapter', MetaData(), Column('id', INTEGER(), table=<chapter>, primary_key=True, nullable=False), Column('work_id', VARCHAR(length=32), ForeignKey('shakespeare.work.id'), table=<chapter>, nullable=False), Column('section_number', INTEGER(), table=<chapter>, nullable=False), Column('chapter_number', INTEGER(), table=<chapter>, nullable=False), Column('description', VARCHAR(length=256), table=<chapter>, nullable=False), schema='shakespeare')
