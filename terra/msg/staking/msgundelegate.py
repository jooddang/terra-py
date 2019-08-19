from terra.msg import Coin
from terra.utils import JsonSerializable


class MsgUndelegate(JsonSerializable):

    def __init__(
        self,
        delegator_address: str,
        validator_address: str,
        amount: Coin,
    ) -> None:
        """Represent the top level of a MsgUndelegate message."""
        self.type = 'staking/MsgUndelegate'
        self.value = MsgUndelegateType(
            delegator_address,
            validator_address,
            amount,
        )


class MsgUndelegateType(JsonSerializable):

    def __init__(
        self,
        delegator_address: str,
        validator_address: str,
        amount: Coin,
    ) -> None:
        """Types of a MsgUndelegate message."""
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.amount = amount
