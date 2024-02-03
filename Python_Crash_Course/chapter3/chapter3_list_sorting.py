cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

square = []
# remember that for list in python (0,5) is normal statements as index starts from 0 for list or other data types
# hence 1 to 6 here means 6-1=5 it stops at 5 
for value in range(1,6): 
    print(value)
    square.append(value ** 2)

print(square)#[1, 4, 9, 16, 25]
#alternative solution known as List Comprehensions
squares = [value**2 for value in range(1, 11)] 
print(squares)

# try it youself
number_list = [value for value in range(1,100_001)]

minimum = min(number_list)
maximum = max(number_list)

print(f"The minimum value in the list is: {minimum}")
print(f"The maximum value in the list is: {maximum}")

sum_of_numbers = sum(number_list)
print(f"The sum of the million numbers is: {sum_of_numbers}")

odd_number_list = []

odd_number_list= list(range(1, 20, 2)) # third arugument is used assert interval in the otherwise it would go with interval 1

print(odd_number_list)

#3's multiplication table
multiplication_table_list = []

multiplication_table_list = list(range(3,31,3))

for i,value in enumerate(multiplication_table_list):
    print(f"3*{i+1}={value}")
    
#print list of cube
cube_list = []

cube_list = [value**3 for value in range(1,11)]

for i,value in enumerate(cube_list):
    print(f"{i+1}^3 = {value}")