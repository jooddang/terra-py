import json

from terra import msg
from terra.msg.pay.msgsend import MsgSendValue


MSG_SEND = {
    "type": "pay/MsgSend",
    "value": {
        "amount": [{"denom": "uluna", "amount": "1000"}],
        "from_address": "terra321",
        "to_address": "terra123",
    },
}


def test_msgsendvalue():
    coin = msg.Coin(amount="1000", denom="uluna")
    value = MsgSendValue(
        amount=[coin], from_address="terra321", to_address="terra123"
    )
    assert value.to_json() == json.dumps(
        MSG_SEND["value"], separators=(",", ":")
    )


def test_msgsend():
    coin = msg.Coin(amount="1000", denom="uluna")
    msgsend = msg.pay.MsgSend(
        amount=[coin], from_address="terra321", to_address="terra123"
    )
    assert msgsend.to_json() == json.dumps(MSG_SEND, separators=(",", ":"))
