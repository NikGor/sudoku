install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
