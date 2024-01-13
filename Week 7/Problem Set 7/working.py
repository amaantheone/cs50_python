import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches =  re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if matches:
        time = matches.groups()
        if int(time[1]) > 12 or int(time[5]) > 12:
            raise ValueError
        ftime = format(time[1], time[2], time[3])
        stime = format(time[5], time[6], time[7])
        return f"{ftime} to {stime}"
    else:
        raise ValueError

def format(hour, minute, meridian):
    if meridian == "AM":
        if int(hour) == 12:
            nhour = 0
        else:
            nhour = int(hour)
    else:
        if int(hour) == 12:
            nhour = 12
        else:
            nhour = int(hour) + 12
    if minute == None:
        nmint = ":00"
        ntime = f"{nhour:02}{nmint}"
    else:
        ntime = f"{nhour:02}:{minute}"
    return ntime

if __name__ == "__main__":
    main()
