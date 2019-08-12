import json

from terra import msg
from terra.msg.auth.stdtx import StdTxValue

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


def test_stdtxvalue():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    value = StdTxValue(fee=fee, memo='test', msg=[], signatures=[])
    assert value.to_json() == json.dumps(STD_TX['value'])


def test_stdtx():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    stdtx = msg.auth.StdTx(fee=fee, memo='test', msg=[], signatures=[])
    assert stdtx.to_json() == json.dumps(STD_TX)


def test_stdtx_with_msg_msgsend():
    amount_msgsend = msg.Amount(amount='1000', denom='uluna')
    msgsend = msg.pay.MsgSend(
        amount=[amount_msgsend],
        from_address='terra321',
        to_address='terra123',
    )
    amount_stdtx = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount_stdtx])
    stdtx = msg.auth.StdTx(fee=fee, memo='test', msg=[msgsend], signatures=[])
    assert stdtx.value.msg[0] == msgsend
