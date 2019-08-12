from terra.utils import JsonSerializable


class Coin(JsonSerializable):

    def __init__(self, denom: str, amount: str):
        """Represent an amount of coin and its denomination"""
        self.denom = denom
        self.amount = amount
