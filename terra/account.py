import hashlib

from mnemonic import Mnemonic
import bech32
import bip32utils


class Account:
    ADDR_PREFIX = {
        'account': 'terra',
        'operator': 'terravaloper',
    }

    def __init__(
        self,
        mnemonic: str,
        account: int = 0,
        index: int = 0
    ) -> None:
        """Class representing an account and its signing capabilities."""
        self.mnemonic = mnemonic
        self.seed = Mnemonic("english").to_seed(self.mnemonic).hex()
        root = self._derive_root(self.seed)
        self.extended_private_key = root.PrivateKey().hex()
        self.extended_public_key = root.PublicKey().hex()
        child = self._derive_child(root, account, index)
        self.private_key = child.PrivateKey().hex()
        self.public_key = child.PublicKey().hex()
        self.address = self._get_address(self.public_key)
        self.account_address = self._get_segwit(
            self.ADDR_PREFIX['account'],
            self.address
        )
        self.operator_address = self._get_segwit(
            self.ADDR_PREFIX['operator'],
            self.address
        )

    def _derive_root(self, seed: str) -> bip32utils.BIP32Key:
        """Derive a root bip32 key object from seed."""
        return bip32utils.BIP32Key.fromEntropy(bytes.fromhex(seed))

    def _derive_child(
        self,
        root: bip32utils.BIP32Key,
        account: int = 0,
        index: int = 0,
    ) -> bip32utils.BIP32Key:
        """Return a child key from a root bip32 Key object.

        Derived with the Luna HDPath "m/44'/330'/0'/0/0".
        """
        return root.ChildKey(
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

    def _get_address(self, public_key: str) -> str:
        """Return the account address.

        The address is the ripmd160 hash of the sha256 hash
        of the public key.
        """
        public_key_bytes = bytes.fromhex(public_key)
        sha = hashlib.sha256()
        rip = hashlib.new('ripemd160')
        sha.update(public_key_bytes)
        rip.update(sha.digest())
        return rip.digest().hex()

    def _get_segwit(self, prefix: str, payload: str) -> str:
        """Return a bech32 Segwit address.

        Computed as bech32 string from the account prefix
        and the account address.

        Note: The `witver` should not be included.
              This is why `bech32_encode` is used over `encode`
              which includes the `witver` by default
        """
        return bech32.bech32_encode(
            prefix,
            bech32.convertbits(bytes.fromhex(payload), 8, 5),
        )
