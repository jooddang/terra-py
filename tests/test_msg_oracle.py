import json

from terra import msg
from terra.msg.oracle.msgpriceprevote import MsgPricePrevoteValue
from terra.msg.oracle.msgpricevote import MsgPriceVoteValue

SALT = "8888"
DENOM = "ukrw"
PRICE = "1.1"
FEEDER = "terra1qjsdrnv5u59syrl7yzla9a7qkgwd5g5hk0yfat"
VALIDATOR = "terravaloper1qjsdrnv5u59syrl7yzla9a7qkgwd5g5hkqg5dc"
HASH = "4bcebe0fd3985be92e4da5ad288d925b9e60276f"
MSG_PRICE_PREVOTE = {
    "type": "oracle/MsgPricePrevote",
    "value": {
        "hash": HASH,
        "denom": DENOM,
        "feeder": FEEDER,
        "validator": VALIDATOR,
    },
}
MSG_PRICE_VOTE = {
    "type": "oracle/MsgPriceVote",
    "value": {
        "price": PRICE,
        "salt": SALT,
        "denom": DENOM,
        "feeder": FEEDER,
        "validator": VALIDATOR,
    },
}


def test_msgpriceprevotevalue():
    value = MsgPricePrevoteValue(
        hash_=HASH, denom=DENOM, feeder=FEEDER, validator=VALIDATOR
    )
    assert value.to_json() == json.dumps(
        MSG_PRICE_PREVOTE["value"], separators=(",", ":")
    )


def test_msgpriceprevote():
    msgpriceprevote = msg.oracle.MsgPricePrevote(
        price=PRICE, salt=SALT, denom=DENOM, feeder=FEEDER, validator=VALIDATOR
    )
    assert msgpriceprevote.to_json() == json.dumps(
        MSG_PRICE_PREVOTE, separators=(",", ":")
    )


def test_msgpriceVotevalue():
    value = MsgPriceVoteValue(
        price=PRICE, salt=SALT, denom=DENOM, feeder=FEEDER, validator=VALIDATOR
    )
    assert value.to_json() == json.dumps(
        MSG_PRICE_VOTE["value"], separators=(",", ":")
    )


def test_msgpriceVote():
    msgpricevote = msg.oracle.MsgPriceVote(
        price=PRICE, salt=SALT, denom=DENOM, feeder=FEEDER, validator=VALIDATOR
    )
    assert msgpricevote.to_json() == json.dumps(
        MSG_PRICE_VOTE, separators=(",", ":")
    )
