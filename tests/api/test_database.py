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
            ["wordform", "work", "chapter", "character", "character_work", "paragraph"],
            status.HTTP_200_OK,
        ),
    ),
)
def test_get_tables(client: TestClient, response_data: dict, status_code: int):
    response = client.get("/v1/database/tables?sql_db_schema=shakespeare")
    assert response.status_code == status_code
    assert response.json() == response_data


@pytest.mark.parametrize(
    "response_data, status_code",
    (
        (
            [
                {
                    "name": "id",
                    "type": {},
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                    "comment": None,
                },
                {
                    "name": "work_id",
                    "type": {
                        "length": 32,
                        "collation": None,
                        "_expect_unicode": False,
                        "_expect_unicode_error": None,
                        "_warn_on_bytestring": False,
                    },
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                    "comment": None,
                },
                {
                    "name": "section_number",
                    "type": {},
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                    "comment": None,
                },
                {
                    "name": "chapter_number",
                    "type": {},
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                    "comment": None,
                },
                {
                    "name": "description",
                    "type": {
                        "length": 256,
                        "collation": None,
                        "_expect_unicode": False,
                        "_expect_unicode_error": None,
                        "_warn_on_bytestring": False,
                    },
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                    "comment": None,
                },
            ],
            status.HTTP_200_OK,
        ),
    ),
)
def test_get_columns(client: TestClient, response_data: dict, status_code: int):
    response = client.get(
        "/v1/database/columns?database_schema=shakespeare&schema_table=chapter"
    )
    assert response.status_code == status_code
    assert response.json() == response_data
