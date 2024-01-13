import emoji

e = input("Input: ")
em = emoji.emojize(e, language='alias')
print("Output:", em)