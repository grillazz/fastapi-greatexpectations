from enum import Enum

# Query, Body as data class with slots with swagger docs ???
from fastapi import APIRouter, Body, Depends, Query
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy import inspect
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import engine, get_db, get_db_session
from app.models.expectation import ExpectationStore

router = APIRouter(prefix="/v1/gx")


# TODO: every expect fn should suggest adequate example payload
class GxFuncModel(str, Enum):
    expect_table_row_count_to_equal = "expect_table_row_count_to_equal"
    expect_multicolumn_sum_to_equal = "expect_multicolumn_sum_to_equal"


@router.post("/try/{gx_func}")
def try_expectations(
    # should be validated as pydantic allow names or maybe dataclass with slots ??? 4 times faster than pydantic
    gx_func: GxFuncModel,
    database_schema: str,
    schema_table: str,
    sql_engine: Engine = Depends(get_db),
    sql_session: Session = Depends(get_db_session),
    suite_name: str = Query(
        None,
        description="if suite name is not empty this mean expectation will be save",
    ),
    gx_mapping: dict = Body(
        None,
        description="pass parameters as json dict and in next step unpack to **mapping",
    ),
):
    # TODO: can be singleton ?
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )

    if suite_name:
        # TODO: if suite for name already exists in database get it and update ?
        db.expectation_suite_name = suite_name
        eval(f"db.{gx_func}(**gx_mapping)")
        gx_suite = db.get_expectation_suite(discard_failed_expectations=False)
        expectation_store = ExpectationStore(
            suite_name=suite_name, suite_desc="balblabla", value=gx_suite.to_json_dict()
        )
        expectation_store.save(sql_session)

        # save to model

    # return db.expect_table_row_count_to_equal(1)
    # TODO: try catch
    #  TypeError: Dataset.expect_multicolumn_sum_to_equal() missing 2 required positional arguments: 'column_list' and 'sum_total'
    try:
        return eval(f"db.{gx_func}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()
