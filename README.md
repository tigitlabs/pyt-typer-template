# pyt-typer-template

Template for a Python CLI application using [Typer](https://typer.tiangolo.com/)  
[Typer GitHub repository](https://github.com/tiangolo/typer)

## Usage

To use this template by running:

```bash
cookiecutter https://github.com/tigitlabs/pyt-typer-template.git
```

Then run cookiecutter:

```bash

## CI/CD

- Run test on Ubuntu and Windows
- pre-commit hooks
  - black
  - flake8
  - mypy
  - pytest
  - coverage

### Python

- Logging with [loguru](https://loguru.readthedocs.io/en/stable/)
- linting with [flake8](https://flake8.pycqa.org/en/latest/)
- testing with [pytest](https://docs.pytest.org/en/stable/)
- code coverage with [coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
- code formatting with [black](https://black.readthedocs.io/en/stable/)
- type checking with [mypy](https://mypy.readthedocs.io/en/stable/)

### CLI

- [Typer](https://typer.tiangolo.com/)

- Printing with [rich](https://rich.readthedocs.io/en/latest/)
- CLI template functions
  - init
    - load config
    - create logger
  - run
    - create list of files to process
    - process files
    - print results with progress bar
  - clean
    - remove files

## Development

### Environment

Designed to work with Github Codespaces

### Tools

#### pytest

The tests are using the plugin pytest-cookies.
To run the tests and keep the output folder for debugging, run:

```bash
pytest tests/ --keep-baked-projects
```

### Working in a Codespace

You can create a Codespace by clicking the green button at the top of the repository.  
Or use the Github CLI

```bash
gh cs create --repo tigitlabs/pyt-typer-template --branch dev --display-name pyt-typer-template --machine premiumLinux
```

Machine options:

- basicLinux32gb
  - RAM: 8 GB
  - Cores: 2
  - Disk Space: 32 GB
- standardLinux32gb
  - RAM: 16 GB
  - Cores: 4
  - Disk Space: 32 GB
- premiumLinux
  - RAM: 32 GB
  - Cores: 8
  - Disk Space: 64 GB
- largePremiumLinux
  - RAM: 64 GB
  - Cores: 16
  - Disk Space: 128 GB

Query Codespace machines options

```bash
gh api \
-H "Accept: application/vnd.github+json" \
-H "X-GitHub-Api-Version: 2022-11-28" \
/repos/tigitlabs/pyt-typer-template/codespaces/machines
```

### Install dependencies

### Running in Codespace

Dependencies are installed globally in this script during creation.
[.devcontainer/postCreateCommand.sh](.devcontainer/postCreateCommand.sh)

### Not in Codespace

Install Python venv if not already installed and not running in a Codespace:

```bash
  # Ensure Python 3.6+ is installed
  # Create a virtual environment
  python3 -m venv .venv
  # Activate the virtual environment
  source source .venv/bin/activate
  # Install requierments
  pip install -r requierments.txt
```
