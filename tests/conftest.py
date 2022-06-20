import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    with TestClient(
        app=app,
        base_url="http://testserver/v1",
    ) as test_client:
        yield test_client
