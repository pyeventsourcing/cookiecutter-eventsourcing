.EXPORT_ALL_VARIABLES:

POETRY ?= poetry
POETRY_INSTALLER_URL ?= https://install.python-poetry.org


.PHONY: install-poetry
install-poetry:
	curl -sSL $(POETRY_INSTALLER_URL) | python3
	$(POETRY) --version


.PHONY: install
install:
	$(POETRY) --version
	$(POETRY) install -vv $(opts)

.PHONY: update-lock-file
update-lock-file:
	$(POETRY) lock -vv

.PHONY: update-packages
update-packages:
	$(POETRY) update -vv

.PHONY: test
test:
	$(POETRY) run pytest -s tests
