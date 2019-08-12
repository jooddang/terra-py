# Terra-py

Python library for Terra Core

## Installation

todo

## Usage

```python
from terra import msg

m = msg.StdTx(
    fee=msg.Fee('10000', [msg.Coin('2000', 'uluna')]),
    memo='test transaction',
)
```

## Develop

Install poetry

```bash
pip install --user poetry
```

Install dependencies

```bash
poetry install
```

Run tests

```bash
poetry run coverage run --source terra -m pytest -v
```
