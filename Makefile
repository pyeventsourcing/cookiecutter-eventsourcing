.PHONY: install
install:
	pip install -U pip
	pip install -Ur requirements_dev.txt

.PHONY: test
test:
	pytest tests
