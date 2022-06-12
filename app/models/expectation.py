import uuid

from sqlalchemy import Column, String, select
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import Session

from .base import Base


class ExpectationStore(Base):
    __tablename__ = "expectation"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    suite_name = Column(String, nullable=False, unique=False)
    suite_desc = Column(String, nullable=False, unique=False)
    value = Column(MutableDict.as_mutable(JSONB), nullable=False)

    def __init__(
        self,
        suite_name: str,
        suite_desc: str,
        value: JSONB,
    ):
        self.suite_name = suite_name
        self.suite_desc = suite_desc
        self.value = value

    @classmethod
    def find_by_name(cls, db: Session, suite_name: str):
        stmt = select(cls).where(cls.suite_name == suite_name)
        return db.execute(stmt).scalars().first()
