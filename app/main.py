from fastapi import Depends, FastAPI, HTTPException, Request, Response
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

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
    return request.state.db.engine


@app.get("/dupa/{c}")
async def try_expectations(
    c: int,
    request: Request,
    engine: Engine = Depends(get_db)
):
    db = SqlAlchemyDataset(
        table_name="chapter",
        engine=engine,
        schema="shakespeare",
    )
    # return db.expect_table_row_count_to_equal(1)
    # TODO: try catch
    #  TypeError: Dataset.expect_multicolumn_sum_to_equal() missing 2 required positional arguments: 'column_list' and 'sum_total'
    try:
        # return db.expect_multicolumn_sum_to_equal()
        return db.expect_table_row_count_to_equal(c)
    except TypeError as e:
        return e.__repr__()

# TODO: 1. endpoint to list database schemas
# In [28]: from sqlalchemy import inspect
# In [29]: a = inspect(gx_sql.sql_engine)
# In [30]: a
# Out[30]: <sqlalchemy.dialects.postgresql.base.PGInspector at 0x7fa818789540>
# In [31]: a.get_schema_names()
