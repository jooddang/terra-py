from terra_py.utils import key

mnemonic = ('bread genuine element reopen cliff power mean quiz mutual '
            'six machine planet dry detect edit slim clap firm jelly '
            'success narrow orange echo tomorrow')


def test_validate_mnemonic():
    assert key.validate_mnemonic(mnemonic)
    assert not key.validate_mnemonic('wrong mnemonic')
