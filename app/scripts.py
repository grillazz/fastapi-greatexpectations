import great_expectations as ge
from pydantic import BaseModel

class Chapter(BaseModel):
    id: int
    work_id: str
    section_number: int
    chapter_number: int
    description: str

# url: str = f"postgresql://user:secret@localhost:5432/gxshakezz?options=-csearch_path=shakespeare"
url: str = f"postgresql://user:secret@localhost:5432/gxshakezz"

_context: ge.DataContext = ge.get_context()

# _context.sources.add_postgres(name='gxshakezz', connection_string=str(url))

_datasource = _context.sources.add_sql(name="my_gx", connection_string=url)
# _datasource = _context.get_datasource("my_gx")
_table_asset = _datasource.add_table_asset(name="my_gx_asset", table_name="chapter")
#
_br = _table_asset.build_batch_request()
#
_batches = _datasource.get_batch_list_from_batch_request(_br)
#

_b = _batches[0]
#
_b.head()

# play with expectations
_validator = _context.get_validator(datasource_name="my_gx", data_asset_name="my_gx_asset")
_validator.expect_column_values_to_not_be_null("work_id")

_validator.list_available_expectation_types()