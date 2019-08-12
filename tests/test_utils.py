from terra.utils import JsonSerializable


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
