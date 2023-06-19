# from __future__ import annotations
#
# from typing import Any, Dict, List, Optional
# from uuid import UUID
#
# from pydantic import BaseModel
#
#
# class RunId(BaseModel):
#     run_name: Any
#     run_time: str
#
#
# class BatchKwargs(BaseModel):
#     ge_batch_id: str
#
#
# class ExpectationSuiteMeta(BaseModel):
#     great_expectations_version: str
#
#
# class Meta(BaseModel):
#     run_id: RunId
#     batch_kwargs: BatchKwargs
#     batch_markers: Dict[str, Any]
#     validation_time: str
#     batch_parameters: Dict[str, Any]
#     expectation_suite_meta: ExpectationSuiteMeta
#     expectation_suite_name: str
#     great_expectations_version: str
#
#
# class Result1(BaseModel):
#     observed_value: int
#
#
# class ExceptionInfo(BaseModel):
#     raised_exception: bool
#     exception_message: Any
#     exception_traceback: Any
#
#
# class Kwargs(BaseModel):
#     value: int
#
#
# class ExpectationConfig(BaseModel):
#     meta: Dict[str, Any]
#     kwargs: Kwargs
#     expectation_type: str
#
#
# class Result(BaseModel):
#     meta: Dict[str, Any]
#     result: Result1
#     success: bool
#     exception_info: ExceptionInfo
#     expectation_config: ExpectationConfig
#
#
# class Statistics(BaseModel):
#     success_percent: int
#     evaluated_expectations: int
#     successful_expectations: int
#     unsuccessful_expectations: int
#
#
# class Value(BaseModel):
#     meta: Meta
#     results: List[Result]
#     success: bool
#     statistics: Statistics
#     evaluation_parameters: Dict[str, Any]
#
#
# class ValidationResponse(BaseModel):
#     value: Value
#     db_schema: str
#     id: UUID
#     db_table: str
#     expectation_suite_id: UUID
#
#     class Config:
#         orm_mode = True
