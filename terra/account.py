from typing import Type, TypeVar, Union

from btclib import bip32, bip39

LUNA_HD_PATH = 'm/44\'/330\'/{}\'/0/{}'

T = TypeVar('T')  # Binded to `cls` in `classmethod`s for the return type hint


class Account:

    def __init__(self, private_key: Union[bytes, str]) -> None:
        """Represent a Terra account and it's signing capabilities."""
        try:
            self.private_key = bytes(private_key, 'utf-8')
        except TypeError:
            self.private_key = private_key
        self._public_key = None

    @classmethod
    def from_mnemonic(cls: Type[T], mnemonic: str, passphrase: str = '', account: int = 0, index: int = 0) -> T:  # noqa: E501
        """Returns an `Account` instance build from an mnemonic,"""
        master_key = cls._mnemonic_to_master_key(mnemonic, passphrase)
        return cls(cls._master_key_to_extended_private_key(master_key))

    @staticmethod
    def _mnemonic_to_master_key(mnemonic: str, passphrase: str = '') -> bytes:
        """Returns a BIP39 master key from a mnemonic,"""
        return bip39.mprv_from_mnemonic(mnemonic, passphrase, bip32.PRV[0])

    @staticmethod
    def _master_key_to_extended_private_key(master_key: bytes, account: int = 0, index: int = 0) -> bytes:  # noqa: E501
        """Returns a BIP32 extended private key from a BIP39 master key,"""
        return bip32.derive(master_key, LUNA_HD_PATH.format(account, index))

    @property
    def public_key(self):
        """Getter for the extended public key.
        If it not yet defined, compute and set it.
        """
        if not self._public_key:
            self._public_key = bip32.xpub_from_xprv(self.private_key)
        return self._public_key
