freq = {}
while True:
    try:
        item = input()
    except EOFError:
        break
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

sorted_freq = dict(sorted(freq.items()))

for item in sorted_freq:
    print(sorted_freq[item], item.upper())