.PHONY: init format lint lint/flake8 lint/black test clean clean-temp clean-build clean-pyc clean-test

PROJECT_DIR=brain_kids
TESTS_DIR=brain_kids/tests

init: ## install dependencies
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

format: ## format code with black
	black ${PROJECT_DIR} ${TESTS_DIR}

lint: lint/flake8 lint/black ## check style

lint/flake8: ## check style with flake8
	flake8 ${PROJECT_DIR} ${TESTS_DIR}

lint/black: ## check style with black
	black --check ${PROJECT_DIR} ${TESTS_DIR}

test: ## run tests quickly with the default Python
	PYTHONPATH=brain_kids/src pytest

clean: clean-temp clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-temp: ## remove temporary files
	rm -fr temp/

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -path ./\.venv -prune -o -name '*.egg-info' -exec rm -fr {} +
	find . -path ./\.venv -prune -o -name '*.egg' -exec rm -rf {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.DS_Store' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .pytest_cache