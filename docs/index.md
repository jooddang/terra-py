# Terra-py

Python library for Terra Core

## Example

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
