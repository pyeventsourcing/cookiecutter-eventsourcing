from contextlib import contextmanager
import shlex
import os
import subprocess
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests

    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    if result.exception:
        raise result.exception
    assert result.project_path.is_dir(), result
    assert result.exit_code == 0, result

    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def check_call_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command), env=adjust_env_vars(dirpath))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command), env=adjust_env_vars(dirpath))


def adjust_env_vars(dirpath):
    env = os.environ.copy()
    if "VIRTUAL_ENV" in env:
        virtual_env_path = env.pop("VIRTUAL_ENV")
        print("Removed 'VIRTUAL_ENV' from env:", virtual_env_path)
    poetry_virtualenvs_path = os.path.abspath(os.path.join(dirpath, "..", ".venvs"))
    env["POETRY_VIRTUALENVS_PATH"] = poetry_virtualenvs_path
    print("Set 'POETRY_VIRTUALENVS_PATH' in env:", poetry_virtualenvs_path)
    return env


def project_info(result):
    """Get toplevel dir, project_name, project_slug, pkg_name and project dir from baked cookies"""
    project_path = str(result.project_path)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:

        print("Baked project path:", result.project_path)

        assert os.path.exists(result.project_path / result.context['pkg_name'])
        assert os.path.exists(result.project_path / result.context['pkg_name'] / '__init__.py')
        assert os.path.exists(result.project_path / result.context['pkg_name'] / 'application.py')
        assert os.path.exists(result.project_path / result.context['pkg_name'] / 'domainmodel.py')
        assert os.path.exists(result.project_path / 'tests')
        assert os.path.exists(result.project_path / 'tests' / '__init__.py')
        assert os.path.exists(result.project_path / 'tests' / 'test_application.py')
        assert os.path.exists(result.project_path / 'pyproject.toml')
        assert os.path.exists(result.project_path / 'pytest.ini')
        assert os.path.exists(result.project_path / 'mypy.ini')
        assert os.path.exists(result.project_path / '.flake8')
        assert os.path.exists(result.project_path / '.editorconfig')
        assert os.path.exists(result.project_path / 'Makefile')

        check_call_inside_dir('make install-packages', str(result.project_path))
        check_call_inside_dir('make lint', str(result.project_path))
        check_call_inside_dir('make test', str(result.project_path))

        check_call_inside_dir('make install', str(result.project_path))
        check_call_inside_dir('make lint', str(result.project_path))
        check_call_inside_dir('make test', str(result.project_path))
