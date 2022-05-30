[![CI](https://github.com/pyeventsourcing/cookiecutter-eventsourcing/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pyeventsourcing/cookiecutter-eventsourcing/actions/workflows/github-actions.yml)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Template for Python eventsourcing projects

## Install Cookiecutter

Create a Python virtual environment for Cookiecutter.

    $ python3 -m venv ~/.cookiecutter-venv

Install Cookiecutter into the Python virtual environment.

    $ ~/.cookiecutter-venv/bin/pip install cookiecutter

## Create new project from template

Use Cookiecutter to create a new Python eventsourcing project. You will be prompted for template values.

    $ ./cookiecutter-venv/bin/cookiecutter gh:pyeventsourcing/cookiecutter-eventsourcing

Choose a name for your new project. By default, the given project name will be lower-cased and hyphenated
to create a default project slug. Hyphens in the project slug will be replaced by underscores to create a
default package name. Adjust the project slug and the package name according to your preferences. 

    $ ./cookiecutter-venv/bin/cookiecutter gh:pyeventsourcing/cookiecutter-eventsourcing
    project_name [My New Project]:
    project_slug [my-project]:
    pkg_name [my_project]:
    author_fullname [Author Name]:
    author_email [example@example.com]:

Change directory to the root folder of the new project files.

    $ cd my-new-project

You will now have the following files and folders.

    my-new-project/.editorconfig
    my-new-project/.flake8
    my-new-project/.github/workflows/github-actions.yml
    my-new-project/.gitignore
    my-new-project/LICENSE
    my-new-project/Makefile
    my-new-project/README.md
    my-new-project/my_new_project/__init__.py
    my-new-project/my_new_project/application.py
    my-new-project/my_new_project/domainmodel.py
    my-new-project/my_new_project/py.typed
    my-new-project/mypy.ini
    my-new-project/pyproject.toml
    my-new-project/pytest.ini
    my-new-project/tests/__init__.py
    my-new-project/tests/test_application.py

Optionally remove the Cookiecutter virtual environment.

    $ rm -r ~/.cookiecutter-venv

## Install Poetry

Check if you have [Poetry](https://python-poetry.org) installed.

    $ poetry --version

If you don't have Poetry installed, then [install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

It will help to make sure Poetry's bin directory is in your `PATH` environment variable.

But in any case, make sure you know the path to the `poetry` executable. The Poetry
installer tells you where it has been installed, and how to configure your shell.

Please refer to the [Poetry docs](https://python-poetry.org/docs/) for guidance on
using Poetry.


## Create project virtual environment

Create a Python virtual environment for your project, either using PyCharm
or from the command line.

### Create project virtual environment using PyCharm

Use the "File > Open..." menu option in PyCharm and open the project folder in a new
window.

Create a new Poetry virtual environment for the project. If PyCharm doesn't already
know where your `poetry` executable is, then set the path to your `poetry` executable
in the "New Poetry Environment" form input field labelled "Poetry executable". In the
"New Poetry Environment" form, you will also have the opportunity to select which
Python executable will be used by the virtual environment.

PyCharm will then create a new Poetry virtual environment for your project, using
a particular version of Python, and also install into this virtual environment the
project's package dependencies according to the `pyproject.toml` file, or the
`poetry.lock` file if that exists in the project files.

You can add different Poetry environments for different Python versions, and switch
between them using the "Python Interpreter" settings of PyCharm. If you want to use
a version of Python that isn't installed, either use your favourite package manager,
or install Python by downloading an installer for recent versions of Python directly
from the [Python website](https://www.python.org/downloads/).

Once project dependencies have been installed, you should be able to run tests
from within PyCharm (right-click on the `tests` folder and select the 'Run' option).

Because of a conflict between pytest and PyCharm's debugger and the coverage tool,
you may need to add ``--no-cov`` as an option to the test runner template. Alternatively,
just use the Python Standard Library's ``unittest`` module.

You should also be able to open a terminal window in PyCharm, and run the project's
Makefile commands from the command line (see below).

### Create project virtual environment from command line

Use the Makefile to create a new Poetry virtual environment for the
project and install the project's package dependencies into it,
using the following command.

    $ make install

If you want to skip the installation of your project's package, use the
`--no-root` option.

    $ make install --no-root

Please note, if you create the virtual environment in this way, and then try to
open the project in PyCharm and configure the project to use this virtual
environment as an "Existing Poetry Environment", PyCharm sometimes has some
issues (don't know why) which might be problematic. If you encounter such
issues, you can resolve these issues by deleting the virtual environment
and creating the Poetry virtual environment using PyCharm (see above).

## Getting started

The template for Python eventsourcing projects includes a small example
of an event-sourced application. It has an event-sourced aggregate and a
test that you can run. You can use this example to check your project is
working, and as a starting point for your own project. You can edit or
remove it and start again.

You can run tests using the following command.

    $ make test

You can check the formatting of the code using the following command.

    $ make lint

You can reformat the code using the following command.

    $ make fmt

Tests belong in `./tests`. Code-under-test belongs in `./{{cookiecutter.pkg_name}}`.

See the [Python eventsourcing project](https://github.com/pyeventsourcing/eventsourcing)
for more information and guidance about developing event-sourced applications.

If you push your changes to a GitHub repo, your code will be automatically
tested in GitHub Actions. View your GitHub Actions config file(s), and
adjust according to your project's needs.

    $ less .github/workflows/github-actions.yml


Edit package dependencies in `pyproject.toml`. Update installed packages (and the
`poetry.lock` file) using the following command.

    $ make update-packages

Please refer to the [Poetry docs](https://python-poetry.org/docs/) for guidance on
using Poetry.
