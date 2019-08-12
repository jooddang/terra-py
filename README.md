# Terra-py

[![CircleCI](https://circleci.com/gh/terra-project/terra-py/tree/develop.svg?style=svg&circle-token=5f2dc128a3b81385969b69b77db1ed45d9163b5c)](https://circleci.com/gh/terra-project/terra-py/tree/develop)
[![codecov](https://codecov.io/gh/terra-project/terra-py/branch/develop/graph/badge.svg?token=mYwZ5wP3oU)](https://codecov.io/gh/terra-project/terra-py)


Python library for Terra Core

## Installation

todo

## Usage

```python
from terra import msg

m = msg.auth.StdTx(
    fee=msg.Fee('10000', [msg.Amount('2000', 'uluna')]),
    memo='test transaction',
    msg=[
        msg.pay.MsgSend(
            amount=[msg.Amount('10', 'uluna')],
            from_address='terra7wwemlk5j73artt5t6j8am08ql3qv1ptdx6akgk',
            to_address='terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qv',
        ),
    ],
)

m.to_json()
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
