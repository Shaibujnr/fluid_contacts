prepare-devenv:
	pip install poetry poetry-setup pre-commit
	poetry install -v
	poetry develop
	pre-commit install

test:
	pytest

serve:
	echo "start server"