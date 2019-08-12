from terra.utils import JsonSerializable


class Amount(JsonSerializable):

    def __init__(self, amount: str, denom: str):
        """Represent an amount of coin and its denomination."""
        self.denom = denom
        self.amount = amount
