from terra.msg.coin import Coin
from terra.utils.jsonserializable import JsonSerializable


class MsgBeginRedelegate(JsonSerializable):
    def __init__(
        self,
        delegator_address: str,
        validator_src_address: str,
        validator_dst_address: str,
        amount: Coin,
    ) -> None:
        """Represent the top level of a MsgBeginRedelegate message."""
        self.type = "staking/MsgBeginRedelegate"
        self.value = MsgBeginRedelegateValue(
            delegator_address,
            validator_src_address,
            validator_dst_address,
            amount,
        )


class MsgBeginRedelegateValue(JsonSerializable):
    def __init__(
        self,
        delegator_address: str,
        validator_src_address: str,
        validator_dst_address: str,
        amount: Coin,
    ) -> None:
        """Values of a MsgBeginRedelegate message."""
        self.delegator_address = delegator_address
        self.validator_src_address = validator_src_address
        self.validator_dst_address = validator_dst_address
        self.amount = amount
