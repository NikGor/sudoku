install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=src --cov-report=term-missing

lint:
	poetry run flake8

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl --force-reinstall
