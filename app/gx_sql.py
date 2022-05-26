import sqlalchemy as sa
from great_expectations.dataset import SqlAlchemyDataset

connection_url = "postgresql://user:secret@db:5432/gxshakezz"
sql_engine = sa.create_engine(url=connection_url, echo=True)

db = SqlAlchemyDataset(
    table_name="chapter",
    engine=sql_engine,
    schema="shakespeare",
)

# TODO: example expectation gx_sql.db.expect_table_row_count_to_equal(1)

# TODO: 1. endpoint to list database schemas
# In [28]: from sqlalchemy import inspect
# In [29]: a = inspect(gx_sql.sql_engine)
# In [30]: a
# Out[30]: <sqlalchemy.dialects.postgresql.base.PGInspector at 0x7fa818789540>
# In [31]: a.get_schema_names()

# TODO 2. endpoint to list database tables for schemas
# In [33]: a.get_table_names(schema="shakespeare")
# Out[33]: ['wordform', 'work', 'chapter', 'character', 'character_work', 'paragraph']

# TODO 3.
# 3. endpoint to accept schema / tabel and expectation to return validation result

# TODO 4. db session via middleware

# # TODO 5. to save expectation suite
# In [1]: from app import gx_sql
# In [2]: a = gx_sql.db
# In [3]: a.expectation_suite_name = "dupa"
# In [4]: a.expect_table_row_count_to_equal(1)
# In [5]: a.get_expectation_suite(discard_failed_expectations=False)
# Out[5]:
# {
#   "expectation_suite_name": "dupa",
#   "expectations": [
#     {
#       "kwargs": {
#         "value": 1
#       },
#       "expectation_type": "expect_table_row_count_to_equal",
#       "meta": {}
#     }
#   ],
#   "ge_cloud_id": null,
#   "data_asset_type": "Dataset",
#   "meta": {
#     "great_expectations_version": "0.14.8"
#   }
# }
# TODO 6: validate
# In [27]: a.validate()
# Out[27]:
# {
#   "meta": {
#     "great_expectations_version": "0.15.3",
#     "expectation_suite_name": "dupa",
#     "run_id": {
#       "run_time": "2022-05-07T16:46:54.481813+00:00",
#       "run_name": null
#     },
#     "batch_kwargs": {
#       "ge_batch_id": "93f92a20-ce20-11ec-926e-0242ac160003"
#     },
#     "batch_markers": {},
#     "batch_parameters": {},
#     "validation_time": "20220507T164654.481638Z",
#     "expectation_suite_meta": {
#       "great_expectations_version": "0.15.3"
#     }
#   },
#   "success": false,
#   "evaluation_parameters": {},
#   "statistics": {
#     "evaluated_expectations": 1,
#     "successful_expectations": 0,
#     "unsuccessful_expectations": 1,
#     "success_percent": 0.0
#   },
#   "results": [
#     {
#       "result": {
#         "observed_value": 945
#       },
#       "meta": {},
#       "exception_info": {
#         "raised_exception": false,
#         "exception_message": null,
#         "exception_traceback": null
#       },
#       "success": false,
#       "expectation_config": {
#         "kwargs": {
#           "value": 1,
#           "result_format": "BASIC"
#         },
#         "meta": {},
#         "expectation_type": "expect_table_row_count_to_equal"
#       }
#     }
#   ]
# }
#
# In [28]:
