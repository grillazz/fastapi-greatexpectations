import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "payload, response_data, status_code",
    (
        (
            "{}",
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
        data=payload,
    )
    assert response.status_code == status_code
    assert response.json() == response_data


@pytest.mark.parametrize(
    "payload, response_data, status_code",
    (
        (
            '{"value": 1}',
            '{}',
            status.HTTP_200_OK,
        ),
    ),
)
def test_try_expectation(
    client: TestClient, payload: dict, response_data: dict, status_code: int
):
    response = client.post(
        "/v1/expectation/try/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter",
        data=payload
    )
    print(response.json())
    assert False
    # assert response.status_code == status_code
    # assert response.json() == response_data
