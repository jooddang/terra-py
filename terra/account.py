import binascii

from mnemonic import Mnemonic
import bip32utils


class Account:

    def __init__(
        self,
        mnemonic: str,
        account: int = 0,
        index: int = 0
    ) -> None:
        self.mnemonic = Mnemonic("english")
        seed = self.mnemonic.to_seed(mnemonic)
        root = bip32utils.BIP32Key.fromEntropy(seed)
        child = root.ChildKey(
            44 + bip32utils.BIP32_HARDEN
        ).ChildKey(
            330 + bip32utils.BIP32_HARDEN
        ).ChildKey(
            account + bip32utils.BIP32_HARDEN
        ).ChildKey(
            0
        ).ChildKey(
            index
        )
        self.addr = child.Address()
        self.public_key = binascii.hexlify(child.PublicKey()).decode()
        self.private_key = binascii.hexlify(child.PrivateKey()).decode()

    def _hash160(self, public_key: bytes) -> bytes:
        sha = hashlib.sha256()
        rip = hashlib.new('ripemd160')
        sha.update(public_key)
        rip.update(sha.digest())
        return rip.digest()

    def _get_acc_addr(self):
