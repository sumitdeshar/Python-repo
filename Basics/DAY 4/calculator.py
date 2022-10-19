num1 = float(input("Give a number: \n"))
num2 = float(input("Give a number: \n"))
op = input("\'Give an operator :\'\n")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("You dont have that feature yet :")
print("The End")