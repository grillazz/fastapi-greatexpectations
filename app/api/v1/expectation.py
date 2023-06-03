from fastapi import APIRouter, Request
from great_expectations.exceptions.exceptions import (
    InvalidExpectationConfigurationError,
)
from app.config import settings

router = APIRouter(prefix="/v1/expectation")


@router.get("/list_available_expectation_types/{table}")
def list_available_expectation_types(table: str, request: Request):
    _gx = request.app.state.gx

    _gx.set_asset(table_name=table)

    _validator = _gx.context.get_validator(
        datasource_name=settings.sql_datasource_name,
        data_asset_name=_gx.sql_table_asset.name
    )

    try:
        return eval(f"_validator.list_available_expectation_types()")
    except InvalidExpectationConfigurationError as e:
        return e.__dict__


@router.post("/try_expectation/{table}/{expectation_type}")
def try_expectation(
    table: str, expectation_type: str, request: Request
):
    _gx = request.app.state.gx

    _gx.set_asset(table_name=table)

    _validator = _gx.context.get_validator(
        datasource_name=settings.sql_datasource_name, data_asset_name=_gx.sql_table_asset.name
    )

    try:
        return eval(f"_validator.{expectation_type}()")
    except InvalidExpectationConfigurationError as e:
        return e.__dict__
