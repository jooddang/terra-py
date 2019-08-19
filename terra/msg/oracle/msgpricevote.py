from terra.utils import JsonSerializable


class MsgPriceVote(JsonSerializable):

    def __init__(
        self,
        price: str,
        salt: str,
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Represent the top level of a MsgPriceVote message.

        If a hash_ is provided, it will override price and salt.
        """
        self.type = 'oracle/MsgPriceVote'
        self.value = MsgPriceVoteType(
            price,
            salt,
            denom,
            feeder,
            validator,
        )


class MsgPriceVoteType(JsonSerializable):

    def __init__(
        self,
        price: str,
        salt: str,
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Types of a MsgPriceVote message."""
        self.price = price
        self.salt = salt
        self.denom = denom
        self.feeder = feeder
        self.validator = validator
