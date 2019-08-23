from typing import List, Optional

from terra import Account
from terra.msg import Fee
from terra.utils import JsonSerializable
from terra.msg.auth import StdTx


class ReturnType:
    BLOCK = "block"
    ASYNC = "async"
    SYNC = "sync"

    def __init__(self) -> None:
        """Return types enum.

        Types are:
        - Block : inclusion in block
        - Async : right away
        - Sync  : after checkTx has passed
        """
        pass


class Tx(JsonSerializable):
    def __init__(
        self,
        fee: Fee,
        memo: str,
        mode: Optional[str] = ReturnType.BLOCK,
        msg: Optional[List[JsonSerializable]] = [],
        signatures: Optional[List[JsonSerializable]] = [],
    ) -> None:
        """Abstracted transaction class.

        Abstract away creation of a StdTx and its broadcast body.
        """
        self.tx = StdTx(fee=fee, memo=memo, msg=msg, signatures=signatures)
        self.mode = mode

    def sign_with(self, account: Account) -> None:
        """Helper function to sign the tx with a given account.

        Proxy `StdTx().sign_with()`.
        """
        self.tx.sign_with(account)
