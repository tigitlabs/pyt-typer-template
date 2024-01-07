#! /bin/bash

# This script is used to run pre-commit checks on the repository.
set -e

echo "🏃‍♂️ Running black"
black .

echo "🏃‍♂️ Running flake8"
flake8

echo "🏃‍♂️ Running mypy"
# Static type checking with mypy
mypy --ignore-missing-imports .
echo "🏃‍♂️ Running pytest"
pytest --durations=0 --cov