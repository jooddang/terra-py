from typing import List
import base64

from terra import Account
from terra.msg import Fee
from terra.msg.auth import StdSignMsg
from terra.utils import crypto, JsonSerializable


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

    def sign_with(self, account: Account) -> None:
        """Helper function to sign with a given account.

        Sign the payload with this structure:
        ```
        Fee           auth.StdFee `json:"fee"`
        Memo          string      `json:"memo"`
        Msgs          []sdk.Msg   `json:"msgs"`
        Sequence      uint64      `json:"sequence"`
        AccountNumber uint64      `json:"account_number"`
        ChainID       string      `json:"chain_id"`
        ```
        Order the keys alphabeticaly while dumping to json.
        Sha256 and then SECP256k1 encrypt it with the private key
        of the account passed via the `account` argument.
        Creates a auth/StdSignMsg with that signature and adds it
        to this stdTx signatures.
        """
        payload = JsonSerializable()
        payload.fee = self.fee
        payload.memo = self.memo
        payload.msgs = self.msg
        payload.sequence = account.sequence
        payload.account_number = account.account_number
        payload.chain_id = account.chain_id
        signature = crypto.sha256_and_sign(
            payload=payload.to_json(sort=True).strip(),
            private_key=account.private_key,
        )
        stdsignmsg = StdSignMsg(
            # `decode()` to convert the base64 bytes array to its str repr
            signature=base64.b64encode(signature).decode(),
            pub_key_value=base64.b64encode(
                bytes.fromhex(account.public_key),
            ).decode(),
        )
        self.signatures.append(stdsignmsg)
