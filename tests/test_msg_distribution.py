import json

from terra import msg
from terra.msg.distribution.msgsetwithdrawaddress import (
    MsgSetWithdrawAddressValue,
)

DELEGATOR_ADDRESS = "terravaloper1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0jgn6r"
WITHDRAW_ADDRESS = "terra1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0ayw2s"
MSG_SET_WITHDRAW_ADDRESS = {
    "type": "distribution/MsgSetWithdrawAddress",
    "value": {
        "delegator_address": DELEGATOR_ADDRESS,
        "withdraw_address": WITHDRAW_ADDRESS,
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
