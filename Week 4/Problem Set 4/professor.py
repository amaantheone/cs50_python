import random

def main():
    level = get_level()
    score = game(level)
    print(f"Score: {score}")

def get_level():
    n = -1
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                break
        except ValueError:
            pass
    return n

def generate_integer(level):
    if level == 1:
        start, end = 0, 9
    elif level == 2:
        start, end = 10, 99
    elif level == 3:
        start, end = 100, 999
    a = random.randint(start,end)
    b = random.randint(start,end)
    return a, b

def game(level):
    score = 10
    for _ in range(10):
        tries = 3
        a, b = generate_integer(level)
        while(tries):
            try:
                ans = int(input(f"{a} + {b} = "))
                res = a + b
                if ans != res:
                    print("EEE")
                    tries -= 1
                elif ans == res:
                    break
            except ValueError:
                print("EEE")
                tries -= 1
        if tries == 0:
            print(f"{a} + {b} = {res}")
            score -= 1
    return score

if __name__ == "__main__":
    main()