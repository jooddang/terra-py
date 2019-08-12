import json

from terra import msg
from terra.msg.pay.msgsend import MsgSendValue


MSG_SEND = {
    'type': 'pay/MsgSend',
    'value': {
        'amount': [{
            'denom': 'uluna',
            'amount': '1000',
        }],
        'from_address': 'terra321',
        'to_address': 'terra123',
    }
}


def test_msgsendvalue():
    amount = msg.Amount(amount='1000', denom='uluna')
    value = MsgSendValue(
        amount=[amount],
        from_address='terra321',
        to_address='terra123',
    )
    assert value.to_json() == json.dumps(MSG_SEND['value'])


def test_msgsend():
    amount = msg.Amount(amount='1000', denom='uluna')
    msgsend = msg.pay.MsgSend(
        amount=[amount],
        from_address='terra321',
        to_address='terra123',
    )
    assert msgsend.to_json() == json.dumps(MSG_SEND)
