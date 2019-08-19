import json

from terra import msg
from terra.msg.auth.stdtx import StdTxType

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
    coin = msg.Coin(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[coin])
    value = StdTxType(fee=fee, memo='test', msg=[], signatures=[])
    assert value.to_json() == json.dumps(STD_TX['value'])


def test_stdtx():
    coin = msg.Coin(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[coin])
    stdtx = msg.auth.StdTx(fee=fee, memo='test', msg=[], signatures=[])
    assert stdtx.to_json() == json.dumps(STD_TX)


def test_stdtx_with_msg_msgsend():
    coin_msgsend = msg.Coin(amount='1000', denom='uluna')
    msgsend = msg.pay.MsgSend(
        amount=[coin_msgsend],
        from_address='terra321',
        to_address='terra123',
    )
    coin_stdtx = msg.Coin(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[coin_stdtx])
    stdtx = msg.auth.StdTx(fee=fee, memo='test', msg=[msgsend], signatures=[])
    assert stdtx.value.msg[0] == msgsend
