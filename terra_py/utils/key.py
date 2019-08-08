import secrets

from btclib import bip39


def generate_mnemonic(entropy_length: int = 256) -> str:
    """Generates a bip39 mnemonic based on 256 bits of entropy

    Uses the `secrets` module introduced in python 3.6.
    It should be used instead of the `random` module which is not
    designed for security/cryptography.
    """
    entropy = secrets.randbits(entropy_length)
    return bip39.mnemonic_from_entropy(entropy, 'en')
