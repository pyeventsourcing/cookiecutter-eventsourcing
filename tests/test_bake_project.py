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


def test_bake_then_make(cookies):
    with bake_in_temp_dir(cookies) as result:
        print("Baked project path:", result.project_path)

        check_call_inside_dir('make install-packages', str(result.project_path))
        check_call_inside_dir('make lint', str(result.project_path))
        check_call_inside_dir('make test', str(result.project_path))
        check_call_inside_dir('make build', str(result.project_path))
        check_call_inside_dir('make update-packages', str(result.project_path))
        check_call_inside_dir('make lock-packages', str(result.project_path))
        check_call_inside_dir('make fmt', str(result.project_path))
        check_call_inside_dir('make install', str(result.project_path))
        check_call_inside_dir('make lint', str(result.project_path))
        check_call_inside_dir('make test', str(result.project_path))
