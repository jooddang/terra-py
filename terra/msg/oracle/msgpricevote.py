from terra.utils.jsonserializable import JsonSerializable


class MsgPriceVote(JsonSerializable):
    def __init__(
        self, price: str, salt: str, denom: str, feeder: str, validator: str
    ) -> None:
        """Represent the top level of a MsgPriceVote message."""
        self.type = "oracle/MsgPriceVote"
        self.value = MsgPriceVoteValue(price, salt, denom, feeder, validator)


class MsgPriceVoteValue(JsonSerializable):
    def __init__(
        self, price: str, salt: str, denom: str, feeder: str, validator: str
    ) -> None:
        """Values of a MsgPriceVote message."""
        self.price = price
        self.salt = salt
        self.denom = denom
        self.feeder = feeder
        self.validator = validator
