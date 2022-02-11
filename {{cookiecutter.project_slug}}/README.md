[*please edit this file according to the needs of your project*]

# Welcome to the {{cookiecutter.project_slug}} project

[*please summarise what your project provides to users*]

## Installation

[*indicate how users can install your project*]

Use pip to install the [stable distribution](https://pypi.org/project/{{cookiecutter.project_slug}}/)
from the Python Package Index.

    $ pip install {{cookiecutter.project_slug}}

It is recommended to
install Python packages into a Python virtual environment.

## Getting started

[*indicate how users can use your project*]

## Developers

[*indicate how developers can make contributions*]

After cloning the repository, you can set up a virtual environment and
install dependencies by running the following command in the root
folder.

    $ make install

After making changes, run the tests.

    $ make test

Check the formatting of the code.

    $ make lint

You can automatically reformat the code by running the following command.

    $ make fmt

Add dependencies in `pyproject.toml`. Update installed packages by running
the following command.

    $ make update-packages
