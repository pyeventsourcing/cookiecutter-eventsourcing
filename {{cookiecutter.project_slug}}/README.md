[*please edit this file according to the needs of your project*]

# Welcome to {{cookiecutter.project_name}}

[*please summarise what your project provides to users*]

## Installation

[*indicate how users can install your project*]

## Getting started

[*indicate how users can use your project*]

## Developers

Clone the project repository, set up a virtual environment, and install
dependencies.

Use your IDE (e.g. PyCharm) to open the project repository. Create a
Poetry virtual environment, and then update packages.

    $ make update-packages

Alternatively, use the ``make install`` command to create a dedicated
Python virtual environment for this project.

    $ make install

The ``make install`` command uses the build tool Poetry to create a dedicated
Python virtual environment for this project, and installs popular development
dependencies such as Black, isort and pytest.

Add tests in `./tests`. Add code in `./{{cookiecutter.pkg_name}}`.

Run tests.

    $ make test

Check the formatting of the code.

    $ make lint

Reformat the code.

    $ make fmt

Add dependencies in `pyproject.toml` and then update installed packages.

    $ make update-packages
