prepare:
	pip install poetry poetry-setup pre-commit
	poetry install -v
	poetry develop
	pre-commit install

test:
	tox .

serve:
	waitress-serve --port=5000  --call 'fluid_contacts:create_app'
	#waitress-serve --call 'fluid_contacts:create_app' --port '5000'

