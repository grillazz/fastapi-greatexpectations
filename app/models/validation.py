import uuid

from sqlalchemy import Column, ForeignKey, String, select
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.mutable import MutableDict

from .base import Base


class ValidationStore(Base):
    __tablename__ = "validation"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    db_schema = Column(String, nullable=False, unique=False)
    db_table = Column(String, nullable=False, unique=False)
    value = Column(MutableDict.as_mutable(JSONB), nullable=False)

    expectation_suite_id = Column(
        UUID(as_uuid=True),
        ForeignKey("expectation.id", ondelete="CASCADE"),
        nullable=False,
    )

    def __init__(
        self, db_schema: str, db_table: str, value: JSONB, expectation_suite_id: UUID
    ):
        self.db_schema = db_schema
        self.db_table = db_table
        self.value = value
        self.expectation_suite_id = expectation_suite_id

    @classmethod
    def find_all(cls, session, db_schema: str, db_table: str):
        stmt = select(cls).where(cls.db_schema == db_schema, cls.db_table == db_table)
        return session.execute(stmt).scalars().all()
