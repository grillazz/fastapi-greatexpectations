# TODO: add POST validation endpoint
# TODO: get expectation suite from db
# TODO: db.validation()

# def validate(
#         self,
#         expectation_suite=expectation suite as JSON from db
#         run_id=None,
#         data_context=None,
#         evaluation_parameters=None,
#         catch_exceptions=True,
#         result_format=None,
#         only_return_failures=False,
#         run_name=None,
#         run_time=None,
# ):
#
# run as background task
# build model with find and validate meths
from enum import Enum

# Query, Body as data class with slots with swagger docs ???
from fastapi import APIRouter, Body, Depends, status
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import get_db, get_db_session
from app.models.expectation import ExpectationStore
from app.schemas.expectation import ExpectationSuiteSchema

router = APIRouter(prefix="/v1/validation")


@router.post("/run/{database_schema}/{schema_table}/{suite_name}")
def run_validation(
    database_schema: str,
    schema_table: str,
    suite_name: str,
    sql_engine: Engine = Depends(get_db),
    sql_session: Session = Depends(get_db_session),
):
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    suite: ExpectationSuiteSchema = ExpectationStore.find_by_name(sql_session, suite_name)
    return db.validate(expectation_suite=suite.value)
