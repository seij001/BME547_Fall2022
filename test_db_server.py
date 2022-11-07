import pytest


@pytest.mark.parametrize("in_data, expected_keys, expected_types, expected", [
    ({"a": 1, "b": "string"}, ["a", "b"], [int, str], True),
    ({"a": 1, "b": 2}, ["a", "b"], [int, str],
     "Key b's value has the wrong data type"),
    ({"c": 1, "b": "string"}, ["a", "b"], [int, str],
     "Key a is missing from POST data"),
    (["a", "b", 1, 2], ["a", "b"], [int, str],
     "POST data was not a dictionary"),
    ({"a": "1", "b": "string"}, ["a", "b"], [int, str],
     "Key a's value has the wrong data type"),
    ({"a": 1, "b": "string", "c": True}, ["a", "b"], [int, str], True),
])
def test_dictionary_validation(in_data, expected_keys, expected_types,
                               expected):
    from db_server import dictionary_validation
    answer = dictionary_validation(in_data, expected_keys, expected_types)
    assert answer == expected
