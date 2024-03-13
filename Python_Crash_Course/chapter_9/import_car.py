from car import Car 
my_new_car = Car('audi', 'a4', 2024) 
print(my_new_car.get_descriptive_name()) 
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

# output
# 2019 Subaru Outback
# This car has 23500 miles on it.
# 2024 Audi A4
# This car has 23 miles on it.


from car import Car 
from inheritance.electric_car import ElectricCar as EC

my_mustang = Car('ford', 'mustang', 2024) 
print(my_mustang.get_descriptive_name()) 
my_leaf = EC('nissan', 'leaf', 2024) 
print(my_leaf.get_descriptive_name())

# output
# 2019 Subaru Outback
# This car has 23500 miles on it.
# 2024 Audi A4
# This car has 23 miles on it.
# This car doesn't have a gas tank!
# 2024 Ford Mustang
# 2024 Nissan Leaf