import pytest

from terra_py.utils import key

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


def test_generate_mnemonic():
    mnemonic = key.generate_mnemonic()
    assert key.validate_mnemonic(mnemonic)
