from fastapi import Depends, FastAPI, HTTPException, Request, Response
from great_expectations.dataset import SqlAlchemyDataset

from .database import session, engine

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = session()
        request.state.db.engine = engine
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.get("/dupa")
async def try_expectations(
    request: Request
):
    db = SqlAlchemyDataset(
        table_name="chapter",
        engine=request.state.db.engine,
        schema="shakespeare",
    )
    return db.expect_table_row_count_to_equal(1)


# TODO: 1. endpoint to list database schemas
# In [28]: from sqlalchemy import inspect
# In [29]: a = inspect(gx_sql.sql_engine)
# In [30]: a
# Out[30]: <sqlalchemy.dialects.postgresql.base.PGInspector at 0x7fa818789540>
# In [31]: a.get_schema_names()
