from hashlib import sha256

from terra.utils.jsonserializable import JsonSerializable


class MsgExchangeRatePrevote(JsonSerializable):
    def __init__(
        self,
        exchangerate: str,
        salt: str,
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Represent the top level of a MsgExchangeRatePrevote message."""
        self.type = "oracle/MsgExchangeRatePrevote"
        self.value = MsgExchangeRatePrevoteValue(
            self._metadata_to_hash(exchangerate, salt, denom, validator),
            denom,
            feeder,
            validator,
        )

    def _metadata_to_hash(
        self, exchangerate: str, salt: str, denom: str, validator: str
    ) -> str:
        """Build the vote hash from metadata.

        The vote hash is the 20 first SHA256 bytes of:
        `salt:exchangerate:denom:voter`
        https://docs.terra.money/specifications/oracle
        """
        sha_hash = sha256(
            f"{salt}:{exchangerate}:{denom}:{validator}".encode()
        )
        return sha_hash.hexdigest()[:40]


class MsgExchangeRatePrevoteValue(JsonSerializable):
    def __init__(
        self,
        hash_: str,  # trailing underscore as `hash` is reserved
        denom: str,
        feeder: str,
        validator: str,
    ) -> None:
        """Values of a MsgExchangeRatePrevote message."""
        self.hash = hash_
        self.denom = denom
        self.feeder = feeder
        self.validator = validator
