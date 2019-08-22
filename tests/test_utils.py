from terra.utils import crypto, JsonSerializable


def test_jsonserializable():
    obj = JsonSerializable()
    obj.a = 'test'
    assert obj.to_json() == '{"a":"test"}'


def test_nested_jsonserializable():
    obj = JsonSerializable()
    nested_obj = JsonSerializable()
    obj.a = 'test'
    nested_obj.a = 'nested_test'
    obj.b = nested_obj
    assert obj.to_json() == '{"a":"test","b":{"a":"nested_test"}}'


def test_generate_salt():
    salt = crypto.generate_salt()
    assert len(salt) == 4
    assert salt != crypto.generate_salt()


def test_sha256_and_sign():

    signature = crypto.sha256_and_sign(
        payload='123',
        private_key='861c3746d1bf6bc83acac4c9e72dbe7cdcf944031823b1c7e1248d16'
                    '3c2b9c01',
    )
    assert signature.hex() == (
        '280bf235bc97d4a98b64af088ebc090234e0749d0f9128367c6bea52853b4a682ec3'
        '2c35430a0f7256e0fcb26e8082b30b86da37fbcced5b644728b9dd3c4539'
    )
