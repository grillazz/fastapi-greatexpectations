import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "response_data, status_code",
    (
        (
            ["information_schema", "public", "shakespeare"],
            status.HTTP_200_OK,
        ),
    ),
)
def test_get_schemas(client: TestClient, response_data: dict, status_code: int):
    response = client.get("/v1/database/schemas")
    assert response.status_code == status_code
    assert response.json() == response_data


@pytest.mark.parametrize(
    "response_data, status_code",
    (
        (
            ["paragraph", "wordform", "character", "character_work", "work", "chapter"],
            status.HTTP_200_OK,
        ),
    ),
)
def test_get_tables(client: TestClient, response_data: dict, status_code: int):
    response = client.get("/v1/database/tables?sql_db_schema=shakespeare")
    assert response.status_code == status_code
    assert sorted(response.json()) == sorted(response_data)


@pytest.mark.parametrize(
    "response_data, status_code",
    (
        (
            ["id", "work_id", "section_number", "chapter_number", "description"],
            status.HTTP_200_OK,
        ),
    ),
)
def test_get_columns(client: TestClient, response_data: dict, status_code: int):
    response = client.get("/v1/database/columns/chapter")
    assert response.status_code == status_code
    assert response.json() == response_data
