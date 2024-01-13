#ask the name of the file
question = input("File name: ")
new_question = question.lower()

#check if the name ends with the file types
if ".gif" in new_question:
    print("image/gif")

elif ".jpg" in new_question:
    print("image/jpeg")

elif ".jpeg" in new_question:
    print("image/jpeg")

elif ".png" in new_question:
    print("image/png")

elif ".pdf" in new_question:
    print("application/pdf")

elif ".zip" in new_question:
    print("application/zip")

elif ".txt" in new_question:
    print("text/plain")

#else print application/octet-stream
else:
    print("application/octet-stream")