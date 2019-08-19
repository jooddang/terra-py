from terra.msg import Coin
from terra.utils import JsonSerializable


class MsgSend(JsonSerializable):

    def __init__(
        self,
        amount: [Coin],
        from_address: str,
        to_address: str,
    ) -> None:
        """Represent the top level of a MsgSend message."""
        self.type = 'pay/MsgSend'
        self.value = MsgSendType(amount, from_address, to_address)


class MsgSendType(JsonSerializable):

    def __init__(
        self,
        amount: [Coin],
        from_address: str,
        to_address: str,
    ) -> None:
        """Types of a MsgSend message."""
        self.amount = sorted(amount, key=lambda o: o.denom)
        self.from_address = from_address
        self.to_address = to_address
