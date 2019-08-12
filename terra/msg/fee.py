from typing import List

from terra.msg import Amount
from terra.utils import JsonSerializable


class Fee(JsonSerializable):

    def __init__(self, gas: str, amount: List[Amount]):
        """Represent a transaction fee."""
        self.gas = gas
        self.amount = []
