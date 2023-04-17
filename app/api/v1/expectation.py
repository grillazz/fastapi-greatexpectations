from enum import Enum

from fastapi import APIRouter, Body, Depends, status, Query
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import get_db, get_db_session
from app.models.expectation import ExpectationStore
from app.schemas.expectation import ExpectationSuiteSchema

router = APIRouter(prefix="/v1/expectation")


class GxFuncModel(str, Enum):
    expect_table_row_count_to_equal = "expect_table_row_count_to_equal"
    expect_table_column_count_to_be_between = "expect_table_column_count_to_be_between"
    expect_column_values_to_not_be_null = "expect_column_values_to_not_be_null"


@router.post("/try/{gx_func}")
def try_expectation(
    gx_func: GxFuncModel,
    database_schema: str = Query(
        description="database schema name", default="shakespeare"
    ),
    schema_table: str = Query(description="schema table name", default="chapter"),
    sql_engine: Engine = Depends(get_db),
    gx_mapping: dict = Body(
        None,
        description="pass parameters as json dict and in next step unpack to **mapping",
    ),
):
    data_set = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    try:
        return eval(f"data_set.{gx_func.value}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()


@router.post(
    "/add/{gx_func}",
    status_code=status.HTTP_201_CREATED,
    response_model=ExpectationSuiteSchema,
)
def add_expectation(
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
    data_set = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )

    # TODO: if suite for name already exists in database get it and update ?
    data_set.expectation_suite_name = suite_name
    try:
        eval(f"data_set.{gx_func.value}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()
    # TODO: if suite exist db.append_expectation() and update existing suite in database
    gx_suite = data_set.get_expectation_suite(discard_failed_expectations=False)
    expectation = ExpectationStore(
        suite_name=suite_name, suite_desc="", value=gx_suite.to_json_dict()
    )
    expectation.save(sql_session)
    return expectation


@router.get("", response_model=ExpectationSuiteSchema)
async def get_expectation(
    suite_name: str,
    sql_session: Session = Depends(get_db_session),
):
    return ExpectationStore.find_by_name(sql_session, suite_name)
