# This script is used to run pre-commit checks on the repository.

# TODO - Add markdownlint for PowerShell
# Write-Host "🏃‍♂️ Running markdownlint"
# #markdownlint *.md

Write-Host "🏃‍♂️ Running yamllint"
yamllint .

Write-Host "🏃‍♂️ Running pyinilint"
pyinilint *.ini

Write-Host "🏃‍♂️ Running isort"
isort .

Write-Host "🏃‍♂️ Running black"
black ./tests/

Write-Host "🏃‍♂️ Running flake8"
flake8

Write-Host "🏃‍♂️ Running mypy"
# Static type checking with mypy
mypy --ignore-missing-imports .

Write-Host "🏃‍♂️ Running pytest"
pytest .
