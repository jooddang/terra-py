import json

from terra import msg
from terra.msg.auth.stdtx import StdTxType
from terra.msg.auth.stdsignmsg import StdSignMsgType

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
STD_SIGN_MSG = {
    'type': 'auth/StdSignMsg',
    'value': {
        'signature': '1234',
        'pub_key': {
            'type': 'tendermint/PubKeySecp256k1',
            'value': '032c2f944ff74e5f40d6c01b171386d3a868c90b25c46ec39a3f4'
                     'c0702d4e2cbc6',
        },
    },
}


def test_stdtxtype():
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


def test_stdsignmsgtype():
    value = StdSignMsgType(
        signature=STD_SIGN_MSG['value']['signature'],
        pub_key=STD_SIGN_MSG['value']['pub_key'],
    )
    assert value.to_json() == json.dumps(STD_SIGN_MSG['value'])


def test_stdsignmsg():
    stdsignmsg = msg.auth.StdSignMsg(
        signature=STD_SIGN_MSG['value']['signature'],
        type_=STD_SIGN_MSG['value']['pub_key']['type'],
        value=STD_SIGN_MSG['value']['pub_key']['value'],
    )
    assert stdsignmsg.to_json() == json.dumps(STD_SIGN_MSG)
