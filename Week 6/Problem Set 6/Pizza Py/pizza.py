import sys
import csv
from tabulate import tabulate

def main():
    check_arg()
    data = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(data[1:], headers=data[0], tablefmt="grid"))

def check_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
