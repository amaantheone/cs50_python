from plates import is_valid

def main():
    test_lengthofplate()
    test_numsatstart()
    test_numsatcenter()
    test_0atstart()
    test_symbols()

def test_lengthofplate():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

def test_numsatstart():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_numsatcenter():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA444") == True

def test_0atstart():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_symbols():
    assert is_valid("PI7.73") == False
    assert is_valid("PI2.!23") == False

if __name__ == "__main__":
    main()