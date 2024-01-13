def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not len(s) >= 2 or not len(s) <= 6:
        return False
    
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    numstart = False
    fnum = -1

    for c in s:
        if fnum == -1:
            if c.isnumeric():
                fnum = int(c)
        if fnum == 0:
            return False

        if c.isnumeric():
            numstart = True
        if numstart == True:
            if c.isalpha():
                return False

        if not c.isalpha() and not c.isnumeric():
            return False

    return True


if __name__ == "__main__":
    main()