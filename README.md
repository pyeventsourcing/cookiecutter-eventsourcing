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

Start using your eventsourcing project.

    $ cd your_project
    $ make install

The `make install` command uses `poetry` to create a dedicated Python
virtual environment for your project, and installs into it the `eventsourcing`
library and popular development dependencies such as `black`, `isort`, and `pytest`.

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
