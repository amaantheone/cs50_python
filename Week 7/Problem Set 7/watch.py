import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9]+)", s)
        if pattern:
            url = pattern.groups()
            return f"https://youtu.be/{url[3]}"



if __name__ == "__main__":
    main()
