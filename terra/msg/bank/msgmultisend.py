from typing import List

from terra.msg.inout import InOut
from terra.utils.jsonserializable import JsonSerializable


class MsgMultiSend(JsonSerializable):
    def __init__(self, inputs: List[InOut], outputs: List[InOut]) -> None:
        """Represent the top level of a MsgMultiSend message."""
        self.type = "bank/MsgMultiSend"
        self.value = MsgMultiSendValue(inputs, outputs)


class MsgMultiSendValue(JsonSerializable):
    def __init__(self, inputs: List[InOut], outputs: List[InOut]) -> None:
        """Values of a MsgMultiSend message."""
        self.inputs = inputs
        self.outputs = outputs
