[![CI](https://github.com/pyeventsourcing/cookiecutter-eventsourcing/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pyeventsourcing/cookiecutter-eventsourcing/actions/workflows/github-actions.yml)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Template for Python eventsourcing projects

Install cookiecutter into a dedicated virtual environment.

    $ python3 -mvenv ./cookiecutter-venv
    $ ./cookiecutter-venv/bin/pip install cookiecutter

Create a new project from the template.

    $ ./cookiecutter-venv/bin/cookiecutter gh:pyeventsourcing/cookiecutter-eventsourcing
    project_slug [my_project]: your_project 
    author_fullname [Author Name]: Your Name
    author_email [example@example.com]: your@email.address

Remove the cookiecutter virtual environment.

    $ rm -r cookiecutter-venv

You will now have the following files and folders.

    ./your_project
    ./your_project/.flake8
    ./your_project/your_project
    ./your_project/your_project/__init__.py
    ./your_project/your_project/domainmodel.py
    ./your_project/your_project/application.py
    ./your_project/your_project/py.typed
    ./your_project/pytest.ini
    ./your_project/LICENSE
    ./your_project/Makefile
    ./your_project/pyproject.toml
    ./your_project/tests
    ./your_project/tests/__init__.py
    ./your_project/tests/test_application.py
    ./your_project/.editorconfig
    ./your_project/README.md
    ./your_project/mypy.ini
    ./your_project/.gitignore
    ./your_project/.github
    ./your_project/.github/workflows
    ./your_project/.github/workflows/github-actions.yml

Start using your eventsourcing project.

    $ cd your_project
    $ make install

The ``make install`` command uses the build tool Poetry to create a dedicated
Python virtual environment for your project, and installs popular development
dependencies such as Black, isort and pytest.

Add tests in `./tests`. Add code in `./your_project`. 

Run tests.

    $ make test

Check the formatting of your code.

    $ make lint

Reformat your code.

    $ make fmt

Add dependencies in `pyproject.toml` and then update installed packages.

    $ make update-packages

If you push your changes to a GitHub repo, your code will be tested in GitHub Actions.
Edit your GitHub Actions config file(s) according to your project needs.

    $ less .github/workflows/github-actions.yml

See the [Python eventsourcing project](https://github.com/pyeventsourcing/eventsourcing)
for more information and guidance about developing event-sourced applications.

Please refer to the Poetry documentation for more information about building and distributing
Python packages with the Poetry build tool.
