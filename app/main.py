from fastapi import FastAPI, Request, Response

from app.api.v1.database import router as database_router
from app.api.v1.expectation import router as gx_router

from .database import engine, session

app = FastAPI()

app.include_router(database_router)
app.include_router(gx_router)


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
