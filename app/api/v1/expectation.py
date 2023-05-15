from enum import Enum

from fastapi import APIRouter, Body, Depends, Query, status
from great_expectations.exceptions.exceptions import InvalidExpectationConfigurationError
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import get_db, get_db_session
from app.models.expectation import ExpectationStore
from app.schemas.expectation import ExpectationSuiteSchema
from app.service import GxSession


router = APIRouter(prefix="/v1/expectation")
url: str = f"postgresql://user:secret@db:5432/gxshakezz"

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
    # data_set = SqlAlchemyataset(
    #     table_name=schema_table, engine=sql_engine, schema=database_schema
    # )

    datasource_name = "my_gx"
    table_name = "chapter"
    data_asset_name =  "my_gx_asset"
    _gx_session = GxSession(url, datasource_name, table_name)

    _validator = _gx_session.context.get_validator(datasource_name="my_gx", data_asset_name="chapter_asset")

    try:
        return eval(f"_validator.{gx_func.value}()")
        # return _validator.expect_column_values_to_not_be_null()
    except InvalidExpectationConfigurationError as e:
        return e.__dict__
#
#
# @router.post(
#     "/add/{gx_func}",
#     status_code=status.HTTP_201_CREATED,
#     response_model=ExpectationSuiteSchema,
# )
# def add_expectation(
#     gx_func: GxFuncModel,
#     database_schema: str,
#     schema_table: str,
#     suite_name: str,
#     sql_engine: Engine = Depends(get_db),
#     sql_session: Session = Depends(get_db_session),
#     gx_mapping: dict = Body(
#         None,
#         description="pass parameters as json dict and in next step unpack to **mapping",
#     ),
# ):
#     data_set = SqlAlchemyDataset(
#         table_name=schema_table, engine=sql_engine, schema=database_schema
#     )
#
#     # TODO: if suite for name already exists in database get it and update ?
#     data_set.expectation_suite_name = suite_name
#     try:
#         eval(f"data_set.{gx_func.value}(**gx_mapping)")
#     except TypeError as e:
#         return e.__repr__()
#     # TODO: if suite exist db.append_expectation() and update existing suite in database
#     gx_suite = data_set.get_expectation_suite(discard_failed_expectations=False)
#     expectation = ExpectationStore(
#         suite_name=suite_name, suite_desc="", value=gx_suite.to_json_dict()
#     )
#     expectation.save(sql_session)
#     return expectation
#
#
# @router.get("", response_model=ExpectationSuiteSchema)
# async def get_expectation(
#     suite_name: str,
#     sql_session: Session = Depends(get_db_session),
# ):
#     return ExpectationStore.find_by_name(sql_session, suite_name)
