from terra.utils.jsonserializable import JsonSerializable


class MsgWithdrawDelegatorReward(JsonSerializable):
    def __init__(self, delegator_address: str, validator_address: str) -> None:
        """Represent the top level of a MsgWithdrawDelegatorReward message."""
        self.type = "distribution/MsgWithdrawDelegatorReward"
        self.value = MsgWithdrawDelegatorRewardValue(
            delegator_address, validator_address
        )


class MsgWithdrawDelegatorRewardValue(JsonSerializable):
    def __init__(self, delegator_address: str, validator_address: str) -> None:
        """Values of a MsgWithdrawDelegatorReward message."""
        self.delegator_address = delegator_address
        self.validator_address = validator_address
