def main():
    func = convert(input())
    print (func)

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()