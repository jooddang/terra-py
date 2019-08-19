from typing import Dict

from terra.utils import JsonSerializable


class StdSignMsg(JsonSerializable):

    def __init__(
        self,
        signature: str,
        value: str,
        type_: str = 'tendermint/PubKeySecp256k1',  # `type` is reserved
    ) -> None:
        """Represent the top level of a StdTx message.

        Note: Abstract help with building the dictionnary by abstracting its
              construction through method parameters.
        """
        self.type = 'auth/StdSignMsg'
        self.value = StdSignMsgType(signature, {'type': type_, 'value': value})


class StdSignMsgType(JsonSerializable):

    def __init__(
        self,
        signature: str,
        pub_key: Dict[str, str],
    ) -> None:
        """Types of a StdTx message."""
        self.signature = signature
        self.pub_key = pub_key
