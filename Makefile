install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=calCLI --cov=mylib test_*.py

container-lint:
	docker run --rm -9 hadolint/hadolint < Dockerfile

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

format:
	black *.py mylib/*.py

refactor: format lint

#deploy: echno not being developed

all: install test lint format