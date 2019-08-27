import json

from terra import msg
from terra.msg.market.msgswap import MsgSwapValue

TRADER = "terra1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0ayw2s"
COIN = msg.Coin(amount="1000", denom="uluna")
ASK_DENOM = "ukrw"
MSG_SWAP = {
    "type": "market/MsgSwap",
    "value": {
        "trader": TRADER,
        "offer_coin": COIN.__dict__,
        "ask_denom": ASK_DENOM,
    },
}


def test_msgdelegatevalue():
    value = MsgSwapValue(trader=TRADER, offer_coin=COIN, ask_denom=ASK_DENOM)
    assert value.to_json() == json.dumps(
        MSG_SWAP["value"], separators=(",", ":")
    )


def test_msgdelegate():
    msgsend = msg.market.MsgSwap(
        trader=TRADER, offer_coin=COIN, ask_denom=ASK_DENOM
    )
    assert msgsend.to_json() == json.dumps(MSG_SWAP, separators=(",", ":"))
