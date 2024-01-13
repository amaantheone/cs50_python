from um import count

def main():
    test_1()
    test_2()

def test_1():
    assert count("um, ") == 1
    assert count("hello, um, world") == 1
    assert count("UM, ") == 1

def test_2():
    assert count("yummy") == 0
    assert count("yum") == 0
