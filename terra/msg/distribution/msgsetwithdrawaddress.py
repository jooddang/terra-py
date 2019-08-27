from terra.utils.jsonserializable import JsonSerializable


class MsgSetWithdrawAddress(JsonSerializable):
    def __init__(self, delegator_address: str, withdraw_address: str) -> None:
        """Represent the top level of a MsgSetWithdrawAddress message."""
        self.type = "distribution/MsgSetWithdrawAddress"
        self.value = MsgSetWithdrawAddressValue(
            delegator_address, withdraw_address
        )


class MsgSetWithdrawAddressValue(JsonSerializable):
    def __init__(self, delegator_address: str, withdraw_address: str) -> None:
        """Values of a MsgSetWithdrawAddress message."""
        self.delegator_address = delegator_address
        self.withdraw_address = withdraw_address
