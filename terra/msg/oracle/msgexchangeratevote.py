from terra.utils.jsonserializable import JsonSerializable


class MsgExchangeRateVote(JsonSerializable):
    def __init__(
        self,
        exchangerate: str,
        salt: str,
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Represent the top level of a MsgExchangeRateVote message."""
        self.type = "oracle/MsgExchangeRateVote"
        self.value = MsgExchangeRateVoteValue(
            exchangerate, salt, denom, feeder, validator
        )


class MsgExchangeRateVoteValue(JsonSerializable):
    def __init__(
        self,
        exchangerate: str,
        salt: str,
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Values of a MsgExchangeRateVote message."""
        self.exchangerate = exchangerate
        self.salt = salt
        self.denom = denom
        self.feeder = feeder
        self.validator = validator
