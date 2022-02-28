from great_expectations.dataset import SqlAlchemyDataset
from great_expectations.execution_engine import SqlAlchemyExecutionEngine
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

connection_url = "postgresql://user:secret@db:5432/gxshakezz"
aio_connection_url = "postgresql+asyncpg://user:secret@db:5432/gxshakezz"
sql_engine = sa.create_engine(url=connection_url, echo=True)

aio_sql_engine = create_async_engine(url=aio_connection_url)

# e = SqlAlchemyExecutionEngine(
#
# )


db = SqlAlchemyDataset(
    table_name="chapter",
    engine=sql_engine,
    custom_sql="select * from shakespeare.chapter",
    schema="shakespeare",
)

# TODO: example expectation gx_sql.db.expect_table_row_count_to_equal(1)

# 1. endpoint to list database schemas
# 2. endpoint to list database tables for schemas
# 3. endpoint to accept schema / tabel and expectation to return validation result
