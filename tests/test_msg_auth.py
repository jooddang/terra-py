import json

from terra import Account, msg

STD_TX = {
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
}
STD_SIGN_MSG = {
    'signature': '1234',
    'pub_key': {
        'type': 'tendermint/PubKeySecp256k1',
        'value': '032c2f944ff74e5f40d6c01b171386d3a868c90b25c46ec39a3f4'
                 'c0702d4e2cbc6',
    },
}


def test_stdtx():
    coin = msg.Coin(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[coin])
    stdtx = msg.auth.StdTx(fee=fee, memo='test', msg=[], signatures=[])
    assert stdtx.to_json() == json.dumps(STD_TX, separators=(',', ':'))


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
    assert stdtx.msg[0] == msgsend


def test_stdtx_sign():
    mnemonic = (
        'bread genuine element reopen cliff power mean quiz mutual '
        'six machine planet dry detect edit slim clap firm jelly '
        'success narrow orange echo tomorrow'
    )
    acc = Account(mnemonic)
    coin = msg.Coin(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[coin])
    stdtx = msg.auth.StdTx(fee=fee, memo='test', msg=[], signatures=[])
    stdtx.sign_with(acc)
    # temporary
    assert stdtx.signatures[0].signature == '1234'


def test_stdsignmsg():
    stdsignmsg = msg.auth.StdSignMsg(
        signature=STD_SIGN_MSG['signature'],
        pub_key_type=STD_SIGN_MSG['pub_key']['type'],
        pub_key_value=STD_SIGN_MSG['pub_key']['value'],
    )
    assert stdsignmsg.to_json() == json.dumps(
        STD_SIGN_MSG,
        separators=(',', ':')
    )
