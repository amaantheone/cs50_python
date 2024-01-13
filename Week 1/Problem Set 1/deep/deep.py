#Ask the question
question = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

#Print yes if the answer is 42
if question.strip() == "42":
    print("Yes")
elif question.lower().strip() == "forty-two":
    print("Yes")
elif question.lower().strip() == "forty two":
    print("Yes")

#else print No
else:
    print("No")