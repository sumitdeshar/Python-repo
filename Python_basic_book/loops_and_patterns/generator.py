def generate_numbers():
    for i in range(5):
        yield i
#to generalize take yield as return but instead of halting a funciton it return the value in list a special data type can be store in any data type like list set tuple etc.

numbers = tuple(generate_numbers())
print(type(numbers))
for num in numbers:
    print(num)
