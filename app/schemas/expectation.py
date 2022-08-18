from __future__ import annotations

from typing import Any, Dict, List
from uuid import UUID

from pydantic import BaseModel, Field


class Meta(BaseModel):
    great_expectations_version: str


class Kwargs(BaseModel):
    value: int


class Expectation(BaseModel):
    meta: Dict[str, Any]
    kwargs: Kwargs
    expectation_type: str


class Value(BaseModel):
    meta: Meta
    ge_cloud_id: Any
    expectations: List[Expectation]
    data_asset_type: str
    expectation_suite_name: str


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

    value: Value = Field(
        title="",
        description="",
    )

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": "40ef18ac-14e0-477e-9c7f-4b4830d29980",
                "suite_name": "chapter_suite_1",
                "suite_desc": "",
                "value": {
                    "meta": {"great_expectations_version": "0.15.15"},
                    "ge_cloud_id": None,
                    "expectations": [
                        {
                            "meta": {},
                            "kwargs": {"value": 945},
                            "expectation_type": "expect_table_row_count_to_equal",
                        }
                    ],
                    "data_asset_type": "Dataset",
                    "expectation_suite_name": "chapter_suite_1",
                },
            }
        }
