from fastapi import status
from fastapi.testclient import TestClient


def test_get_stuff(client: TestClient):
    response = client.get("/v1/database/schemas")
    assert response.status_code == status.HTTP_200_OK
