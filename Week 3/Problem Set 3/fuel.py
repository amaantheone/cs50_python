while True:
    try:
        f = input("Fraction: ")
        f = f.split("/")
        f1 = int(f[0])
        f2 = int(f[1])
        res = round((f1/f2) * 100)
        if res == 99 or res == 100:
            print("F")
            break
        elif res == 0 or res == 1:
            print("E")
            break
        elif f1 > f2:
            pass
        else:
            print(f"{res}%")
            break
    except (ValueError, ZeroDivisionError):
        pass