import pytest

from terra.utils import key

mnemonic = ('bread genuine element reopen cliff power mean quiz mutual '
            'six machine planet dry detect edit slim clap firm jelly '
            'success narrow orange echo tomorrow')
bad_mnemonic = 'this is a bad mnemonic'


def test_validate_mnemonic():
    assert key.validate_mnemonic(mnemonic)
    assert not key.validate_mnemonic(bad_mnemonic)


def test_derive_master_key():
    mnemonic = key.generate_mnemonic()
    master_key = key.derive_master_key(mnemonic)
    assert master_key[:4] == b'xprv'


def test_derive_master_key_raise_valueerror():
    with pytest.raises(ValueError):
        assert key.derive_master_key(bad_mnemonic)


def test_derive_key_pair():
    mnemonic = key.generate_mnemonic()
    master_key = key.derive_master_key(mnemonic)
    key_pair = key.derive_key_pair(master_key)
    assert isinstance(key_pair, key.KeyPair)
    assert key_pair.private_key[:4] == b'xprv'
    assert key_pair.public_key[:4] == b'xpub'


def test_generate_mnemonic():
    mnemonic = key.generate_mnemonic()
    assert key.validate_mnemonic(mnemonic)
