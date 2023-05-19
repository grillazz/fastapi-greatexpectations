# fastapi-greatexpectations :shield: :eyes:

[![developer](https://img.shields.io/badge/Dev-grillazz-green?style)](https://github.com/grillazz)
![language](https://img.shields.io/badge/language-python-blue?style)
[![license](https://img.shields.io/github/license/grillazz/fastapi-greatexpectations)](https://github.com/grillazz/fastapi-greatexpectations/blob/main/LICENSE)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=grillazz.fastapi-greatexpectations")
[![CI](https://img.shields.io/github/workflow/status/grillazz/fastapi-greatexpectations/Unit%20Tests/main)](https://github.com/grillazz/fastapi-greatexpectations/actions/workflows/build-and-test.yml)

![fastapi-greatexpectations](/static/wunsz.jpg)

In this place two personas William Shakespeare as [Data Feed](https://github.com/catherinedevlin/opensourceshakespeare)
and Charles Dickens as [Data Validation](https://greatexpectations.io/expectations/)
will be hosted by Almighty Monty Python as Watchman Service :)

[greatexpectations.io](https://greatexpectations.io/expectations/) is a tool for data quality validation, documentation, and profiling.
Here we will use latest version of [great-expectations = "0.16.12"](https://pypi.org/project/great-expectations/) 
and [fastapi = "0.95.0"](https://pypi.org/project/fastapi/).

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

### Backbone

...
Hope you enjoy it.

