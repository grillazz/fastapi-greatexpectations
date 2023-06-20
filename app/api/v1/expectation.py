from fastapi import APIRouter, Request, Body
from fastapi.responses import PlainTextResponse
from great_expectations.exceptions.exceptions import (
    InvalidExpectationConfigurationError,
)
from app.config import settings
from app.utils.logging import AppLogger

logger = AppLogger.__call__().get_logger()

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
    table: str, expectation_type: str, request: Request,
    gx_mapping: dict = Body(
        None,
        description="pass parameters as json dict and in next step unpack to **mapping",
    ),
):
    _gx = request.app.state.gx

    _gx.set_asset(table_name=table)

    _validator = _gx.context.get_validator(
        datasource_name=settings.sql_datasource_name, data_asset_name=_gx.sql_table_asset.name
    )

    try:
        return eval(f"_validator.{expectation_type}(**gx_mapping)")
    except InvalidExpectationConfigurationError as e:
        return e.__dict__
    except Exception as e:
        logger.error(f"Error: {e}")
        return e.__dict__


@router.get("/doc_expectation/{table}/{expectation_type}", response_class=PlainTextResponse)
def doc_expectation(
    table: str, expectation_type: str, request: Request,
):
    _gx = request.app.state.gx

    _gx.set_asset(table_name=table)

    _validator = _gx.context.get_validator(
        datasource_name=settings.sql_datasource_name, data_asset_name=_gx.sql_table_asset.name
    )

    try:
        _doc = eval(f"_validator.{expectation_type}.__doc__")
        return _doc
    except Exception as e:
        logger.error(f"Error: {e}")
        return e.__dict__


# TODO: endpoint to create expectation suite >
#  should keep expectation suite in memory and update it with each call
#  unless reset or implicit reset after save to database
