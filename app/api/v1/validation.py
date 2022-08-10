from fastapi import APIRouter, Depends
from great_expectations.dataset import SqlAlchemyDataset
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database import get_db, get_db_session
from app.models.expectation import ExpectationStore
from app.models.validation import ValidationStore
from app.schemas.expectation import ExpectationSuiteSchema

router = APIRouter(prefix="/v1/validation")


@router.post("/run/{database_schema}/{table_name}/{suite_name}")
def run_validation(
    database_schema: str,
    table_name: str,
    suite_name: str,
    sql_engine: Engine = Depends(get_db),
    sql_session: Session = Depends(get_db_session),
):
    data_set = SqlAlchemyDataset(
        table_name=table_name, engine=sql_engine, schema=database_schema
    )
    suite: ExpectationSuiteSchema = ExpectationStore.find_by_name(
        sql_session, suite_name
    )
    validation_result = data_set.validate(expectation_suite=suite.value)  # type: ignore
    validation = ValidationStore(
        db_schema=database_schema,
        db_table=table_name,
        value=validation_result.to_json_dict(),
        expectation_suite_id=suite.id,
    )
    return validation.save(sql_session)
