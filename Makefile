.PHONY: test

deps:
	pip install -r requirements.txt

lint:
	flake8 features

test:
	behave