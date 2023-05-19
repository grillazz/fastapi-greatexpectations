from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.config import settings
from app.main import app
from app.service import GxSession


@pytest.fixture
def client() -> Generator:
    with TestClient(
        app=app,
        base_url="http://testserver",
    ) as test_client:
        app.state.gx = GxSession(settings.pg_url.__str__(), "my_gx")
        yield test_client
