from enum import Enum
from typing import AnyStr, Dict, List

from fastapi import APIRouter, Depends
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy import inspect
from sqlalchemy.engine import Engine

from app.database import get_db

router = APIRouter(prefix="/v1/gx")


class GxFuncModel(str, Enum):
    expect_table_row_count_to_equal = "expect_table_row_count_to_equal"
    expect_multicolumn_sum_to_equal = "expect_multicolumn_sum_to_equal"


@router.post("/try/{gx_func}")
async def try_expectations(
    gx_mapping: Dict,  # pass parameters as json dict and in next step unpack to **mapping /
    # should be validated as pydantic allowe names
    gx_func: GxFuncModel,
    database_schema: str,
    schema_table: str,
    sql_engine: Engine = Depends(get_db),
):
    """

    :param gx_mapping:
    :param gx_func:
    :param database_schema:
    :param schema_table:
    :param sql_engine:
    :return:
    """
    # TODO: can be singleton ?
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    # return db.expect_table_row_count_to_equal(1)
    # TODO: try catch
    #  TypeError: Dataset.expect_multicolumn_sum_to_equal() missing 2 required positional arguments: 'column_list' and 'sum_total'
    try:
        return eval(f"db.{gx_func}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()
