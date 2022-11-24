from pytest_project.func_set import set_


def test_set_():
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 8) == {"a": {"b": {"c": 8}}}
    assert set_({"a": {"b": {"c": 3}}}, ["q", "z", "w"], 2) == {"a": {"b": {"c": 3}}, "q": {"z": {"w": 2}}}
