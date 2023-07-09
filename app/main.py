from fastapi import FastAPI

from app.api.v1.database import router as database_router
from app.api.v1.expectation import router as gx_router

# from app.api.v1.validation import router as val_router
from app.config import settings
from app.database import start_db
from app.utils.logging import AppLogger
from app.service import GxSession

logger = AppLogger.__call__().get_logger()

app = FastAPI(title="Guardian API")

app.include_router(database_router)
app.include_router(gx_router)
# app.include_router(val_router)


@app.on_event("startup")
def startup_event():
    logger.info("Starting up...")
    logger.info(f"Connecting to database...{settings.sqlserver_url.__str__()}")
    app.state.gx = GxSession(
        settings.sqlserver_url.__str__(),
        settings.sql_datasource_name,
    )
    start_db()
