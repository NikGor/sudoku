install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

lint:
	poetry run flake8

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall


