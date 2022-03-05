from fastapi import Depends, FastAPI, HTTPException, Request, Response
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from enum import Enum

from .database import session, engine

app = FastAPI()


class GxFuncModel(str, Enum):
    expect_table_row_count_to_equal = "expect_table_row_count_to_equal"


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        # request.state.db = session()
        request.state.db_engine = engine
        response = await call_next(request)
    finally:
        # request.state.db.close()
        pass
    return response


# Dependency
def get_db(request: Request):
    return request.state.db_engine

# TODO: add enum with expectations as available parameters

@app.post("/dupa/{gx_func}")
async def try_expectations(
    c: int, # pass parameters as json dict and in next step unpack to **mapping
    gx_func: GxFuncModel,
    request: Request,
    engine: Engine = Depends(get_db),

):
    # TODO: can be singleton
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
        fn = "db."+gx_func
        e = eval(fn)
        return e
    except TypeError as e:
        return e.__repr__()

# TODO: 1. endpoint to list database schemas
# In [28]: from sqlalchemy import inspect
# In [29]: a = inspect(gx_sql.sql_engine)
# In [30]: a
# Out[30]: <sqlalchemy.dialects.postgresql.base.PGInspector at 0x7fa818789540>
# In [31]: a.get_schema_names()
# https://docs.greatexpectations.io/docs/reference/expectations/conditional_expectations
#
# In [19]: a.get_expectation_suite(
#     ...:   discard_failed_expectations=False
#     ...: )
# Out[19]:
# {
#   "expectations": [
#     {
#       "meta": {},
#       "kwargs": {
#         "value": 1
#       },
#       "expectation_type": "expect_table_row_count_to_equal"
#     }
#   ],
#   "expectation_suite_name": "default",
#   "meta": {
#     "great_expectations_version": "0.14.8"
#   },
#   "data_asset_type": "Dataset",
#   "ge_cloud_id": null
# }
#
# In [20]:
