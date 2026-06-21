PYTHON ?= python3

.PHONY: setup validate tables figures test package clean

setup:
	$(PYTHON) -m pip install -r requirements.txt

validate:
	$(PYTHON) scripts/validate_numbers.py
	$(PYTHON) scripts/validate_status_vocab.py
	$(PYTHON) scripts/validate_public_release.py
	$(PYTHON) -m pytest -q

tables:
	$(PYTHON) scripts/regenerate_tables.py

figures:
	$(PYTHON) scripts/regenerate_figures.py

test:
	$(PYTHON) -m pytest -q

package:
	$(PYTHON) scripts/package_release.py

clean:
	rm -rf .pytest_cache __pycache__ src/embedded_nn_contracts/__pycache__ tests/__pycache__
