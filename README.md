# Terra-py

[![CircleCI](https://circleci.com/gh/terra-project/terra-py/tree/develop.svg?style=svg&circle-token=5f2dc128a3b81385969b69b77db1ed45d9163b5c)](https://circleci.com/gh/terra-project/terra-py/tree/develop)
[![codecov](https://codecov.io/gh/terra-project/terra-py/branch/develop/graph/badge.svg?token=mYwZ5wP3oU)](https://codecov.io/gh/terra-project/terra-py)


Python library for Terra Core

## Installation

todo

## Usage

```python
import os

from terra import Account, msg

acc = Account(os.getenv('MNEMONIC'))
# or generate a new one
# acc = Account.generate()

delegate = msg.staking.MsgDelegate(
    delegator_address=acc.account_address,
    validator_address='terravaloper1p54hc4yy2ajg67j645dn73w3378j6k05vmx9r2',
    amount=msg.Coin(amount='10000', denom='uluna')
)

tx = msg.Tx(
    fee=msg.Fee('10000', [msg.Coin('2000', 'uluna')]),
    memo='Delegating my LUNA tokens',
    msg=[delegate],
)

tx.sign_with(acc)

tx.to_json()
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

Format Code
```bash
poetry run black .
```

Linting and code style

```bash
poetry run flake8 .
```

Static type checking
```bash
poetry run mypy --ignore-missing-imports .
```

Run tests

```bash
poetry run coverage run --source terra -m pytest -v
```
