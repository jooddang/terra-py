from terra.utils import JsonSerializable


class StdSignMsg(JsonSerializable):

    def __init__(
        self,
        signature: str,
        pub_key_value: str,
        pub_key_type: str = 'tendermint/PubKeySecp256k1',
    ) -> None:
        """Values of a StdSignMsg message.

        Note: Abstract help with building the dictionnary by abstracting its
              construction through method parameters.
        """
        self.signature = signature
        self.pub_key = {'type': pub_key_type, 'value': pub_key_value}
