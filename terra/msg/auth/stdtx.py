from typing import List

from terra.msg import Fee
from terra.utils import JsonSerializable


class StdTx(JsonSerializable):

    def __init__(
        self,
        fee: Fee,
        memo: str,
        msg: List[JsonSerializable] = [],
        signatures: List[JsonSerializable] = [],
    ) -> None:
        """Represent the top level of a StdTx message."""
        self.type = 'auth/StdTx'
        self.value = StdTxType(fee, memo, msg, signatures)


class StdTxType(JsonSerializable):

    def __init__(
        self,
        fee: Fee,
        memo: str,
        msg: List[JsonSerializable] = [],
        signatures: List[JsonSerializable] = [],
    ) -> None:
        """Types of a StdTx message."""
        self.fee = fee
        self.memo = memo
        self.msg = msg
        self.signatures = signatures
