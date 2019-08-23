from hashlib import sha256

from terra.utils import JsonSerializable


class MsgPricePrevote(JsonSerializable):
    def __init__(
        self, price: str, salt: str, denom: str, feeder: str, validator: str
    ) -> None:
        """Represent the top level of a MsgPricePrevote message."""
        self.type = "oracle/MsgPricePrevote"
        self.value = MsgPricePrevoteValue(
            self._metadata_to_hash(price, salt, denom, feeder),
            denom,
            feeder,
            validator,
        )

    def _metadata_to_hash(
        self, price: str, salt: str, denom: str, voter: str
    ) -> str:
        """Build the vote hash from metadata.

        The vote hash is the 20 first SHA256 bytes of:
        `salt:price:denom:voter`
        https://docs.terra.money/specifications/oracle
        """
        sha_hash = sha256(f"{salt}:{price}:{denom}:{voter}".encode())
        return sha_hash.hexdigest()[:-20]


class MsgPricePrevoteValue(JsonSerializable):
    def __init__(
        self,
        hash_: str,  # trailing underscore as `hash` is reserved
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Values of a MsgPricePrevote message."""
        self.hash = hash_
        self.denom = denom
        self.feeder = feeder
        self.validator = validator
