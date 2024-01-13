import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    arg_check()
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size_of_shirt = shirt.size
    person = ImageOps.fit(image, size_of_shirt)
    person.paste(shirt, shirt)
    person.save(sys.argv[2])

def arg_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    first_file = splitext(sys.argv[1])
    second_file = splitext(sys.argv[2])
    if image_check(first_file[1]) == False:
        sys.exit("Invalid input")
    elif image_check(second_file[1]) == False:
        sys.exit("Invalid output")
    elif first_file[1].lower() != second_file[1].lower():
        sys.exit("Input and output have different extensions")

def image_check(file):
    if file not in [".png", ".jpg", ".jpeg"]:
        return False
    return True

if __name__ == "__main__":
    main()
