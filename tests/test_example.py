import pytest

def add_one(x) -> int:
    return x + 1

def system_exit_raised() -> None:
    raise SystemExit(1)

class TestClass:
    def test_method(self):
        pass

def test_add_one():
    assert add_one(4) == 5

def test_system_exit_raised():
    with pytest.raises(SystemExit):
        system_exit_raised()

def test_class_method_exists():
    test_object = TestClass()

    assert hasattr(test_object, "test_method")
