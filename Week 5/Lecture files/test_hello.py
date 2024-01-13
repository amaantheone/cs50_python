from hello import hello

def test_default():
    hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"