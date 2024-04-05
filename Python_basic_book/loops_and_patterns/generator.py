def generate_numbers():
    for i in range(5):
        yield i

numbers = tuple(generate_numbers())
print(type(numbers))
for num in numbers:
    print(num)
