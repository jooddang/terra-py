from terra import msg


def test_amount():
    amount = msg.Amount(amount='1000', denom='uluna')
    assert amount.to_json() == '{"denom": "uluna", "amount": "1000"}'
