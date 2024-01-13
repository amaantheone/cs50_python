#ask the user for a greeting
greet = input("Greeting: ")
new_greet = greet.lower().strip()

#if the greeting starts with hello output 0$
if "hello" in new_greet:
    print("$0")

#if the greeting starts with h output $20
elif 'h' == new_greet[0]:
    print("$20")

#else output $100
else:
    print("$100")