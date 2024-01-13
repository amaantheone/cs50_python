import sys
import random
import pyfiglet


figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    text = input("Input: ")
    rfont = random.choice(fonts)
    print(pyfiglet.figlet_format(text, font=rfont))

elif len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            text = input("Input: ")
            print(pyfiglet.figlet_format(text, font=sys.argv[2]))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")