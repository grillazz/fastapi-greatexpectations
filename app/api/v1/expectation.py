from enum import Enum
# Query, Body as data class with slots with swagger docs ???
from fastapi import APIRouter, Depends, Query, Body
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy import inspect
from sqlalchemy.engine import Engine

from app.database import get_db

router = APIRouter(prefix="/v1/gx")


# TODO: every expect fn should suggest adequate example payload
class GxFuncModel(str, Enum):
    expect_table_row_count_to_equal = "expect_table_row_count_to_equal"
    expect_multicolumn_sum_to_equal = "expect_multicolumn_sum_to_equal"


@router.post("/try/{gx_func}")
async def try_expectations(
    # should be validated as pydantic allow names or maybe dataclass with slots ??? 4 times faster than pydantic
    gx_func: GxFuncModel,
    database_schema: str,
    schema_table: str,
    sql_engine: Engine = Depends(get_db),
    suite_name: str = Query(None, description="if suite name is not empty this mean expectation will be save"),
    gx_mapping: dict = Body(None, description="pass parameters as json dict and in next step unpack to **mapping")
):
    # TODO: can be singleton ?
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )

    if suite_name:
        db.expectation_suite_name = suite_name
        eval(f"db.{gx_func}(**gx_mapping)")
        return db.get_expectation_suite(discard_failed_expectations=False)
        # save to model

    # return db.expect_table_row_count_to_equal(1)
    # TODO: try catch
    #  TypeError: Dataset.expect_multicolumn_sum_to_equal() missing 2 required positional arguments: 'column_list' and 'sum_total'
    try:
        return eval(f"db.{gx_func}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()
