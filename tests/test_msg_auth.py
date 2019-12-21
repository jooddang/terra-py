import json

from terra import Account, msg

STD_TX = {
    "fee": {"gas": "500", "amount": [{"denom": "uluna", "amount": "1000"}]},
    "memo": "test",
    "msg": [],
    "signatures": [],
}
STD_SIGN_MSG = {
    "signature": "1234",
    "pub_key": {
        "type": "tendermint/PubKeySecp256k1",
        "value": "032c2f944ff74e5f40d6c01b171386d3a868c90b25c46ec39a3f4"
        "c0702d4e2cbc6",
    },
}


def test_stdtx():
    coin = msg.Coin(amount="1000", denom="uluna")
    fee = msg.Fee(gas="500", amount=[coin])
    stdtx = msg.auth.StdTx(fee=fee, memo="test", msg=[], signatures=[])
    assert stdtx.to_json() == json.dumps(STD_TX, separators=(",", ":"))


def test_stdtx_with_msg_msgsend():
    coin_msgsend = msg.Coin(amount="1000", denom="uluna")
    msgsend = msg.bank.MsgSend(
        amount=[coin_msgsend], from_address="terra321", to_address="terra123"
    )
    coin_stdtx = msg.Coin(amount="1000", denom="uluna")
    fee = msg.Fee(gas="500", amount=[coin_stdtx])
    stdtx = msg.auth.StdTx(fee=fee, memo="test", msg=[msgsend], signatures=[])
    assert stdtx.msg[0] == msgsend


def test_stdtx_sign():
    """Must match terra-js signature:
    ```javascript
        const terra = require('./dist/src/index.js')
        const mnemonic = "bread genuine element reopen cliff power mean " +
            "quiz mutual six machine planet dry detect edit slim clap firm " +
            "jelly success narrow orange echo tomorrow"
        const masterKey = terra.deriveMasterKeySync(mnemonic)
        const keypair = terra.deriveKeypair(masterKey)
        const accAddr = terra.getAccAddress(keypair.publicKey)

        const msgSend = terra.buildSend(
            [{
                "amount": "1000000",
                "denom": "uluna"
            }],
            "terra18ydtc7jzr07ejkper09rzeysh0qruvfewfk8ch",
            "terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qv"
        );
        const stdTx = terra.buildStdTx([msgSend], {
        "gas": "200000",
        "amount": [
            {
            "amount": "1000",
            "denom": "uluna"
            }
        ]
        }, "library test")
        const jsonTx = stdTx.value
        const txSignature = terra.sign(jsonTx, keypair, {
        sequence: "0",
        account_number: "0",
        chain_id: "columbus-3"
        })
        const signedTx = terra.createSignedTx(stdTx.value, txSignature)
        console.log(signedTx)
    ```
    """
    acc = Account(
        "bread genuine element reopen cliff power mean quiz mutual six "
        "machine planet dry detect edit slim clap firm jelly success na"
        "rrow orange echo tomorrow"
    )
    send = msg.bank.MsgSend(
        amount=[msg.Coin(amount="1000000", denom="uluna")],
        from_address=acc.account_address,
        to_address="terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qv",
    )
    tx = msg.auth.StdTx(
        fee=msg.Fee("200000", [msg.Coin("1000", "uluna")]),
        memo="library test",
        msg=[send],
    )
    tx.sign_with(acc)
    assert tx.signatures[0].signature == (
        "eIBlrEwWAUUqnBd8W0N4YaNYUS7kKC/EZEtzp9asxOpsb0eifCfZYKxn6"
        "aiyZ4oJSJhaYV4p1ExyAi6GQLlLJg=="
    )
    assert tx.signatures[0].pub_key["type"] == "tendermint/PubKeySecp256k1"
    assert tx.signatures[0].pub_key["value"] == (
        "AywvlE/3Tl9A1sAbFxOG06hoyQslxG7Dmj9MBwLU4svG"
    )


def test_stdsignmsg():
    stdsignmsg = msg.auth.StdSignMsg(
        signature=STD_SIGN_MSG["signature"],
        pub_key_type=STD_SIGN_MSG["pub_key"]["type"],
        pub_key_value=STD_SIGN_MSG["pub_key"]["value"],
    )
    assert stdsignmsg.to_json() == json.dumps(
        STD_SIGN_MSG, separators=(",", ":")
    )
