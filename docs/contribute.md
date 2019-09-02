# Contribute

This project uses [poetry](https://github.com/sdispater/poetry) to manage dependencies and packaging.

## Install poetry

The recommanded way to install poetry is through it's custom installer that adds vendorized dependencies to make it independant from your system.

```shell
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

## General

### Install dependencies
```shell
poetry install
```

### Format Code
```shell
poetry run black .
```

### Linting and code style
```shell
poetry run flake8 .
```

### Static type checking
```shell
poetry run mypy --ignore-missing-imports .
```

### Run tests and check coverage
```shell
poetry run coverage run --source terra -m pytest -v
poetry run coverage report
```

### Serve documentation

```shell
poetry run mkdocs serve
```

## Contributing

Open a PR against develop.
