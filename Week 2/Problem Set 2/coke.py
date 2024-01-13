ad = 50
print("Amount Due:",ad)

while (ad > 0):
    ic = int(input("Insert Coin: "))
    if ic in (25, 10, 5):
        ad -= ic
        if (ad > 0):
          print("Amount Due:", ad)
    else:
        print("Amount Due:", ad)

if ad <= 0:
    co = abs(ad)
    print("Change Owed:",co)
