from great_expectations.dataset import SqlAlchemyDataset
import sqlalchemy as sa

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
