# tests/test_main.py
from sum import add_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(3, 4) == 7
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(-2, -3) == -5