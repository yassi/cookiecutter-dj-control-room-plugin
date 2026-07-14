.PHONY: help install_test_requirements test test_fast

help:
	@echo "Makefile targets:"
	@echo "  make install_test_requirements   Install dependencies needed to test the template"
	@echo "  make test                        Bake the template and run the generated test suite"
	@echo "  make test_fast                   Same as 'test' but skips the slow bake+install+run checks"

install_test_requirements:
	python -m pip install -r requirements-test.txt

test: install_test_requirements
	python -m pytest tests/ -v

test_fast: install_test_requirements
	python -m pytest tests/ -v -m "not slow"
