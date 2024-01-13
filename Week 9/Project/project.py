import random

def main():
    print("Welcome to the number guessing game!")
    num = random.randint(1, 10)
    tries = 4
    for _ in range(tries):
        ans = int(input("Guess a number from 1 to 10 "))
        if ans > 10:
            print("invalid number")
        if num == ans:
            print("Correct Answer")
            break
        if num != ans:
            print("Incorrect Answer")
            print("Tries:", tries)
            tries -= 1
        if tries == 0:
            break

if __name__ == "__main__":
    main()
