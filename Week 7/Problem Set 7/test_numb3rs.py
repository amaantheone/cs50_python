from numb3rs import validate
import sys

def main():
    test_numb3rs()
    test_range()

def test_numb3rs():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"1234.2334.3.2") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"1000.255.255.255") == False
    assert validate(r"2.3.257.2") == False
    assert validate(r"2.2.256.2") == False

if __name__ == "__main__":
    main()
