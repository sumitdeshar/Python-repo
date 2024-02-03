#Strings

first_name = "ada"
last_name = "lovelace"
previous_method = first_name + " "+ last_name # less efficient
full_name = f"{first_name} {last_name}" #f-string
message = f"Hello, {full_name.title()}!"
print(message)
print(previous_method)

print("Languages:\n\tPython\n\tC\n\tJavaScript\n\t\'C++\'") 

product = "Laptop"
price = 1200.50
quantity = 2

total_cost = f"The total cost of purchasing {quantity} {product}s is ${price * quantity:.2f}."
print(total_cost)
print("//")
#dollar is string and dono tbe confused by it as part of syntax
total_cost = f"The total cost of purchasing {quantity} {product}s is {price * quantity:.2f}."
print(total_cost)

#assignment
name = "     sumit deshar     "
print(name.lstrip())
print(name.rstrip())
print(name.strip())


filename = 'python_notes.txt'
filename_without_extension = filename.removesuffix('.txt')
print(filename_without_extension)

text = "Hello, World!"
text_without_prefix = text.removeprefix("Hello, ")
print(text_without_prefix)
