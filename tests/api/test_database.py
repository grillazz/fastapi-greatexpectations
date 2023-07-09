import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "response_data, status_code",
    (
        (
                [
                    "db_accessadmin",
                    "db_backupoperator",
                    "db_datareader",
                    "db_datawriter",
                    "db_ddladmin",
                    "db_denydatareader",
                    "db_denydatawriter",
                    "db_owner",
                    "db_securityadmin",
                    "dbo",
                    "guest",
                    "HumanResources",
                    "INFORMATION_SCHEMA",
                    "Person",
                    "Production",
                    "Purchasing",
                    "Sales",
                    "sys"
                ],
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
                [
                    "Address",
                    "AddressType",
                    "BusinessEntity",
                    "BusinessEntityAddress",
                    "BusinessEntityContact",
                    "ContactType",
                    "CountryRegion",
                    "EmailAddress",
                    "Password",
                    "Person",
                    "PersonPhone",
                    "PhoneNumberType",
                    "StateProvince"
                ],
            status.HTTP_200_OK,
        ),
    ),
)
def test_get_tables(client: TestClient, response_data: dict, status_code: int):
    response = client.get("/v1/database/tables?sql_db_schema=Person")
    assert response.status_code == status_code
    assert sorted(response.json()) == sorted(response_data)

# TODO: fix this test
# @pytest.mark.parametrize(
#     "response_data, status_code",
#     (
#         (
#             ["id", "work_id", "section_number", "chapter_number", "description"],
#             status.HTTP_200_OK,
#         ),
#     ),
# )
# def test_get_columns(client: TestClient, response_data: dict, status_code: int):
#     response = client.get("/v1/database/columns/chapter")
#     assert response.status_code == status_code
#     assert response.json() == response_data
