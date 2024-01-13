import sys

def main():
    checkarg()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    count = -1
    for line in lines:
        if line_check(line) == False:
            count += 1
    print(count)

def checkarg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a command-line argument")

def line_check(line):
    if line.isspace():
        return True
    elif line.strip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
