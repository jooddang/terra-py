from terra.msg import Coin
from terra.utils import JsonSerializable


class MsgDelegate(JsonSerializable):

    def __init__(
        self,
        delegator_address: str,
        validator_address: str,
        amount: Coin,
    ) -> None:
        """Represent the top level of a MsgDelegate message."""
        self.type = 'staking/MsgDelegate'
        self.value = MsgDelegateType(
            delegator_address,
            validator_address,
            amount,
        )


class MsgDelegateType(JsonSerializable):

    def __init__(
        self,
        delegator_address: str,
        validator_address: str,
        amount: Coin,
    ) -> None:
        """Types of a MsgDelegate message."""
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.amount = amount
