months = {
    "January" : "01",
    "February": "02",
    "March"   : "03",
    "April"   : "04",
    "May"    : "05",
    "June"  : "06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}

while True:
    date = input("Date: ")
    if "/" in date:
        fdate = date.split("/")
        try:
            m = int(fdate[0])
        except ValueError:
            continue
        if m < 10:
            m = str(m)
            m = "0" + m

        d = int(fdate[1])
        if d < 10:
            d = str(d)
            d = "0" + d

        y = int(fdate[2])

    else:
        odate = date.split(", ")
        sdate = odate[0].split(" ")

        mname = sdate[0]
        m = 0
        if mname in months:
            m = months[mname]
        try:
            d = int(sdate[1])
        except ValueError:
            continue
        if d < 10:
            d = str(d)
            d = "0" + d
        try:
            y = int(odate[1])
        except:
            continue
        
    if int(m) > 12 or int(d) > 31:
        pass
    else:
        print(f"{y}-{m}-{d}")
        break
