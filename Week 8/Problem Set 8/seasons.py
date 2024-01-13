from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        y, m, d = check(birthday)
    except:
        sys.exit("Invalid Date")
    bdate = date(int(y), int(m), int(d))
    present_date = date.today()
    subtract = present_date - bdate
    minutes = subtract.days * 24 * 60
    res = p.number_to_words(minutes, andword="").capitalize()
    print(f"{res}" + " minutes")


def check(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}", birthday):
        y, m, d = birthday.split("-")
        return y, m, d

if __name__ == "__main__":
    main()
