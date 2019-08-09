from collections import namedtuple
import secrets

from btclib import bip32, bip39

KeyPair = namedtuple('KeyPair', ['private_key', 'public_key'])


def validate_mnemonic(mnemonic: str, lang: str = 'en') -> bool:
    """Validate a mnemonic by trying to get its entropy"""
    try:
        bip39.entropy_from_mnemonic(mnemonic, lang)
        return True
    except ValueError:
        return False


def derive_master_key(mnemonic: str) -> bytes:
    """Derive a master key from a given mnemonic"""
    if validate_mnemonic(mnemonic):
        # empty string for no passphrase
        return bip39.mprv_from_mnemonic(mnemonic, '', bip32.MAINNET_PRV)
    else:
        raise ValueError('Invalid mnemonic')


def derive_key_pair(master_key: bytes, account: int = 0, index: int = 0) -> KeyPair:  # noqa: E501
    """Derive a key pair (priv + pub key) from a given master key"""
    luna_hd_path = f'm/44\'/330\'/{account}\'/0/{index}'
    private_key = bip32.derive(master_key, luna_hd_path)
    public_key = bip32.xpub_from_xprv(master_key)
    return KeyPair(private_key, public_key)


def generate_mnemonic(entropy_length: int = 256, lang: str = 'en') -> str:
    """Generates a bip39 mnemonic based on 256 bits of entropy

    Uses the `secrets` module introduced in python 3.6.
    It should be used instead of the `random` module which is not
    designed for security/cryptography.
    """
    entropy = secrets.randbits(entropy_length)
    return bip39.mnemonic_from_entropy(entropy, lang)
