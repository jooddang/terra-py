from terra import msg
from terra.msg.stdtx import StdTxValue


def test_amount():
    amount = msg.Amount(amount='1000', denom='uluna')
    assert amount.to_json() == '{"denom": "uluna", "amount": "1000"}'


def test_fee():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    assert fee.to_json() == '{"gas": "500", "amount": [{"denom": "uluna", "amount": "1000"}]}'  # noqa: E501


def test_stdtxvalue():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    value = StdTxValue(fee=fee, memo='test', msg=[], signatures=[])
    assert value.to_json() == '{"fee": {"gas": "500", "amount": [{"denom": "uluna", "amount": "1000"}]}, "memo": "test", "msg": [], "signatures": []}'  # noqa: E501


def test_stdtx():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    value = msg.StdTx(fee=fee, memo='test', msg=[], signatures=[])
    assert value.to_json() == '{"type": "auth/StdTx", "value": {"fee": {"gas": "500", "amount": [{"denom": "uluna", "amount": "1000"}]}, "memo": "test", "msg": [], "signatures": []}}'  # noqa: E501
