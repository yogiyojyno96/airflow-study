.PHONY: default run test

default:
	@echo "Local examples:"
	@echo "    make run        		# Starts a development server locally."
run:
	@poetry run uvicorn airflow_fastapi.main:app --reload

test:
	@echo [ === TEST === ]
	@poetry run pytest -n auto --dist loadscope

init_db:
	@echo [ === Init DB === ]
	@poetry run python3 airflow_fastapi/cli.py database init