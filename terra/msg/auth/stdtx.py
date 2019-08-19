from typing import List

from terra import Account
from terra.msg import Fee
from terra.msg.auth import StdSignMsg
from terra.utils import JsonSerializable


class StdTx(JsonSerializable):

    def __init__(
        self,
        fee: Fee,
        memo: str,
        msg: List[JsonSerializable] = [],
        signatures: List[JsonSerializable] = [],
    ) -> None:
        """Values of a StdTx message."""
        self.fee = fee
        self.memo = memo
        self.msg = msg
        self.signatures = signatures

    def sign_with(self, account: Account):
        signature = StdSignMsg(
            signature='1234',
            pub_key_value=account.public_key,
        )
        self.signatures.append(signature)
