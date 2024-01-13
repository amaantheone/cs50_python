def main():
    i = input("Input ")
    ans = shorten(i)
    print(f"Output: {ans}")

def shorten(word):
    v = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    res = ""

    for c in word:
        if c not in v:
            res += c

    return res

if __name__ == "__main__":
    main()