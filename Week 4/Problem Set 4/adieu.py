names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
if len(names) == 1:
    print(f"\nAdieu, adieu, to {names[0]}")

elif len(names) == 2:
    print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")

elif len(names) > 2:
    names1 = names[0:-1]
    names2 = names[-1]
    print("\nAdieu, adieu, to",end=' ')
    print(', '.join(names1), end=', ')
    print(f"and {names2}")