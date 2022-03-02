from great_expectations.dataset import SqlAlchemyDataset
from great_expectations.execution_engine import SqlAlchemyExecutionEngine
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

connection_url = "postgresql://user:secret@db:5432/gxshakezz"
aio_connection_url = "postgresql+asyncpg://user:secret@db:5432/gxshakezz"
sql_engine = sa.create_engine(url=connection_url, echo=True)

aio_sql_engine = create_async_engine(url=aio_connection_url)
from .database import session
# e = SqlAlchemyExecutionEngine(
#
# )


db = SqlAlchemyDataset(
    table_name="chapter",
    engine=sql_engine,
    # custom_sql="select * from shakespeare.chapter",
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