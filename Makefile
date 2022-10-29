.EXPORT_ALL_VARIABLES:

POETRY ?= poetry
POETRY_INSTALLER_URL ?= https://install.python-poetry.org


.PHONY: install-poetry
install-poetry:
	curl -sSL $(POETRY_INSTALLER_URL) | python3
	$(POETRY) --version

.PHONY: install
install:
	pip install -U pip
	pip install -Ur requirements_dev.txt

.PHONY: test
test:
	pytest -s tests
