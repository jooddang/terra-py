import json

from terra import Account, msg
from terra.msg.tx import ReturnType

ADDRESS = "terra1ptdx6akgk7wwemlk5j73artt5t6j8am08ql3qv"
FEE = {"gas": "500", "amount": [{"denom": "uluna", "amount": "1000"}]}
OUT = {
    "address": ADDRESS,
    "coins": [
        {"denom": "ukrw", "amount": "40"},
        {"denom": "uluna", "amount": "1000"},
    ],
}


def test_coin():
    amount = msg.Coin(amount="1000", denom="uluna")
    assert amount.to_json() == json.dumps(
        FEE["amount"][0], separators=(",", ":")
    )


def test_fee():
    amount = msg.Coin(amount="1000", denom="uluna")
    fee = msg.Fee(gas="500", amount=[amount])
    assert fee.to_json() == json.dumps(FEE, separators=(",", ":"))


def test_inout():
    out = msg.InOut(
        address=ADDRESS,
        coins=[
            msg.Coin(amount="1000", denom="uluna"),
            msg.Coin(amount="40", denom="ukrw"),
        ],
    )
    assert out.to_json() == json.dumps(OUT, separators=(",", ":"))


def test_tx():
    acc = Account(
        "bread genuine element reopen cliff power mean quiz mutual six "
        "machine planet dry detect edit slim clap firm jelly success na"
        "rrow orange echo tomorrow",
        sequence="0",
        account_number="0",
        chain_id="soju",
    )
    send = msg.pay.MsgSend(
        amount=[msg.Coin(amount="1000000", denom="uluna")],
        from_address=acc.account_address,
        to_address=ADDRESS,
    )
    stdtx = msg.auth.StdTx(
        fee=msg.Fee("200000", [msg.Coin("1000", "uluna")]),
        memo="library test",
        msg=[send],
    )
    stdtx.sign_with(acc)
    tx = msg.Tx(
        fee=msg.Fee("200000", [msg.Coin("1000", "uluna")]),
        memo="library test",
        msg=[send],
    )
    tx.sign_with(acc)
    assert tx.tx.to_json() == stdtx.to_json()


def test_returntype():
    assert ReturnType.BLOCK == "block"
    assert ReturnType()
