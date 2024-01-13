import random

n = -1
guess = -1
while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            continue
        break
    except ValueError:
        pass

res = random.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < res:
            print("Too small!")
        elif guess > res:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass