[*please edit this file according to the needs of your project*]

# Welcome to {{cookiecutter.project_slug}}

[*please summarise what your project provides to users*]

## Installation

[*indicate how users can install your project*]

## Getting started

[*indicate how users can use your project*]

## Developers

After cloning the repository, you can set up a virtual environment and
install dependencies by running the following command in the root
folder.

    $ make install

The `make install` command uses `poetry` to create a dedicated Python
virtual environment, and installs into it the `eventsourcing`
library and popular development dependencies such as `black`, `isort`,
and `pytest`.

Add tests in `./tests`. Add code in `./{{cookiecutter.project_slug}}`.

Run tests.

    $ make test

Check the formatting of the code.

    $ make lint

Reformat the code.

    $ make fmt

Add dependencies in `pyproject.toml` and then update installed packages.

    $ make update-packages
