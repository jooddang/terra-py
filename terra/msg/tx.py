from typing import List
import logging

from terra.account import Account
from terra.api.client import Client
from terra.msg.fee import Fee
from terra.msg.auth.stdsignmsg import StdSignMsg
from terra.msg.auth.stdtx import StdTx
from terra.utils.jsonserializable import JsonSerializable

_log = logging.getLogger(__name__)


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
        memo: str = "",
        mode: str = ReturnType.BLOCK,
        msg: List[JsonSerializable] = [],
        signatures: List[StdSignMsg] = [],
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
        _log.debug(f"Signing tx with account {account.account_address}")
        self.tx.sign_with(account)

    def broadcast(self) -> dict:
        """Helper function to broadcast the tx."""
        _log.debug(f"Broadcasting tx {self.to_json()}")
        return Client().broadcast_tx(self.to_json())
