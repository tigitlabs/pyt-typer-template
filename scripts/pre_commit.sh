#! /bin/bash

# This script is used to run pre-commit checks on the repository.
set -e

echo "🏃‍♂️ Running markdownlint"
markdownlint *.md

echo "🏃‍♂️ Running yamllint"
yamllint .

echo "🏃‍♂️ Running pyinilint"
pyinilint mypy.ini

echo "🏃‍♂️ Running isort"
isort .

echo "🏃‍♂️ Running black"
black ./tests/

echo "🏃‍♂️ Running flake8"
flake8

echo "🏃‍♂️ Running mypy"
# Static type checking with mypy
mypy --ignore-missing-imports .

echo "🏃‍♂️ Running pytest"
pytest  tests/test_bake_project.py::test_bake_project
