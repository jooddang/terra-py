# Modules

Documentation of the modules apis.

# terra

Account:
```python
Account(
    mnemonic: str
    account: int = 0,
    index: int = 0,
    chain_id: str = "columbus-3",
)

Account().generate() -> Account
```

Exceptions:
```python
# Raised when an error occured while communicating with the API
ApiError()
```

# terra.api

The api module is wrapping some endpoints from [Terra lcd server](https://swagger.terra.money/).

You can change the api endpoint used by setting:
```python
terra.api.Client.URL = "https://my.lcd.server"
```

Client:
```python
Client(api_network=ApiNetwork.MAINNET)

Client().get(
    path: str,
    params: Optional[Dict[str, str]] = None,
    timeout: Optional[int] = 5,
) -> dict

Client().post(
    path: str,
    json: Optional[Dict[str, str]],
    params: Optional[Dict[str, str]] = None,
    timeout: Optional[int] = 10,
) -> dict
```

**Note**: You should probably not have to use this class.
It is meant for internal use.

## terra.api.auth

accounts:
```python
accounts.get(
    address: str
) -> dict
```

## terra.api.bank

balances:
```python
balances.get(
    address: str
) -> dict
```

## terra.api.oracle

denoms:
```python
denoms.get() -> dict
```

## terra.api.tendermint

blocks:
```python
blocks.get() -> dict
```

node_info:
```python
node_info.get() -> dict
```

txs:
```python
txs.post(tx_dump: str) -> dict
```

# terra.msg

Coin:
```python
Coin(
    amount: str,
    denom: str,
)

Coin().to_json(
    sort: bool = False,
) -> str
```

Fee:
```python
Fee(
    gas: str,
    amount: List[terra.msg.Coin],
)

Fee().to_json(
    sort: bool = False,
) -> str
```

InOut:
```python
InOut(
    address: str,
    coins: List[terra.msg.Coin],
)

InOut().to_json(
    sort: bool = False,
) -> str
```

ReturnType:
```python
ReturnType()

ReturnType.BLOCK
ReturnType.ASYNC
ReturnType.SYNC
```

Tx:
```python
Tx(
    fee: terra.msg.Fee,
    memo: str = "",
    mode: str = terra.msg.ReturnType.BLOCK,
    msg: List[terra.utils.JsonSerializable] = [],
    signatures: List[terra.msg.auth.StdSignMessage] = [],
)

Tx().sign_with(
    account: terra.Account,
) -> None

Tx().broadcast() -> dict:

Tx().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.auth

StdSignMsg:
```python
StdSignMsg(
    signature: str,
    pub_key_value: str,
    pub_key_type: str = "tendermint/PubKeySecp256k1",
)

StdSignMsg().to_json(
    sort: bool = False,
) -> str
```

StdTx:
```python
StdTx(
    fee: terra.msg.Fee,
    memo: str = "",
    msg: List[terra.utils.JsonSerializable] = [],  # all terra.msg classes inherit from JsonSerializable
    signatures: List[terra.msg.auth.StdSignMessage] = [],
)

StdTx().sign_with(
    account: terra.Account,
) -> None

StdTx().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.distribution

MsgSetWithdrawAddress:
```python
MsgSetWithdrawAddress(
    delegator_address: str,
    withdraw_address: str,
)

MsgSetWithdrawAddress().to_json(
    sort: bool = False,
) -> str
```

MsgWithdrawDelegatorReward:
```python
MsgWithdrawDelegatorReward(
    delegator_address: str,
    validator_address: str,
)

MsgWithdrawDelegatorReward().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.market

MsgSwap:
```python
MsgSwap(
    trader: str,
    offer_coin: terra.msg.Coin,
    ask_denom: str,
)

MsgSwap().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.oracle

MsgExchangeRatePrevote:
```python
MsgExchangeRatePrevote(
    price: str,
    salt: str,
    denom: str,
    feeder: str,
    validator: str
)

MsgExchangeRatePrevote().to_json(
    sort: bool = False,
) -> str
```

MsgExchangeRateVote:
```python
MsgExchangeRateVote(
    price: str,
    salt: str,
    denom: str,
    feeder: str,
    validator: str,
)

MsgExchangeRateVote().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.bank

MsgMultiSend:
```python
MsgMultiSend(
    inputs: List[terra.msg.InOut],
    outputs: List[terra.msg.InOut],
)

MsgMultiSend().to_json(
    sort: bool = False,
) -> str
```

MsgSend:
```python
MsgSend(
    amount: List[terra.msg.Coin],
    from_address: str,
    to_address: str
)

MsgSend().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.staking

MsgBeginRedelegate:
```python
MsgBeginRedelegate(
    delegator_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: terra.msg.Coin,
)

MsgBeginRedelegate().to_json(
    sort: bool = False,
) -> str
```

MsgDelegate:
```python
MsgDelegate(
    delegator_address: str,
    validator_address: str,
    amount: terra.msg.Coin,
)

MsgDelegate().to_json(
    sort: bool = False,
) -> str
```

MsgUndelegate:
```python
MsgUndelegate(
    delegator_address: str,
    validator_address: str,
    amount: terra.msg.Coin,
)

MsgUndelegate().to_json(
    sort: bool = False,
) -> str
```

# terra.utils

JsonSerializable:
```python
JsonSerializable()

JsonSerializable().to_json(
    sort: bool = False,
) -> str
```

## terra.utils.crypto

generate_salt:
```python
generate_salt() -> str
```

sha256_and_sign:
```python
sha256_and_sign(
    payload: str,
    private_key: str,
    curve: ecdsa.curves.Curve = ecdsa.SECP256k1,
    canonize: bool = True,
) -> bytes
```

sha256:
```python
sha256(
    payload: str,
) -> bytes
```
