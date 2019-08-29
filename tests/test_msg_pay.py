import json

from terra import msg
from terra.msg.pay.msgmultisend import MsgMultiSendValue
from terra.msg.pay.msgsend import MsgSendValue

ADDRESS_IN = "terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qv"
ADDRESS_OUT = "terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qk"
MSG_SEND = {
    "type": "pay/MsgSend",
    "value": {
        "amount": [{"denom": "uluna", "amount": "1000"}],
        "from_address": ADDRESS_IN,
        "to_address": ADDRESS_OUT,
    },
}
MSG_MULTI_SEND = {
    "type": "pay/MsgMultiSend",
    "value": {
        "inputs": [
            {
                "address": ADDRESS_IN,
                "coins": [
                    {"denom": "ukrw", "amount": "40"},
                    {"denom": "uluna", "amount": "1000"},
                ],
            }
        ],
        "outputs": [
            {
                "address": ADDRESS_OUT,
                "coins": [
                    {"denom": "ukrw", "amount": "40"},
                    {"denom": "uluna", "amount": "1000"},
                ],
            }
        ],
    },
}


def test_msgsendvalue():
    coin = msg.Coin(amount="1000", denom="uluna")
    value = MsgSendValue(
        amount=[coin], from_address=ADDRESS_IN, to_address=ADDRESS_OUT
    )
    assert value.to_json() == json.dumps(
        MSG_SEND["value"], separators=(",", ":")
    )


def test_msgsend():
    coin = msg.Coin(amount="1000", denom="uluna")
    msgsend = msg.pay.MsgSend(
        amount=[coin], from_address=ADDRESS_IN, to_address=ADDRESS_OUT
    )
    assert msgsend.to_json() == json.dumps(MSG_SEND, separators=(",", ":"))


def test_msgmultisendvalue():
    coin_uluna = msg.Coin(amount="1000", denom="uluna")
    coin_ukrw = msg.Coin(amount="40", denom="ukrw")
    value = MsgMultiSendValue(
        inputs=[msg.InOut(address=ADDRESS_IN, coins=[coin_uluna, coin_ukrw])],
        outputs=[
            msg.InOut(
                address=ADDRESS_OUT, coins=[coin_ukrw, coin_uluna]
            )  # inverted coin order to test sorting
        ],
    )
    assert value.to_json() == json.dumps(
        MSG_MULTI_SEND["value"], separators=(",", ":")
    )


def test_msgmultisend():
    coin_uluna = msg.Coin(amount="1000", denom="uluna")
    coin_ukrw = msg.Coin(amount="40", denom="ukrw")
    value = msg.pay.MsgMultiSend(
        inputs=[msg.InOut(address=ADDRESS_IN, coins=[coin_uluna, coin_ukrw])],
        outputs=[
            msg.InOut(
                address=ADDRESS_OUT, coins=[coin_ukrw, coin_uluna]
            )  # inverted coin order to test sorting
        ],
    )
    assert value.to_json() == json.dumps(MSG_MULTI_SEND, separators=(",", ":"))
