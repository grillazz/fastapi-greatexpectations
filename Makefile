.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:	## Build project with compose
	docker-compose build

.PHONY: up_code
up_code:	## Run project with compose
	docker-compose up --build --remove-orphans

up: black isort up_code

.PHONY: down
down: ## Reset project containers with compose
	docker-compose down

.PHONY: clean
clean: ## Clean Reset project containers with compose
	docker-compose down -v --remove-orphans

.PHONY: isort
isort:  ## sort imports in project code.
	docker-compose run --rm app isort  -m 3 -tc .

.PHONY: black
black:  ## apply black in project code.
	docker-compose run --rm app black .

.PHONY: mypy
mypy:  ## apply black in project code.
	docker-compose run --rm app mypy --ignore-missing-imports .

.PHONY: flake8
flake8:  ## apply black in project code.
	docker-compose run --rm app flake8 .

.PHONY: feed_db
feed_db: ## create database objects and insert data
	docker-compose exec db psql gxshakezz user -f /home/gx/code/shakespeare.sql

.PHONY: requirements
requirements:	## Refresh requirements.txt from pipfile.lock
	pipenv lock --requirements --dev >| requirements.txt

.PHONY: test
test:	## Run project tests
	docker-compose run --rm app pytest -vv

.PHONY: coverage
coverage:	## Run project tests with coverage
	docker-compose run --rm app bash -c "cd tests && pytest --cov=app --cov-report=xml --cov-report=html"

.PHONY: verify_db_backup
verify_db_backup:	## Verify database backup file names before restore on running sqlserver container
	docker-compose exec sqlserver bash -c "cd /opt/mssql-tools18/bin && ./sqlcmd -S localhost -U sa -P 'yourStrong(!)Password' -d master -i /home/setup/verify.sql"

.PHONY: restore_db_backup
restore_db_backup:	## Restore database backup on running sqlserver container
	docker-compose exec sqlserver bash -c "cd /opt/mssql-tools/bin && ./sqlcmd -S localhost -U sa -P 'yourStrong(!)Password' -d master -i /home/setup/restore.sql"

.PHONY: build_database
build_database:	## Build database on running sqlserver container
	docker-compose exec app bash -c "/opt/mssql-tools18/bin/sqlcmd -S sqlserver -U SA -P 'Alaska2023' -C -i /home/code/setup/instawdb.sql"