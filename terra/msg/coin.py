from terra.utils import JsonSerializable


class Coin(JsonSerializable):
    def __init__(self, amount: str, denom: str) -> None:
        """Represent an amount of coin and its denomination."""
        self.denom = denom
        self.amount = amount
