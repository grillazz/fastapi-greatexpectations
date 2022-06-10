from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ExpectationSuiteSchema(BaseModel):
    id: UUID = Field(
        title="",
        description="",
    )
    suite_name: str = Field(
        title="",
        description="",
    )

    suite_desc: str = Field(
        title="",
        description="",
    )

    value: dict = Field(
        title="",
        description="",
    )

    class Config:
        orm_mode = True
