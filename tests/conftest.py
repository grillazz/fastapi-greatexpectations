from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client() -> Generator:
    with TestClient(
        app=app,
        base_url="http://testserver",
    ) as test_client:
        yield test_client
