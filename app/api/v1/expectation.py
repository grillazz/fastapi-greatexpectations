from enum import Enum

from fastapi import APIRouter, Body, Depends, status
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


@router.get("/try/{gx_func}")
def try_expectation(
    gx_func: GxFuncModel,
    database_schema: str,
    schema_table: str,
    sql_engine: Engine = Depends(get_db),
    gx_mapping: dict = Body(
        None,
        description="pass parameters as json dict and in next step unpack to **mapping",
    ),
):
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    try:
        return eval(f"db.{gx_func}(**gx_mapping)")
    except TypeError as e:
        return e.__repr__()


@router.post(
    "/add/{gx_func}",
    status_code=status.HTTP_201_CREATED,
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
    # if suite existst db.append_expectation() and update existsing suite in database
    gx_suite = db.get_expectation_suite(discard_failed_expectations=False)
    expectation_store = ExpectationStore(
        suite_name=suite_name, suite_desc="", value=gx_suite.to_json_dict()
    )
    expectation_store.save(sql_session)


@router.get("", response_model=ExpectationSuiteSchema)
async def get_expectation(
    suite_name: str,
    sql_session: Session = Depends(get_db_session),
):
    return ExpectationStore.find_by_name(sql_session, suite_name)
