from terra.utils import crypto, JsonSerializable


def test_jsonserializable():
    obj = JsonSerializable()
    obj.a = 'test'
    assert obj.to_json() == '{"a": "test"}'


def test_nested_jsonserializable():
    obj = JsonSerializable()
    nested_obj = JsonSerializable()
    obj.a = 'test'
    nested_obj.a = 'nested_test'
    obj.b = nested_obj
    assert obj.to_json() == '{"a": "test", "b": {"a": "nested_test"}}'


def test_generate_salt():
    salt = crypto.generate_salt()
    assert len(salt) == 4
    assert salt != crypto.generate_salt()
