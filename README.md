# Terra-py

[![CircleCI](https://circleci.com/gh/terra-project/terra-py/tree/develop.svg?style=svg&circle-token=5f2dc128a3b81385969b69b77db1ed45d9163b5c)](https://circleci.com/gh/terra-project/terra-py/tree/develop)
[![codecov](https://codecov.io/gh/terra-project/terra-py/branch/develop/graph/badge.svg?token=mYwZ5wP3oU)](https://codecov.io/gh/terra-project/terra-py)


Python library for Terra Core

**NOTE:** This is an early version and interface changes could occure until `v1.0.0`.

## Installation

```
pip3 install terra-core
```

## Usage

- [Example](#example)
- [Module `terra`](#module-terra)
    - [`msg`](#module-terramsg)
        - [`auth`](#module-terramsgauth)
        - [`distribution`](#module-terramsgdistribution)
        - [`market`](#module-terramsgmarket)
        - [`oracle`](#module-terramsgoracle)
        - [`pay`](#module-terramsgpay)
        - [`staking`](#module-terramsgstaking)
    - [`utils`](#module-terrautils)
        - [`crypto`](#module-terrautilscrypto)

### Example

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

### Module `terra`

```python
Account(
    mnemonic: str,
    account: int = 0,
    index: int = 0,
    sequence: str = "0",
    account_number: str = "0",
    chain_id: str = "",
)
Account.generate(
    account: int = 0,
    index: int = 0,
    sequence: str = "0",
    account_number: str = "0",
    chain_id: str = "",
)  # return Account
```

### Module `terra.msg`

```python
Coin(
    amount: str,
    denom: str,
)
Coin().to_json(
    sort: bool = False,
)  # return str

Fee(
    gas: str,
    amount: List[terra.msg.Coin],
)
Fee().to_json(
    sort: bool = False,
)  # return str

InOut(
    address: str,
    coins: List[terra.msg.Coin],
)
InOut().to_json(
    sort: bool = False,
)  # return str

ReturnType()
ReturnType.BLOCK
ReturnType.ASYNC
ReturnType.SYNC

Tx(
    fee: terra.msg.Fee,
    memo: str = "",
    mode: str = terra.msg.ReturnType.BLOCK,
    msg: List[terra.utils.JsonSerializable] = [],
    signatures: List[terra.msg.auth.StdSignMessage] = [],
)
Tx().sign_with(
    account: terra.Account,
)  # return None
Tx().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.msg.auth`

```python
StdSignMsg(
    signature: str,
    pub_key_value: str,
    pub_key_type: str = "tendermint/PubKeySecp256k1",
)
StdSignMsg().to_json(
    sort: bool = False,
)  # return str

StdTx(
    fee: terra.msg.Fee,
    memo: str = "",
    msg: List[terra.utils.JsonSerializable] = [],  # all terra.msg classes inherit from JsonSerializable
    signatures: List[terra.msg.auth.StdSignMessage] = [],
)
StdTx().sign_with(
    account: terra.Account,
)  # return None
StdTx().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.msg.distribution`

```python
MsgSetWithdrawAddress(
    delegator_address: str,
    withdraw_address: str,
)
MsgSetWithdrawAddress().to_json(
    sort: bool = False,
)  # return str

MsgWithdrawDelegatorReward(
    delegator_address: str,
    validator_address: str,
)
MsgWithdrawDelegatorReward().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.msg.market`

```python
MsgSwap(
    trader: str,
    offer_coin: terra.msg.Coin,
    ask_denom: str,
)
MsgSwap().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.msg.oracle`

```python
MsgPricePrevote(
    price: str,
    salt: str,
    denom: str,
    feeder: str,
    validator: str
)
MsgPricePrevote().to_json(
    sort: bool = False,
)  # return str

MsgPriceVote(
    price: str,
    salt: str,
    denom: str,
    feeder: str,
    validator: str,
)
MsgPriceVote().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.msg.pay`

```python
MsgMultiSend(
    inputs: List[terra.msg.InOut],
    outputs: List[terra.msg.InOut],
)
MsgMultiSend().to_json(
    sort: bool = False,
)  # return str

MsgSend(
    amount: List[terra.msg.Coin],
    from_address: str,
    to_address: str
)
MsgSend().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.msg.staking`

```python
MsgBeginRedelegate(
    delegator_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: terra.msg.Coin,
)
MsgBeginRedelegate().to_json(
    sort: bool = False,
)  # return str

MsgDelegate(
    delegator_address: str,
    validator_address: str,
    amount: terra.msg.Coin,
)
MsgDelegate().to_json(
    sort: bool = False,
)  # return str

MsgUndelegate(
    delegator_address: str,
    validator_address: str,
    amount: terra.msg.Coin,
)
MsgUndelegate().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.utils`

```python
JsonSerializable()
JsonSerializable().to_json(
    sort: bool = False,
)  # return str
```

### Module `terra.utils.crypto`

```python
generate_salt()  # return str

sha256_and_sign(
    payload: str,
    private_key: str,
    curve: ecdsa.curves.Curve = ecdsa.SECP256k1,
    canonize: bool = True,
)  # return bytes

sha256(
    payload: str,
)  # return bytes
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
