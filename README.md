[![CI](https://github.com/pyeventsourcing/cookiecutter-eventsourcing/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pyeventsourcing/cookiecutter-eventsourcing/actions/workflows/github-actions.yml)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Template for Python eventsourcing projects

Install cookiecutter into a dedicated virtual environment.

    $ python3 -mvenv ./cookiecutter-venv
    $ ./cookiecutter-venv/bin/pip install cookiecutter

Create a new project from the template.

    $ ./cookiecutter-venv/bin/cookiecutter gh:pyeventsourcing/cookiecutter-eventsourcing
    project_name [My New Project]: My Project 
    project_slug [my-project]: 
    pkg_name [my_project]: myproject 
    author_fullname [Author Name]: Your Name
    author_email [example@example.com]: your@email.address

Remove the cookiecutter virtual environment.

    $ rm -r cookiecutter-venv

You will now have the following files and folders.

    ./my-project
    ./my-project/.editorconfig
    ./my-project/.flake8
    ./my-project/.github
    ./my-project/.github/workflows
    ./my-project/.github/workflows/github-actions.yml
    ./my-project/.gitignore
    ./my-project/LICENSE
    ./my-project/Makefile
    ./my-project/README.md
    ./my-project/mypy.ini
    ./my-project/pyproject.toml
    ./my-project/pytest.ini
    ./my-project/tests
    ./my-project/tests/__init__.py
    ./my-project/tests/test_application.py
    ./my-project/myproject
    ./my-project/myproject/__init__.py
    ./my-project/myproject/application.py
    ./my-project/myproject/domainmodel.py
    ./my-project/myproject/py.typed

Start using your eventsourcing project.

    $ cd my-project
    $ make install

The ``make install`` command installs and uses the build tool Poetry to create a
dedicated  Python virtual environment for your project, and installs popular
development dependencies such as mypy, Black, isort, and pytest.

Add tests in `./tests`. Add code in `./myproject`. 

Run tests.

    $ make test

Check the formatting of your code.

    $ make lint

Reformat your code.

    $ make fmt

Add dependencies in `pyproject.toml` and then update installed packages.

    $ make update-packages

If you push your changes to a GitHub repo, your code will be automatically
tested in GitHub Actions. View your GitHub Actions config file(s), and
adjust according to your project's needs.

    $ less .github/workflows/github-actions.yml

See the [Python eventsourcing project](https://github.com/pyeventsourcing/eventsourcing)
for more information and guidance about developing event-sourced applications.

Please refer to the Poetry documentation for more information about building and distributing
Python packages with the Poetry build tool.
