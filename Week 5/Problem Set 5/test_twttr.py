from twttr import shorten

def main():
    test_argument()
    test_numbers()
    test_symbols()

def test_argument():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("tWiTtEr") == "tWTtr"

def test_numbers():
    assert shorten("1234") == "1234"

def test_symbols():
    assert shorten(".,/?!@#") == ".,/?!@#"

if __name__ == "__main__":
    main()