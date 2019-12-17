import hashlib

from mnemonic import Mnemonic
import bech32
import bip32utils

from terra import api


class Account:
    ADDR_PREFIX = {"account": "terra", "operator": "terravaloper"}

    def __init__(
        self,
        mnemonic: str,
        account: int = 0,
        index: int = 0,
        chain_id: str = "columbus-3",
    ) -> None:
        """Class representing an account and its signing capabilities."""
        self.mnemonic = mnemonic
        seed = Mnemonic("english").to_seed(self.mnemonic).hex()
        root = self._derive_root(seed)
        child = self._derive_child(root, account, index)
        self.private_key = child.PrivateKey().hex()
        self.public_key = child.PublicKey().hex()
        address = self._get_address(self.public_key)
        self.account_address = self._get_bech(
            self.ADDR_PREFIX["account"], address
        )
        self.operator_address = self._get_bech(
            self.ADDR_PREFIX["operator"], address
        )
        self.chain_id = chain_id
        self._sequence = self._get_sequence()
        self._account_number = self._get_account_number()

    @property
    def sequence(self) -> str:
        """Sequence getter.

        Compare the sequence from the api and the one cached in memory.
        If the api one is higher, set the cached one to the same value.
        Return the cached value.
        """
        api_sequence = self._get_sequence()
        if int(self._sequence) > int(api_sequence):
            return self._sequence
        else:
            self._sequence = api_sequence
            return api_sequence

    @sequence.setter
    def sequence(self, sequence: str) -> None:
        """Sequence setter."""
        self._sequence = sequence

    @property
    def account_number(self) -> str:
        """Account number getter.

        As long as the cached value is equal to 0,
        will replace it by the api result on each call.
        """
        if int(self._account_number) > 0:
            return self._account_number
        else:
            api_account_number = self._get_account_number()
            self._account_number = api_account_number
            return api_account_number

    @classmethod
    def generate(
        cls, account: int = 0, index: int = 0, chain_id: str = "columbus-3"
    ) -> "Account":  # see PEP484 and 563 (type hint yet undefined names)
        """Generate a new account from a random mnemonic"""
        return cls(
            mnemonic=Mnemonic("english").generate(256),
            account=account,
            index=index,
            chain_id=chain_id,
        )

    def _get_sequence(self) -> str:
        """Get sequence from api."""
        return api.auth.accounts.by_address.get(self.account_address)[
            "result"
        ]["value"]["sequence"]

    def _get_account_number(self) -> str:
        """Get account number from api."""
        return api.auth.accounts.by_address.get(self.account_address)[
            "result"
        ]["value"]["account_number"]

    def _derive_root(self, seed: str) -> bip32utils.BIP32Key:
        """Derive a root bip32 key object from seed."""
        return bip32utils.BIP32Key.fromEntropy(bytes.fromhex(seed))

    def _derive_child(
        self, root: bip32utils.BIP32Key, account: int = 0, index: int = 0
    ) -> bip32utils.BIP32Key:
        """Return a child key from a root bip32 Key object.

        Derived with the Luna HDPath "m/44'/330'/0'/0/0".
        """
        return (
            root.ChildKey(44 + bip32utils.BIP32_HARDEN)
            .ChildKey(330 + bip32utils.BIP32_HARDEN)
            .ChildKey(account + bip32utils.BIP32_HARDEN)
            .ChildKey(0)
            .ChildKey(index)
        )

    def _get_address(self, public_key: str) -> str:
        """Return the account address.

        The address is the ripmd160 hash of the sha256 hash
        of the public key.
        """
        public_key_bytes = bytes.fromhex(public_key)
        sha = hashlib.sha256()
        rip = hashlib.new("ripemd160")
        sha.update(public_key_bytes)
        rip.update(sha.digest())
        return rip.digest().hex()

    def _get_bech(self, prefix: str, payload: str) -> str:
        """Return a bech32 address.

        Computed as bech32 string from the account prefix
        and the account address.

        Note: The `witver` should not be included.
              This is why `bech32.bech32_encode` is used over `bech32.encode`
              which includes the `witver` by default
        """
        return bech32.bech32_encode(
            prefix, bech32.convertbits(bytes.fromhex(payload), 8, 5)
        )
