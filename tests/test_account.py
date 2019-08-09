from terra import Account

acc_mnemonic = (
    'bread genuine element reopen cliff power mean quiz mutual '
    'six machine planet dry detect edit slim clap firm jelly '
    'success narrow orange echo tomorrow'
)
bad_mnemonic = 'this is a bad mnemonic'
acc_xprv_bytes = (
    b'xprvA3nap1LYVDzy4hVsRfusMKgqPVcMawYjZXTWPonuy52fVAUTR6Y'
    b'EASDCCsFs6Yn7ogwsc6nqAJU26guXTaUadNJvajCZ7eVyNH9CkQ24A1Z')
acc_xprv_str = (
    'xprvA3nap1LYVDzy4hVsRfusMKgqPVcMawYjZXTWPonuy52fVAUTR6Y'
    'EASDCCsFs6Yn7ogwsc6nqAJU26guXTaUadNJvajCZ7eVyNH9CkQ24A1Z'
)


def test_account_key_as_bytes():
    a = Account(acc_xprv_bytes)
    assert isinstance(a.private_key, bytes)


def test_account_key_as_string():
    a = Account(acc_xprv_str)
    assert isinstance(a.private_key, bytes)


def test_account_from_mnemonic():
    a = Account.from_mnemonic(acc_mnemonic)
    assert isinstance(a.private_key, bytes)
    assert a.private_key[:4] == b'xprv'
    assert a.private_key == acc_xprv_bytes


def test_public_key_getter():
    a = Account(acc_xprv_bytes)
    assert a.public_key is not None
    assert a.public_key[:4] == b'xpub'


def test_mnemonic_to_master_key():
    assert isinstance(
        Account._mnemonic_to_master_key(acc_mnemonic),
        bytes,
    )


def test_master_key_to_extended_private_key():
    mk = Account._mnemonic_to_master_key(acc_mnemonic)
    xprv = Account._master_key_to_extended_private_key(mk)
    assert xprv == acc_xprv_bytes
