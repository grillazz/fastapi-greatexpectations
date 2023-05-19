from fastapi import APIRouter, Depends, Request

# from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy import inspect
from sqlalchemy.engine import Engine

from app.database import get_db

router = APIRouter(prefix="/v1/database")


@router.get("/schemas")
async def get_database_schemas(sql_engine: Engine = Depends(get_db)) -> list[str]:
    inspected = inspect(sql_engine)
    return inspected.get_schema_names()


@router.get("/tables")
async def get_schema_tables(
    sql_db_schema: str, sql_engine: Engine = Depends(get_db)
) -> list[str]:
    inspected = inspect(sql_engine)
    return inspected.get_table_names(schema=sql_db_schema)


@router.get("/columns/{datasource}/{table}")
def get_table_columns(datasource: str, table: str, request: Request):
    _gx = request.app.state.gx

    _gx.set_asset(table_name=table)

    _validator = _gx.context.get_validator(
        datasource_name=datasource, data_asset_name=_gx.sql_table_asset.name
    )

    return _validator.columns()
