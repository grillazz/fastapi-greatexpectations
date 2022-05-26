#
# class GXValidation(Base):
#     __tablename__ = "ge_validations_store"
#     modified_by = Column(String)
#     id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
#
#     run_name = Column(String, nullable=False)
#     run_time = Column(String, nullable=True)
#     batch_identifier = Column(String, nullable=True, index=True)
#     task_id = Column(String, nullable=True)
#     value = Column(mutable_json_type(dbtype=JSONB, nested=True))
#
#     # foreign keys part
#     expectation_suite_id = Column(
#         UUID(as_uuid=True),
#         ForeignKey("ge_expectations_store.id", ondelete="CASCADE"),
#         nullable=False,
#     )
#     cid = Column(Integer, ForeignKey("clients.cid"))
#     exec_id = Column(Integer, ForeignKey("exec.id"))
#     # relationship part
#     exec = relationship("Exec")
#     client = relationship("Client")
#
#     def __init__(
#             self,
#             modified_by,
#             expectation_suite_id,
#             run_name,
#             run_time,
#             batch_identifier,
#             task_id,
#             value,
#     ):
#         self.modified_by = modified_by
#         self.expectation_suite_id = expectation_suite_id
#         self.run_name = run_name
#         self.run_time = run_time
#         self.batch_identifier = batch_identifier
#         self.task_id = task_id
#         self.value = value
