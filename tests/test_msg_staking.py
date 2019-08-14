import json

from terra import msg
from terra.msg.staking.msgdelegate import MsgDelegateValue

AMOUNT = msg.Amount(amount='1000', denom='uluna')
DELEGATOR_ADDRESS = ''
VALIDATOR_ADDRESS = ''
MSG_DELEGATE = {
    'type': 'staking/MsgDelegate',
    'value': {
        'delegator_address': DELEGATOR_ADDRESS,
        'validator_address': VALIDATOR_ADDRESS,
        'amount': AMOUNT.__dict__,
    }
}


def test_msgdelegatevalue():
    value = MsgDelegateValue(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
        amount=AMOUNT,
    )
    assert value.to_json() == json.dumps(MSG_DELEGATE['value'])


def test_msgdelegate():
    msgsend = msg.staking.MsgDelegate(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
        amount=AMOUNT,
    )
    assert msgsend.to_json() == json.dumps(MSG_DELEGATE)
