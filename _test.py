import pytest
from app import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, -1) == -2
    assert add(0, 5) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError):  # Test division by zero
        divide(5, 0)