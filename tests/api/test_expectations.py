import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "payload, response_data, status_code",
    (
            (
                    {},
                    "TypeError(\"Dataset.expect_table_row_count_to_equal() missing 1 required positional argument: 'value'\")",
                    status.HTTP_200_OK,
            ),
    ),
)
def test_try_expectation_empty_payload(
        client: TestClient, payload: dict, response_data: str, status_code: int
):
    response = client.post(
        "/v1/expectation/try/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter",
        json=payload
    )
    assert response.status_code == status_code
    assert response.json() == response_data


@pytest.mark.parametrize(
    "payload, response_data, status_code",
    (
            (
                    {"value": 1},
                    {
                        "success": False,
                        "expectation_config": {
                            "_expectation_type": "expect_table_row_count_to_equal",
                            "_kwargs": {
                                "value": 1,
                                "result_format": "BASIC"
                            },
                            "_raw_kwargs": None,
                            "meta": {},
                            "success_on_last_run": None,
                            "_ge_cloud_id": None,
                            "_expectation_context": None,
                            "_rendered_content": None
                        },
                        "result": {
                            "observed_value": 945
                        },
                        "meta": {},
                        "exception_info": {
                            "raised_exception": False,
                            "exception_traceback": None,
                            "exception_message": None
                        },
                        "rendered_content": None
                    },
                    status.HTTP_200_OK,
            ),
            (
                    {"value": 945},
                    {
                        "success": True,
                        "expectation_config": {
                            "_expectation_type": "expect_table_row_count_to_equal",
                            "_kwargs": {
                                "value": 945,
                                "result_format": "BASIC"
                            },
                            "_raw_kwargs": None,
                            "meta": {},
                            "success_on_last_run": None,
                            "_ge_cloud_id": None,
                            "_expectation_context": None,
                            "_rendered_content": None
                        },
                        "result": {
                            "observed_value": 945
                        },
                        "meta": {},
                        "exception_info": {
                            "raised_exception": False,
                            "exception_traceback": None,
                            "exception_message": None
                        },
                        "rendered_content": None
                    },
                    status.HTTP_200_OK,
            ),
    ),
)
def test_try_expectation(
        client: TestClient, payload: dict, response_data: dict, status_code: int
):
    response = client.post(
        "/v1/expectation/try/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter",
        json=payload
    )
    assert response.status_code == status_code
    assert response.json() == response_data
