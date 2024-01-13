def main():
    #ask time
    question = input("What time is it?")
    #convert
    time = convert(question)
    #if time is between 7 and 8
    if time >= 7 and time <= 8:
        print("breakfast time")
    #if time is between 12 and 13
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    #split hours and minutes
    hours, minutes = time.split(":")
    #convert time into decimal
    new_minute = float(minutes) / 60
    #return the result
    return float(hours) + new_minute

if __name__ == "__main__":
    main()