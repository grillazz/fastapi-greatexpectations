from ruamel import yaml

import great_expectations as ge
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest


CONNECTION_STRING = "postgresql+psycopg2://user:secret@db/gxshakezz"

context = ge.get_context()

datasource_config = {
    "name": "my_postgres_datasource",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetSqlDataConnector",
            "include_schema_name": True,
        },
    },
}

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_config["execution_engine"]["connection_string"] = CONNECTION_STRING

context.add_datasource(**datasource_config)

# Here is a RuntimeBatchRequest using a query
batch_request = RuntimeBatchRequest(
    datasource_name="my_postgres_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="default_name",  # this can be anything that identifies this data
    runtime_parameters={"query": "SELECT * from public.taxi_data LIMIT 10"},
    batch_identifiers={"default_identifier_name": "default_identifier"},
)

context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)
print(validator.head())

# NOTE: The following code is only for testing and can be ignored by users.
assert isinstance(validator, ge.validator.validator.Validator)

# Here is a BatchRequest naming a table
batch_request = BatchRequest(
    datasource_name="my_postgres_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="public.taxi_data",  # this is the name of the table you want to retrieve
)
context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)
print(validator.head())

# NOTE: The following code is only for testing and can be ignored by users.
assert isinstance(validator, ge.validator.validator.Validator)
assert [ds["name"] for ds in context.list_datasources()] == ["my_postgres_datasource"]
assert "public.taxi_data" in set(
    context.get_available_data_asset_names()["my_postgres_datasource"][
        "default_inferred_data_connector_name"
    ]
)