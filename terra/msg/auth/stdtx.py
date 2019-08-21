from typing import List
import base64
import hashlib

from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_string_canonize

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
        payload = JsonSerializable()
        payload.fee = self.fee
        payload.memo = self.memo
        payload.msgs = self.msg
        payload.sequence = account.sequence
        payload.account_number = account.account_number
        payload.chain_id = account.chain_id
        # TODO refactor crypto stuff out in a new `utils.crypto`
        sk = SigningKey.from_string(
            bytes.fromhex(account.private_key),
            curve=SECP256k1
        )
        signature = sk.sign_deterministic(
            payload.to_json(sort=True).encode(),
            hashfunc=hashlib.sha256,
            sigencode=sigencode_string_canonize,
        )
        stdsignmsg = StdSignMsg(
            signature=base64.encodebytes(signature).decode(),
            pub_key_value=base64.b64encode(
                bytes.fromhex(account.public_key)
            ).decode(),
        )
        self.signatures.append(stdsignmsg)
