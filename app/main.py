from fastapi import FastAPI

from app.api.v1.database import router as database_router
from app.api.v1.expectation import router as gx_router
from app.api.v1.validation import router as val_router
from app.database import start_db

app = FastAPI(title="Otoroshi API")

app.include_router(database_router)
app.include_router(gx_router)
app.include_router(val_router)


@app.on_event("startup")
def startup_event():
    start_db()
