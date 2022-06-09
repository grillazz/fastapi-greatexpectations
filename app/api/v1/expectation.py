from enum import Enum

# Query, Body as data class with slots with swagger docs ???
from fastapi import APIRouter, Body, Depends, status
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import get_db, get_db_session
from app.models.expectation import ExpectationStore

router = APIRouter(prefix="/v1/expectation")


# TODO: every expect fn should suggest adequate example payload
# TODO: change this to smart model with expectation name and example parameters
class GxFuncModel(str, Enum):
    expect_table_row_count_to_equal = "expect_table_row_count_to_equal"
    expect_table_column_count_to_be_between = "expect_table_column_count_to_be_between"


@router.get("/try/{gx_func}")
def try_expectation(
        # should be validated as pydantic allow names or maybe dataclass with slots ??? 4 times faster than pydantic
        gx_func: GxFuncModel,
        database_schema: str,
        schema_table: str,
        sql_engine: Engine = Depends(get_db),
        gx_mapping: dict = Body(
            None,
            description="pass parameters as json dict and in next step unpack to **mapping",
        ),
):
    # TODO: can be singleton ?
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    try:
        return eval(f"db.{gx_func}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()


@router.post("/add/{gx_func}", status_code=status.HTTP_201_CREATED, )
def add_expectation(
        # should be validated as pydantic allow names or maybe dataclass with slots ??? 4 times faster than pydantic
        gx_func: GxFuncModel,
        database_schema: str,
        schema_table: str,
        suite_name: str,
        sql_engine: Engine = Depends(get_db),
        sql_session: Session = Depends(get_db_session),
        gx_mapping: dict = Body(
            None,
            description="pass parameters as json dict and in next step unpack to **mapping",
        ),
):
    # TODO: can be singleton ?
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )

    # TODO: if suite for name already exists in database get it and update ?
    db.expectation_suite_name = suite_name
    try:
        eval(f"db.{gx_func}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()
    # db.append_expectation()
    gx_suite = db.get_expectation_suite(discard_failed_expectations=False)
    expectation_store = ExpectationStore(
        suite_name=suite_name, suite_desc="", value=gx_suite.to_json_dict()
    )
    expectation_store.save(sql_session)

# TODO: get suite by id or name
# TODO: get all suites

