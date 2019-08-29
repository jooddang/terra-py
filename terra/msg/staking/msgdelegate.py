from terra.msg.coin import Coin
from terra.utils.jsonserializable import JsonSerializable


class MsgDelegate(JsonSerializable):
    def __init__(
        self, delegator_address: str, validator_address: str, amount: Coin
    ) -> None:
        """Represent the top level of a MsgDelegate message."""
        self.type = "staking/MsgDelegate"
        self.value = MsgDelegateValue(
            delegator_address, validator_address, amount
        )


class MsgDelegateValue(JsonSerializable):
    def __init__(
        self, delegator_address: str, validator_address: str, amount: Coin
    ) -> None:
        """Values of a MsgDelegate message."""
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.amount = amount
