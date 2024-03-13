class Car: 
    """A simple attempt to represent a car.""" 
    
    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
        
        
    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name.""" 
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title() 
    
    def read_odometer(self): 
        """Print a statement showing the car's mileage.""" 
        print(f"This car has {self.odometer_reading} miles on it.") 

    def update_odometer(self, mileage): 
        # """Set the odometer reading to the given value.""" 
        # self.odometer_reading = mileage
        self.odometer_reading = 0 
        
        """ 
        Set the odometer reading to the given value. 
        Reject the change if it attempts to roll the odometer back. 
        """ 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles): 
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles 
        
    
        
   

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name()) 
# my_new_car.read_odometer()
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# my_new_car.update_odometer(-33)
# my_new_car.read_odometer()


# output
#  2024 Audi A4 
# This car has 0 miles on it.
#updated
#  2024 Audi A4 
# This car has 23 miles on it.
#final cut
# 2024 Audi A4
# This car has 0 miles on it.
# This car has 23 miles on it.
# You can't roll back an odometer!
# This car has 0 miles on it.


my_used_car = Car('subaru', 'outback', 2019) 
print(my_used_car.get_descriptive_name()) 
my_used_car.update_odometer(23_500) 
my_used_car.read_odometer() 

#output
# 2019 Subaru Outback
# This car has 23500 miles on it.