import json

from terra import msg
from terra.msg.oracle.msgexchangerateprevote import MsgExchangeRatePrevoteValue
from terra.msg.oracle.msgexchangeratevote import MsgExchangeRateVoteValue

SALT = "8888"
DENOM = "ukrw"
EXCHANGE_RATE = "1.1"
FEEDER = "terra1qjsdrnv5u59syrl7yzla9a7qkgwd5g5hk0yfat"
VALIDATOR = "terravaloper1qjsdrnv5u59syrl7yzla9a7qkgwd5g5hkqg5dc"
HASH = "cbe1e46fbf41925604d3c2b02977d9295b2cacbb"
MSG_EXCHANGE_RATE_PREVOTE = {
    "type": "oracle/MsgExchangeRatePrevote",
    "value": {
        "hash": HASH,
        "denom": DENOM,
        "feeder": FEEDER,
        "validator": VALIDATOR,
    },
}
MSG_EXCHANGE_RATE_VOTE = {
    "type": "oracle/MsgExchangeRateVote",
    "value": {
        "exchangerate": EXCHANGE_RATE,
        "salt": SALT,
        "denom": DENOM,
        "feeder": FEEDER,
        "validator": VALIDATOR,
    },
}


def test_msgexchangeratePrevotevalue():
    value = MsgExchangeRatePrevoteValue(
        hash_=HASH, denom=DENOM, feeder=FEEDER, validator=VALIDATOR
    )
    assert value.to_json() == json.dumps(
        MSG_EXCHANGE_RATE_PREVOTE["value"], separators=(",", ":")
    )


def test_msgexchangeratePrevote():
    MsgExchangeRatePrevote = msg.oracle.MsgExchangeRatePrevote(
        exchangerate=EXCHANGE_RATE,
        salt=SALT,
        denom=DENOM,
        feeder=FEEDER,
        validator=VALIDATOR,
    )
    assert MsgExchangeRatePrevote.to_json() == json.dumps(
        MSG_EXCHANGE_RATE_PREVOTE, separators=(",", ":")
    )


def test_msgexchangerateVotevalue():
    value = MsgExchangeRateVoteValue(
        exchangerate=EXCHANGE_RATE,
        salt=SALT,
        denom=DENOM,
        feeder=FEEDER,
        validator=VALIDATOR,
    )
    assert value.to_json() == json.dumps(
        MSG_EXCHANGE_RATE_VOTE["value"], separators=(",", ":")
    )


def test_msgexchangerateVote():
    msgexchangeratevote = msg.oracle.MsgExchangeRateVote(
        exchangerate=EXCHANGE_RATE,
        salt=SALT,
        denom=DENOM,
        feeder=FEEDER,
        validator=VALIDATOR,
    )
    assert msgexchangeratevote.to_json() == json.dumps(
        MSG_EXCHANGE_RATE_VOTE, separators=(",", ":")
    )
