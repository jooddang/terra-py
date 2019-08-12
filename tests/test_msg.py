from terra import msg


def test_amount():
    amount = msg.Amount(amount='1000', denom='uluna')
    assert amount.to_json() == '{"denom": "uluna", "amount": "1000"}'


def test_fee():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    assert fee.to_json() == '{"gas": "500", "amount": [{"denom": "uluna", "amount": "1000"}]}'  # noqa: E501
