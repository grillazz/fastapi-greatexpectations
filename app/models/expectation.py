import uuid

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSONB, UUID

from base import Base


class ExpectationStore(Base):
    # TODO: add ge as schema
    __tablename__ = "expectation"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    suite_name = Column(String, nullable=False, unique=False)
    suite_desc = Column(String, nullable=False, unique=False)
    value = Column(MutableDict.as_mutable(JSONB), nullable=False)

    def __init__(
            self,
            suite_name: str,
            suite_decs: str,
            value: JSONB,
    ):
        self.suite_name = suite_name
        self.suite_desc = suite_decs
        self.value = value
