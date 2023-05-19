from fastapi import APIRouter, Request
from great_expectations.exceptions.exceptions import (
    InvalidExpectationConfigurationError,
)
from app.config import settings
from app.service import GxSessionTable, GxSession


router = APIRouter(prefix="/v1/expectation")


@router.post("/try_expectation/{datasource}/{table}/{expectation_type}")
def try_expectation(
    datasource: str, table: str, expectation_type: str, request: Request
):
    _gx = request.app.state.gx

    _gx.set_asset(table_name=table)

    _validator = _gx.context.get_validator(
        datasource_name=datasource, data_asset_name=_gx.sql_table_asset.name
    )

    try:
        return eval(f"_validator.{expectation_type}()")
    except InvalidExpectationConfigurationError as e:
        return e.__dict__


@router.get("/list_available_expectation_types")
def list_available_expectation_types():
    # TODO: pass gx session as dependency or if not possible create new one
    datasource_name = "my_gx"
    table_name = "chapter"
    data_asset_name = "my_gx_asset"
    _gx_session = GxSessionTable(settings.pg_url.__str__()+"?options=-csearch_path=shakespeare", datasource_name, table_name)

    _validator = _gx_session.context.get_validator(
        datasource_name="my_gx", data_asset_name="chapter_asset"
    )

    return _validator.list_available_expectation_types()
