# Terra-py

[![CircleCI](https://circleci.com/gh/terra-project/terra-py/tree/develop.svg?style=svg&circle-token=5f2dc128a3b81385969b69b77db1ed45d9163b5c)](https://circleci.com/gh/terra-project/terra-py/tree/develop)
[![codecov](https://codecov.io/gh/terra-project/terra-py/branch/develop/graph/badge.svg?token=mYwZ5wP3oU)](https://codecov.io/gh/terra-project/terra-py)


Python library for Terra Core

**NOTE:** This is an early version and interface changes could occure until `v1.0.0`.

Please heads-up to the [documentation](http://terra-project.github.io/terra-py) for complete modules description and more details.

## Installation

Virtualenv:
```shell
virtualenv -p python3.6 .venv  # if not already created
source .venv/bin/activate
pip install terra-core
```

Poetry:
```shell
poetry add terra-core
```

Pipenv
```shell
pipenv install terra-core
```

## Example

```python
import os

from terra import Account
from terra import api
from terra import msg

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

res = tx.broadcast()
```

Complete api in the [documentation](http://terra-project.github.io/terra-py).

## Develop

To contribute to terra-py developement, please check how to contribute in the [documentation](http://terra-project.github.io/terra-py/contribute/)
