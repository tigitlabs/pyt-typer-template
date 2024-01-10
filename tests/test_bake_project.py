# Using this plugin:
# https://github.com/hackebrot/pytest-cookies
# Example:
# https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/tests/test_bake_project.py

import os
from pathlib import Path
import shlex
import subprocess
from contextlib import contextmanager

EXPECTED_TOPLEVEL_FILES = ["tests", "README.md", ".gitignore", ".flake8", ".actrc"]


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
            return subprocess.check_call(shlex.split(command))
        except Exception:
            print(
                f"An error occurred when running the command {command} in directory: {dirpath}"
            )
            raise


def test_bake_project(cookies, request):
    keep_baked_projects = request.config.getoption("--keep-baked-projects")
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

    run_inside_dir("pip install -r requierments.txt", str(output_path)) == 0
    run_inside_dir("markdownlint .", str(output_path)) == 0
    run_inside_dir("yamllint .", str(output_path)) == 0
    run_inside_dir("black .", str(output_path)) == 0
    run_inside_dir("flake8", str(output_path)) == 0
    run_inside_dir("mypy --ignore-missing-imports .", str(output_path)) == 0
    run_inside_dir("pytest .", str(output_path)) == 0
    # This is redundant, just making sure it works
    run_inside_dir("./pre-commit.sh", str(output_path)) == 0
    print("test_bake_and_run_tests path", str(output_path))

    # Test Github Actions
    # git init is needed for act to work
    run_inside_dir("git init", str(output_path)) == 0
    run_inside_dir("act pull_request -l", str(output_path)) == 0
    run_inside_dir("act pull_request --dryrun", str(output_path)) == 0
    run_inside_dir("act pull_request -v", str(output_path)) == 0

    if keep_baked_projects:
        print("Keeping baked project at:\n {}".format(output_path))
        pass
