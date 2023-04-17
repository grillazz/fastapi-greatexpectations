# fastapi-greatexpectations

[![developer](https://img.shields.io/badge/Dev-grillazz-green?style)](https://github.com/grillazz)
![language](https://img.shields.io/badge/language-python-blue?style)
[![license](https://img.shields.io/github/license/grillazz/fastapi-greatexpectations)](https://github.com/grillazz/fastapi-greatexpectations/blob/main/LICENSE)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=grillazz.fastapi-greatexpectations")
[![CI](https://img.shields.io/github/workflow/status/grillazz/fastapi-greatexpectations/Unit%20Tests/main)](https://github.com/grillazz/fastapi-greatexpectations/actions/workflows/build-and-test.yml)

![fastapi-greatexpectations](/static/wunsz.jpg)

In this place two personas William Shakespeare as [Data Feed](https://github.com/catherinedevlin/opensourceshakespeare)
and Charles Dickens as [Data Validation](https://greatexpectations.io/expectations/)
will be hosted by Almighty Monty Python as Service :)

Can we be better prepared for expected unexpected philosophy ?
The `expect the unexpected` philosophy leads to the freedom of
choice and the freedom of others people judgment,
creating a future full of possibilities, accepting that whatever will be,
will be; the future's not ours to see, que será, será.

### :cook: How to Set up project locally

To build , run and more... use magic of make help to play with this project.

```shell
make help
```

and you receive below list:

```text
black                apply black in project code.
build                Build project with compose
clean                Clean Reset project containers with compose
down                 Reset project containers with compose
feed_db              create database objects and insert data
flake8               apply black in project code.
help                 Show this help
isort                sort imports in project code.
mypy                 apply black in project code.
requirements         Refresh requirements.txt from pipfile.lock
up                   Run project with compose
```

### How to Play

1. Build project with docker compose: `make build`
2. Run project with docker compose: `make up`
3. Create database objects and insert data: `make feed_db`

4. Get list of available database schemas `/v1/database/schemas` endpoint
    ```shell
    curl -X 'GET' 'http://0.0.0.0:8585/v1/database/schemas' -H 'accept: application/json'
    ```
   and get response like below with `200 OK`
    ```json
   [
     "information_schema",
     "public",
     "shakespeare"
   ]
    ```
5. Get list of tables for requested schema `/v1/database/tables` endpoint
    ```shell
    curl -X 'GET' 'http://0.0.0.0:8585/v1/database/tables?sql_db_schema=shakespeare' -H 'accept: application/json'
    ```
   and get response like below with `200 OK`
    ```json
   [
     "paragraph",
     "wordform",
     "character",
     "character_work",
     "work",
     "chapter"
   ]
    ```
6. Get columns for requested table `/v1/database/columns` endpoint
    ```shell
    curl -X 'GET' 'http://0.0.0.0:8585/v1/database/columns?database_schema=shakespeare&schema_table=chapter' -H 'accept: application/json'
    ```
   and get response like below with `200 OK`
    ```json
        [
           {
             "name": "id",
             "type": {},
             "nullable": false,
             "default": null,
             "autoincrement": false,
             "comment": null
           },
           {
             "name": "work_id",
             "type": {
               "length": 32,
               "collation": null,
               "_expect_unicode": false,
               "_expect_unicode_error": null,
               "_warn_on_bytestring": false
             },
             "nullable": false,
             "default": null,
             "autoincrement": false,
             "comment": null
           },
           {
             "name": "section_number",
             "type": {},
             "nullable": false,
             "default": null,
             "autoincrement": false,
             "comment": null
           },
           {
             "name": "chapter_number",
             "type": {},
             "nullable": false,
             "default": null,
             "autoincrement": false,
             "comment": null
           },
           {
             "name": "description",
             "type": {
               "length": 256,
               "collation": null,
               "_expect_unicode": false,
               "_expect_unicode_error": null,
               "_warn_on_bytestring": false
             },
             "nullable": false,
             "default": null,
             "autoincrement": false,
             "comment": null
           }
         ]
   ```

7. Try simple expectation `/v1/expectation/try/{gx_func}` endpoint
   ```shell
   curl -X 'POST' \
   'http://0.0.0.0:8585/v1/expectation/try/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{}' 
    ```

   and get response error like below

   ```json
   "TypeError(\"Dataset.expect_table_row_count_to_equal() missing 1 required positional argument: 'value'\")"
   ```

   so try again with expected value equal to 100

   ```shell
   curl -X 'POST' \
   'http://0.0.0.0:8585/v1/expectation/try/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{"value":100}'
    ```
   and get response like below with `200 OK`
   with information that expectation run with no success as observed value in table is equal to 945
   ```json
   {
     "success": false,
     "expectation_config": {
       "_expectation_type": "expect_table_row_count_to_equal",
       "_kwargs": {
         "value": 100,
         "result_format": "BASIC"
       },
       "_raw_kwargs": null,
       "meta": {},
       "success_on_last_run": null,
       "_ge_cloud_id": null,
       "_expectation_context": null
     },
     "result": {
       "observed_value": 945
     },
     "meta": {},
     "exception_info": {
       "raised_exception": false,
       "exception_traceback": null,
       "exception_message": null
     }
   }
   ```
   one more try with expected value equal to 945
     ```shell
     curl -X 'POST' \
     'http://0.0.0.0:8585/v1/expectation/try/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{"value":945}'
      ```
   and get response like below with `200 OK` with information that expectation run with success as expected value meet
   observed value
   ```json
   {
     "include_rendered_content": false,
     "success": true,
     "expectation_config": {
       "_expectation_type": "expect_table_row_count_to_equal",
       "_kwargs": {
         "value": 945,
         "result_format": "BASIC"
       },
       "_raw_kwargs": null,
       "meta": {},
       "success_on_last_run": null,
       "_ge_cloud_id": null,
       "_expectation_context": null,
       "_include_rendered_content": false
     },
     "result": {
       "observed_value": 945
     },
     "meta": {},
     "exception_info": {
       "raised_exception": false,
       "exception_traceback": null,
       "exception_message": null
     }
   }
   ```


8. Save expectation `/v1/expectation/add/{gx_func}` endpoint
   ```shell
   curl -X 'POST' \
   'http://0.0.0.0:8585/v1/expectation/add/expect_table_row_count_to_equal?database_schema=shakespeare&schema_table=chapter&suite_name=chapter_suite' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{"value":945}'
   ```
   and get response like below with `201`
   ```json
   {
     "id": "40ef18ac-14e0-477e-9c7f-4b4830d29980",
     "suite_name": "chapter_suite_1",
     "suite_desc": "",
     "value": {
       "meta": {
         "great_expectations_version": "0.15.19"
       },
       "ge_cloud_id": null,
       "expectations": [
         {
           "meta": {},
           "kwargs": {
             "value": 945
           },
           "expectation_type": "expect_table_row_count_to_equal"
         }
       ],
       "data_asset_type": "Dataset",
       "expectation_suite_name": "chapter_suite_1"
     }
   }
   ```


9. Run validation `/v1/validation/run/{database_schema}/{table_name}/{suite_name}` endpoint
   ```shell
   curl -X 'POST' \
     'http://0.0.0.0:8585/v1/validation/run/shakespeare/chapter/chapter_suite' \
     -H 'accept: application/json'
   ```
   and get response like below with `201`


10. Get validation results `/v1/validation` endpoint
      ```shell
      curl -X 'GET' \
        'http://0.0.0.0:8585/v1/validation?database_schema=shakespeare&table_name=chapter' \
        -H 'accept: application/json'
      ```
    and get response like below with `200` with list of validation results in response
    ```json
     [
      {
       "value": {
         "meta": {
           "run_id": {
             "run_name": null,
             "run_time": "2022-08-21T15:52:46.263216+00:00"
           },
           "batch_kwargs": {
             "ge_batch_id": "4cd3db9e-2169-11ed-bcba-0242ac180003"
           },
           "batch_markers": {},
           "validation_time": "20220821T155246.263096Z",
           "batch_parameters": {},
           "expectation_suite_meta": {
             "great_expectations_version": "0.15.19"
           },
           "expectation_suite_name": "chapter_suite",
           "great_expectations_version": "0.15.19"
         },
         "results": [
           {
             "meta": {},
             "result": {
               "observed_value": 945
             },
             "success": true,
             "exception_info": {
               "raised_exception": false,
               "exception_message": null,
               "exception_traceback": null
             },
             "expectation_config": {
               "meta": {},
               "kwargs": {
                 "value": 945
               },
               "expectation_type": "expect_table_row_count_to_equal"
             }
           }
         ],
         "success": true,
         "statistics": {
           "success_percent": 100,
           "evaluated_expectations": 1,
           "successful_expectations": 1,
           "unsuccessful_expectations": 0
         },
         "evaluation_parameters": {}
       },
       "db_schema": "shakespeare",
       "id": "8e1f6b6a-14a6-48ba-b724-2363f8949dbe",
       "db_table": "chapter",
       "expectation_suite_id": "5e4d8e0e-8bb3-4c84-9f2d-86abb981872a"
     },
     ...
    ] 
    ```


11. list of available expectations https://greatexpectations.io/expectations/

### Backbone

...
Hope you enjoy it.

