def main():
    greeting = input("Greeting: ")
    x = value(greeting)
    print(f"${x}")


def value(greeting):
    new_greeting = greeting.lower().strip()

    if "hello" in new_greeting:
        return 0
    elif 'h' == new_greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()