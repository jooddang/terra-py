import json

from terra import msg

FEE = {
    'gas': '500',
    'amount': [{
        'denom': 'uluna',
        'amount': '1000',
    }],
}


def test_amount():
    amount = msg.Amount(amount='1000', denom='uluna')
    assert amount.to_json() == json.dumps(FEE['amount'][0])


def test_fee():
    amount = msg.Amount(amount='1000', denom='uluna')
    fee = msg.Fee(gas='500', amount=[amount])
    assert fee.to_json() == json.dumps(FEE)
