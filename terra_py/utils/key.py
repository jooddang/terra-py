import secrets

from btclib import bip32, bip39


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
        seed = bip39.seed_from_mnemonic(mnemonic, '')
    else:
        raise ValueError('Invalid mnemonic')
    # using bitcoin mainnet version bytes
    return bip32.xmprv_from_seed(seed, bip32.MAINNET_PRV)


def generate_mnemonic(entropy_length: int = 256, lang: str = 'en') -> str:
    """Generates a bip39 mnemonic based on 256 bits of entropy

    Uses the `secrets` module introduced in python 3.6.
    It should be used instead of the `random` module which is not
    designed for security/cryptography.
    """
    entropy = secrets.randbits(entropy_length)
    return bip39.mnemonic_from_entropy(entropy, lang)
