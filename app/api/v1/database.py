from typing import List

from fastapi import APIRouter, Depends
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy import inspect
from sqlalchemy.engine import Engine

from app.database import get_db

router = APIRouter(prefix="/v1/database")


@router.get("/schemas")
async def get_database_schemas(sql_engine: Engine = Depends(get_db)) -> List[str]:
    inspected = inspect(sql_engine)
    return inspected.get_schema_names()


@router.get("/tables")
async def get_schema_tables(
    sql_db_schema: str, sql_engine: Engine = Depends(get_db)
) -> List[str]:
    inspected = inspect(sql_engine)
    return inspected.get_table_names(schema=sql_db_schema)


@router.get("/columns")
async def get_table_columns(
    database_schema: str,
    schema_table: str,
    sql_engine: Engine = Depends(get_db),
) -> List[dict]:
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    return db.columns
