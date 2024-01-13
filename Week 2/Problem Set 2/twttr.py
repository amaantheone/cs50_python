s = input("Input: ")
v = ("a", "e", "i", "o", "u")

res = ""
for c in s:
    if c.lower() not in v:
        res += c

print("Output:", res)