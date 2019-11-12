SHELL := /usr/bin/env bash

activate: venv
	@ [ -f activate ] || (ln -s venv/bin/activate . && $(MAKE) requirements)

requirements: activate venv
	. activate && venv/bin/pip install -r requirements.txt

venv:
	@ [ -d venv ] || python3 -m venv venv

freeze: activate
	. activate && venv/bin/pip freeze > requirements.txt

# possible to run only a given test file by overriding TEST
TEST_COMMAND = pytest -vv --capture=no $(TEST)

test: activate
	. activate && $(TEST_COMMAND)

pep8: activate
	. activate && pycodestyle *.py
