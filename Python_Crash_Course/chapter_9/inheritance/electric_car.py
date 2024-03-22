# class Car: 
#     """A simple attempt to represent a car.""" 
    
#     def __init__(self, make, model, year): 
#         """Initialize attributes to describe a car.""" 
#         self.make = make 
#         self.model = model 
#         self.year = year 
#         self.odometer_reading = 0 
        
#     def get_descriptive_name(self): 
#         """Return a neatly formatted descriptive name.""" 
#         long_name = f"{self.year} {self.make} {self.model}" 
#         return long_name.title() 
    
#     def read_odometer(self): 
#         """Print a statement showing the car's mileage.""" 
#         print(f"This car has {self.odometer_reading} miles on it.") 

#     def update_odometer(self, mileage): 
#         # """Set the odometer reading to the given value.""" 
#         # self.odometer_reading = mileage
#         self.odometer_reading = 0 
        
#         """ 
#         Set the odometer reading to the given value. 
#         Reject the change if it attempts to roll the odometer back. 
#         """ 
#         if mileage >= self.odometer_reading: 
#             self.odometer_reading = mileage 
#         else: 
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles): 
#         """Add the given amount to the odometer reading.""" 
#         self.odometer_reading += miles
#     def fill_gas_tank(self): 
#         print("The gas tank is filled")

import sys
sys.path.append('F:\LearnToCode\Python-repo\Python_Crash_Course\chapter_9')
from car import Car

class ElectricCar(Car): 
    """Represent aspects of a car, specific to electric 
vehicles.""" 
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.""" 
        super().__init__(make, model, year) 
        self.battery_size = 40 
        
    def describe_battery(self): 
        print(f"This car has a {self.battery_size}-kWh battery.") 
        
    def fill_gas_tank(self): 
        """Electric cars don't have gas tanks.""" 
        print("This car doesn't have a gas tank!")
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name()) #2024 Nissan Leaf
# my_leaf.describe_battery() #This car has a 40-kWh battery.
my_leaf.fill_gas_tank()

# after the change (adding battery class as an attribute in electric)
#Instances as Attributes

# class Battery: 
#     """A simple attempt to model a battery for an electric 
# car.""" 
#     def __init__(self, battery_size=40): 
#         """Initialize the battery's attributes.""" 
#         self.battery_size = battery_size 
#     def describe_battery(self): 
#         """Print a statement describing the battery size.""" 
#         print(f"This car has a {self.battery_size}-kWh 
# battery.") 
        
        
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric 
# vehicles.""" 
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric 
# car.
#  ❸
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery() 
        
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name()) 
# my_leaf.battery.describe_battery()




