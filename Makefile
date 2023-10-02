install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_app.py

container-lint:
	docker run --rm -9 hadolint/hadolint < Dockerfile

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py mylib/*.py

format:
	black *.py

refactor: format lint

#deploy: echno not being developed

all: install test lint format