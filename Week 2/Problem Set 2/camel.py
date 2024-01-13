# get the user input
s = input("camelCase: ")
res = ""

# output the snake case
for c in s:
    if c == c.upper():
        res += '_'
        res += c.lower()
    else:
        res += c

print(res)
