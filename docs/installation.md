# Installation

Requirements:

- Python >= 3.6

## Virtualenv

```bash
virtualenv -p python3.6 .venv
source .venv/bin/activate
pip install terra-core
```

## Poetry

```bash
poetry add terra-core
```

## Pipenv

```bash
pipenv install terra-core
```

## System (not recommended)

!!! Warning
    It is not reccomended to install packages directly to your system. Please use a virtualenv or a dependency management tool.

```bash
# system wide
pip3 install terra-core

# or user specific
pip3 install --user terra-core
```
