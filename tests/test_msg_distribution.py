import json

from terra import msg
from terra.msg.distribution.msgsetwithdrawaddress import (
    MsgSetWithdrawAddressValue,
)
from terra.msg.distribution.msgwithdrawdelegatorreward import (
    MsgWithdrawDelegatorRewardValue,
)

DELEGATOR_ADDRESS = "terra1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0ayw2s"
WITHDRAW_ADDRESS = "terra1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0ayw2s"
VALIDATOR_ADDRESS = "terravaloper1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0jgn6r"
MSG_SET_WITHDRAW_ADDRESS = {
    "type": "distribution/MsgSetWithdrawAddress",
    "value": {
        "delegator_address": DELEGATOR_ADDRESS,
        "withdraw_address": WITHDRAW_ADDRESS,
    },
}
MSG_WITHDRAW_DELEGATOR_REWARD = {
    "type": "distribution/MsgWithdrawDelegatorReward",
    "value": {
        "delegator_address": DELEGATOR_ADDRESS,
        "validator_address": VALIDATOR_ADDRESS,
    },
}


def test_msgsetwithdrawaddressvalue():
    value = MsgSetWithdrawAddressValue(
        delegator_address=DELEGATOR_ADDRESS, withdraw_address=WITHDRAW_ADDRESS
    )
    assert value.to_json() == json.dumps(
        MSG_SET_WITHDRAW_ADDRESS["value"], separators=(",", ":")
    )


def test_msgsetwithdrawaddress():
    msgsetwithdrawaddress = msg.distribution.MsgSetWithdrawAddress(
        delegator_address=DELEGATOR_ADDRESS, withdraw_address=WITHDRAW_ADDRESS
    )
    assert msgsetwithdrawaddress.to_json() == json.dumps(
        MSG_SET_WITHDRAW_ADDRESS, separators=(",", ":")
    )


def test_msgwithdrawdelegatorrewardvalue():
    value = MsgWithdrawDelegatorRewardValue(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
    )
    assert value.to_json() == json.dumps(
        MSG_WITHDRAW_DELEGATOR_REWARD["value"], separators=(",", ":")
    )


def test_msgwithdrawdelegatorreward():
    msgwithdrawdelegatorreward = msg.distribution.MsgWithdrawDelegatorReward(
        delegator_address=DELEGATOR_ADDRESS,
        validator_address=VALIDATOR_ADDRESS,
    )
    assert msgwithdrawdelegatorreward.to_json() == json.dumps(
        MSG_WITHDRAW_DELEGATOR_REWARD, separators=(",", ":")
    )
