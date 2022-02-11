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

Add tests in `./tests`. Add code in `./your_project`. Run tests.

    $ make test

See the [Python eventsourcing project](https://github.com/pyeventsourcing/eventsourcing)
for more information and guidance about developing event-sourced applications
and extensions for the Python eventsourcing library.

Add dependencies in `pyproject.toml`. Update installed packages.

    $ make update-packages

Check the code formatting.

    $ make lint

Reformat your code.

    $ make fmt

If your push your changes to a GitHub repo, your code will be tested in GitHub Actions.
