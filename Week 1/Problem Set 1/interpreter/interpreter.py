#get input from user
expression = input("Expression: ")

#Change to x and y
x, y, z = expression.split(" ")

#Change x and z to float
new_x = float(x)
new_z = float(z)

#Get the answer
if y == "+":
    answer = new_x + new_z
elif y == "-":
    answer = new_x - new_z
elif y == "/":
    answer = new_x / new_z
elif y == "*":
    answer = new_x * new_z

print(round(answer, 1))