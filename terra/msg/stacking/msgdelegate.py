from terra.msg import Amount
from terra.utils import JsonSerializable


class MsgDelegate(JsonSerializable):

    def __init__(
        self,
        delegator_address: str,
        validator_address: str,
        amount: Amount,
    ) -> None:
        """Represent the top level of a MsgSend message."""
        self.type = 'staking/MsgDelegate'
        self.value = MsgDelegateValue(
            delegator_address,
            validator_address,
            amount,
        )


class MsgDelegateValue(JsonSerializable):

    def __init__(
        self,
        delegator_address: str,
        validator_address: str,
        amount: Amount,
    ) -> None:
        """Values of a MsgSend message."""
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.amount = amount
