from fastapi import APIRouter, Depends
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import get_db, get_db_session
from app.models.expectation import ExpectationStore
from app.schemas.expectation import ExpectationSuiteSchema

router = APIRouter(prefix="/v1/validation")


def validate(db: SqlAlchemyDataset, suite: ExpectationSuiteSchema):
    db.validate(expectation_suite=suite.value)


@router.post("/run/{database_schema}/{schema_table}/{suite_name}")
def run_validation(
    database_schema: str,
    schema_table: str,
    suite_name: str,
    sql_engine: Engine = Depends(get_db),
    sql_session: Session = Depends(get_db_session),
):
    db = SqlAlchemyDataset(
        table_name=schema_table, engine=sql_engine, schema=database_schema
    )
    suite: ExpectationSuiteSchema = ExpectationStore.find_by_name(
        sql_session, suite_name
    )
    # TODO: save validation result
    return db.validate(expectation_suite=suite.value)
