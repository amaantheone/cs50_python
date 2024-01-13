from bank import value

def main():
    test_give_0()
    test_give_20()
    test_give_100()

def test_give_0():
    assert value("hello bro") == 0
    assert value("Hello") == 0
    assert value("Hello wassup") == 0

def test_give_20():
    assert value("Hey") == 20
    assert value("Hi") == 20
    assert value("Heya") == 20

def test_give_100():
    assert value("good mornin") == 100
    assert value("ayo wassup") == 100

if __name__ == "__main__":
    main()