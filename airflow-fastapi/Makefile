.PHONY: default run test

default:
	@echo "Local examples:"
	@echo "    make run        		# Starts a development server locally."
run:
	@poetry run uvicorn config.asgi:application --host 0.0.0.0 --port 9000 --reload

test:
	@echo [ === TEST === ]
	@poetry run pytest -n auto --dist loadscope
