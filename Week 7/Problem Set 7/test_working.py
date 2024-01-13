from working import convert
import pytest

def main():
    test_1()
    test_2()
    test_main()

def test_1():
    with pytest.raises(ValueError):
        convert("14 PM - 19 PM")

def test_2():
    with pytest.raises(ValueError):
        convert("11:60 AM to 7:60 PM")

def test_main():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
