import json

from terra import msg
from terra.msg.staking.msgdelegate import MsgDelegateValue
from terra.msg.staking.msgbeginredelegate import MsgBeginRedelegateValue
from terra.msg.staking.msgundelegate import MsgUndelegateValue

COIN = msg.Coin(amount='1000', denom='uluna')
DELEGATOR_ADDRESS = ''
VALIDATOR_ADDRESS = ''
MSG_DELEGATE = {
    'type': 'staking/MsgDelegate',
    'value': {
        'delegator_address': DELEGATOR_ADDRESS,
        'validator_address': VALIDATOR_ADDRESS,
        'amount': COIN.__dict__,
    }
}
MSG_BEGIN_REDELEGATE = {
    'type': 'staking/MsgBeginRedelegate',
    'value': {
        'delegator_address': DELEGATOR_ADDRESS,
        'validator_src_address': VALIDATOR_ADDRESS,
        'validator_dst_address': VALIDATOR_ADDRESS,
        'amount': COIN.__dict__,
    }
}
MSG_UNDELEGATE = {
    'type': 'staking/MsgUndelegate',
    'value': {
        'delegator_address': DELEGATOR_ADDRESS,
        'validator_address': VALIDATOR_ADDRESS,
        'amount': COIN.__dict__,
    }
}


def test_msgdelegatevalue():
    value = MsgDelegateValue(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
        amount=COIN,
    )
    assert value.to_json() == json.dumps(MSG_DELEGATE['value'])


def test_msgdelegate():
    msgsend = msg.staking.MsgDelegate(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
        amount=COIN,
    )
    assert msgsend.to_json() == json.dumps(MSG_DELEGATE)


def test_msgbeginredelegatevalue():
    value = MsgBeginRedelegateValue(
        delegator_address=DELEGATOR_ADDRESS,
        validator_src_address=VALIDATOR_ADDRESS,
        validator_dst_address=VALIDATOR_ADDRESS,
        amount=COIN,
    )
    assert value.to_json() == json.dumps(MSG_BEGIN_REDELEGATE['value'])


def test_msgbeginredelegate():
    msgsend = msg.staking.MsgBeginRedelegate(
        delegator_address=DELEGATOR_ADDRESS,
        validator_src_address=VALIDATOR_ADDRESS,
        validator_dst_address=VALIDATOR_ADDRESS,
        amount=COIN,
    )
    assert msgsend.to_json() == json.dumps(MSG_BEGIN_REDELEGATE)


def test_msgundelegatevalue():
    value = MsgUndelegateValue(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
        amount=COIN,
    )
    assert value.to_json() == json.dumps(MSG_UNDELEGATE['value'])


def test_msgundelegate():
    msgsend = msg.staking.MsgUndelegate(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
        amount=COIN,
    )
    assert msgsend.to_json() == json.dumps(MSG_UNDELEGATE)
