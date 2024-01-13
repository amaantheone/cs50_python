import sys
import csv

def main():
    check_arg()
    res = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"].split(",")
                res.append({"first": name[1].lstrip(), "last": name[0], "house": row["house"]})



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        write = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        write.writerow({"first": "first", "last": "last", "house": "house"})
        for row in res:
            write.writerow({"first": row["first"], "last": row["last"], "house": row ["house"]})

def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
