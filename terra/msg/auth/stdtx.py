from typing import List
import base64

from terra.account import Account
from terra.msg.auth.stdsignmsg import StdSignMsg
from terra.msg.fee import Fee
from terra.utils import crypto
from terra.utils.jsonserializable import JsonSerializable


class StdTx(JsonSerializable):
    def __init__(
        self,
        fee: Fee,
        memo: str = "",
        msg: List[JsonSerializable] = [],
        signatures: List[StdSignMsg] = [],
    ) -> None:
        """Values of a StdTx message."""
        self.fee = fee
        self.memo = memo
        self.msg = msg or []
        self.signatures = signatures or []

    def sign_with(self, account: Account) -> None:
        """Helper function to sign the StdTx with a given account.

        Sign the tx payload built with this structure:
        ```
        Fee           Fee               `json:"fee"`
        Memo          string            `json:"memo"`
        Msgs          JsonSerializable  `json:"msgs"`
        Sequence      string            `json:"sequence"`
        AccountNumber string            `json:"account_number"`
        ChainID       string            `json:"chain_id"`
        ```
        Order the keys alphabeticaly while dumping to json.
        Sha256 and then SECP256k1 encrypt it with the private key
        of the account passed via the `account` argument.
        Creates a auth/StdSignMsg with that signature and adds it
        to this stdTx signatures.
        """
        payload = SignPayload(
            fee=self.fee,
            memo=self.memo,
            msg=self.msg,
            sequence=account.sequence,
            account_number=account.account_number,
            chain_id=account.chain_id,
        )
        signature = crypto.sha256_and_sign(
            payload=payload.to_json(sort=True).strip(),
            private_key=account.private_key,
        )
        stdsignmsg = StdSignMsg(
            # `decode()` to convert the base64 bytes array to its str repr
            signature=base64.b64encode(signature).decode(),
            pub_key_value=base64.b64encode(
                bytes.fromhex(account.public_key)
            ).decode(),
        )
        self.signatures.append(stdsignmsg)


class SignPayload(JsonSerializable):
    def __init__(
        self,
        fee: Fee,
        memo: str,
        msg: List[JsonSerializable],
        sequence: str,
        account_number: str,
        chain_id: str,
    ) -> None:
        """StdTx structured as a payload ready to be signed."""
        self.fee = fee
        self.memo = memo
        self.msg = msg
        self.sequence = sequence
        self.account_number = account_number
        self.chain_id = chain_id
