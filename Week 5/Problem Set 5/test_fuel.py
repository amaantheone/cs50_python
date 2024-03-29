from fuel import convert, gauge
import pytest

def main():
    test_rightinput()
    test_divisionbyzero()
    test_notnum()

def test_rightinput():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("2/100") == 2 and gauge(2) == "2%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_divisionbyzero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_notnum():
    with pytest.raises(ValueError):
        convert("yo/hello")
