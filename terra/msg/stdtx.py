from terra.msg import Fee
from terra.utils import JsonSerializable


class StdTx(JsonSerializable):

    def __init__(self, fee: Fee, memo: str, msg=[], signatures=[]):
        """Represent the top level of a StdTx message."""
        self.type = 'auth/StdTx'
        self.value = StdTxValue(fee, memo, msg, signatures)


class StdTxValue(JsonSerializable):

    def __init__(self, fee: Fee, memo: str, msg=[], signatures=[]):
        """Values of a StdTx message."""
        self.fee = fee
        self.memo = None
        self.msg = []
        self.signatures = []
