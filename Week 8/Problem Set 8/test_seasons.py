from seasons import check

def main():
    testbirthday()

def testbirthday():
    assert check("2010-07-03") == ("2010", "07", "03")
    assert check ("1998-7-3") == None



if __name__ == "__main__":
    main()
