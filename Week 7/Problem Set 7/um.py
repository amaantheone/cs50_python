import re

def main():
    print(count(input("Text: ")))


def count(s):
    noum = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(noum)


if __name__ == "__main__":
    main()
