from typing import List

from terra.msg.coin import Coin
from terra.utils.jsonserializable import JsonSerializable


class InOut(JsonSerializable):
    def __init__(self, address: str, coins: List[Coin]) -> None:
        """Represent a input or output of multisend."""
        self.address = address
        self.coins = sorted(coins, key=lambda o: o.denom)
