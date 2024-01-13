from jar import Jar

def main():
    testjar()
    testdeposit()
    testwithdraw()
    test()


def testjar():
    jar = Jar()
    assert jar.capacity == 12

def testdeposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def testwithdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(10)
    assert str(jar) == "🍪"

def test():
    jar = Jar()
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

if __name__ == "__main__":
    main()
