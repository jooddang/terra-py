from terra.msg.coin import Coin
from terra.utils.jsonserializable import JsonSerializable


class MsgSwap(JsonSerializable):
    def __init__(self, trader: str, offer_coin: Coin, ask_denom: str) -> None:
        """Represent the top level of a MsgSwap message."""
        self.type = "market/MsgSwap"
        self.value = MsgSwapValue(trader, offer_coin, ask_denom)


class MsgSwapValue(JsonSerializable):
    def __init__(self, trader: str, offer_coin: Coin, ask_denom: str) -> None:
        """Values of a MsgSwap message."""
        self.trader = trader
        self.offer_coin = offer_coin
        self.ask_denom = ask_denom
