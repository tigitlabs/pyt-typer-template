# pyt-typer-template

Template for a Python CLI application using [Typer](https://typer.tiangolo.com/)  
[Typer GitHub repository](https://github.com/tiangolo/typer)

## Roadmap

- [x] Add requirements with conda
- [x] Add logging
- [x] Add linting
- [x] Add formatting
- [x] Add type checking
- [x] Add three CLI commands with typer
- [x] Add tests
- [X] Add code coverage
- [x] Add pre-commit hooks
- [ ] Add CI/CD for Ubuntu and Windows
- [ ] Convert to a cookiecutter template

## Requirements

### CI/CD

- Run test on Ubuntu and Windows
- pre-commit hooks
  - black
  - flake8
  - mypy
  - pytest
  - coverage

### Python

- dependencies with [conda](https://docs.conda.io/en/latest/)
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

### Dev Environment

Designed to work with Github Codespaces

#### Working in a Codespace

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

## Usage

### Install dependencies

### Running in Codespace

```bash
  conda activate $CONDA_ENV_NAME
```

### Not in Codespace

Install conda if not already installed or not running in a Codespace

```bash
  # https://docs.conda.io/projects/miniconda/en/latest/

  mkdir -p ~/miniconda3
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
  bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
  rm -rf ~/miniconda3/miniconda.sh
```

Create conda environment

```bash
  conda env create --file environment.yml
  conda activate typer_template
```

Update conda environment with new dependencies

```bash
  conda env update
```
