# Using this plugin:
# https://github.com/hackebrot/pytest-cookies
# Example:
# https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/tests/test_bake_project.py

import os
import platform
import shlex
import subprocess
from contextlib import contextmanager
from enum import Enum
from pathlib import Path

import pytest

EXPECTED_TOPLEVEL_FILES = ["tests", "README.md", ".gitignore", ".flake8", ".actrc"]


class OS(str, Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "Darwin"


@pytest.fixture(scope="session", autouse=True)
def get_os() -> OS:
    """
    Get the current operating system
    :return: OS enum
    """
    os_name = platform.system()
    if os_name == OS.WINDOWS.value:
        return OS.WINDOWS
    elif os_name == OS.LINUX.value:
        return OS.LINUX
    elif os_name == OS.MACOS.value:
        return OS.MACOS
    else:
        raise ValueError(f"Unknown OS: {os_name}")


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


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        try:
            result = subprocess.run(shlex.split(command), check=True)
            return result.returncode
        except Exception:
            print(
                f"An error occurred when running the command {command} in directory: {dirpath}\n"
                "💡 Run the command pytest tests/ --keep-baked-projects and run the failed command in the directory.\n"
                f"Output dir: {dirpath}"
            )
            raise


def test_bake_project(cookies, get_os):
    result = cookies.bake(extra_context={"project_name": "helloworld"})
    assert result.exit_code == 0
    assert result.exception is None

    output_path: Path = result.project_path
    assert output_path.is_dir()

    assert output_path.name == "helloworld"
    assert output_path.is_dir()

    found_toplevel_files = [f.name for f in output_path.iterdir()]

    for expected_file in EXPECTED_TOPLEVEL_FILES:
        assert expected_file in found_toplevel_files

    run_inside_dir("pip install -r requirements.txt", str(output_path)) == 0
    # TODO: Add this back when we know how to run it on Windows
    if get_os == OS.WINDOWS:
        print("Skipping markdownlint tests on Windows")
    else:
        run_inside_dir("markdownlint .", str(output_path)) == 0
    run_inside_dir("black .", str(output_path)) == 0
    if get_os == OS.WINDOWS:
        # TODO: Add this back when we know how to run it on Windows, line endings are different
        print("Skipping yamllint tests on Windows")
    else:
        run_inside_dir("yamllint .", str(output_path)) == 0

    run_inside_dir("flake8", str(output_path)) == 0
    run_inside_dir("mypy --ignore-missing-imports .", str(output_path)) == 0
    run_inside_dir("pytest .", str(output_path)) == 0
    if get_os == OS.WINDOWS:
        # Setting the execution policy to unrestricted is needed for the pre-commit script to run
        print("Skipping pre-commit script tests on Windows")
    else:
        run_inside_dir("./scripts/pre_commit.sh", str(output_path)) == 0

    # Test the CLI
    run_inside_dir("python helloworld/main.py --help", str(output_path)) == 0


def test_bake_github_actions(cookies, request, get_os):
    if get_os == OS.WINDOWS:
        print("Skipping Github Actions tests on Windows")
        pass
    else:
        keep_baked_projects = request.config.getoption("--keep-baked-projects")
        result = cookies.bake(extra_context={"project_name": "gh-actions"})
        assert result.exit_code == 0
        assert result.exception is None

        output_path: Path = result.project_path
        assert output_path.is_dir()

        assert output_path.name == "gh-actions"
        assert output_path.is_dir()

        if keep_baked_projects:
            print("Keeping baked project at:\n {}".format(output_path))
            pass
            # Test Github Actions
        # git init is needed for act to work
        run_inside_dir("git init", str(output_path)) == 0
        run_inside_dir("act pull_request -l", str(output_path)) == 0
        run_inside_dir("act pull_request --dryrun", str(output_path)) == 0
        run_inside_dir("act pull_request -v", str(output_path)) == 0


def test_bake_devcontainer(cookies, request, get_os):
    if get_os == OS.WINDOWS:
        print("Skipping Github Actions tests on Windows")
        pass
    else:
        keep_baked_projects = request.config.getoption("--keep-baked-projects")

        result = cookies.bake(extra_context={"project_name": "dev-con"})
        assert result.exit_code == 0
        assert result.exception is None

        output_path: Path = result.project_path
        assert output_path.is_dir()

        assert output_path.name == "dev-con"
        assert output_path.is_dir()
        if keep_baked_projects:
            print("Keeping baked project at:\n {}".format(output_path))
        # Test the devcontainer build
        run_inside_dir("./scripts/devcontainer_test.sh", str(output_path)) == 0
