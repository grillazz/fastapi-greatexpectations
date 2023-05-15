import great_expectations as ge
from great_expectations.datasource.fluent.sql_datasource import SQLDatasource, TableAsset
from great_expectations.data_context.data_context.abstract_data_context import AbstractDataContext
# url: str = f"postgresql://user:secret@localhost:5432/gxshakezz"
# url: str = f"postgresql://user:secret@localhost:5432/gxshakezz?options=-csearch_path=shakespeare"

class GxSession:
    # keep state of the great_expectations session
    # TODO: make this a singleton or borg ?

    context: AbstractDataContext
    sql_datasource: SQLDatasource
    sql_table_asset: TableAsset

    def __init__(self, url: str, datasource_name: str, table_name: str):
        self.context = ge.get_context()
        self.sql_datasource = self.context.sources.add_sql(name=datasource_name, connection_string=url)
        self.sql_table_asset = self.sql_datasource.add_table_asset(name=f"{table_name}_asset", table_name=table_name)
