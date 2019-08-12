import json

from terra import msg
from terra.msg.msgsend import MsgSendValue
from terra.msg.stdtx import StdTxValue

STD_TX = {
    'type': 'auth/StdTx',
    'value': {
        'fee': {
            'gas': '500',
            'amount': [{
                'denom': 'uluna',
                'amount': '1000',
            }],
        },
        'memo': 'test',
        'msg': [],
        'signatures': [],
    },
}

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


def test_amount():
    amount = msg.Amount(amount='1000', denom='uluna')
    assert amount.to_json() == json.dumps(STD_TX['value']['fee']['amount'][0])


def test_fee():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    assert fee.to_json() == json.dumps(STD_TX['value']['fee'])


def test_stdtxvalue():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    value = StdTxValue(fee=fee, memo='test', msg=[], signatures=[])
    assert value.to_json() == json.dumps(STD_TX['value'])


def test_stdtx():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    value = msg.StdTx(fee=fee, memo='test', msg=[], signatures=[])
    assert value.to_json() == json.dumps(STD_TX)


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
    value = msg.MsgSend(
        amount=[amount],
        from_address='terra321',
        to_address='terra123',
    )
    assert value.to_json() == json.dumps(MSG_SEND)
