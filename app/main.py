from fastapi import FastAPI

from app.api.v1.database import router as database_router
from app.api.v1.expectation import router as gx_router

# from app.api.v1.validation import router as val_router
from app.database import start_db
from app.logging import AppLogger
from app.service import GxSession

logger = AppLogger.__call__().get_logger()

app = FastAPI(title="Watchman Service API")

app.include_router(database_router)
app.include_router(gx_router)
# app.include_router(val_router)

# TODO: build from PostgreDSN
url: str = f"postgresql://user:secret@db:5432/gxshakezz"


@app.on_event("startup")
def startup_event():
    app.state.gx = GxSession(url, "my_gx")
    start_db()
