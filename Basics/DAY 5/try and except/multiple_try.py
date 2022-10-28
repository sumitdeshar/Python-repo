
try:
    number = int(input("Enter a number:"))
    value = 10 / number
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")