Pg = 262

#  9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a
#  class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise
#  9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will work; just
#  pick the one you like better. Add an attribute called flavors that stores a list of ice
#  cream flavors. Write a method that displays these flavors. Create an instance of
#  IceCreamStand, and call this method.

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open!")
        



# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type,*ice_cream):
#         super().__init__(restaurant_name, cuisine_type)
#         self.ice_cream_type =  ice_cream
        
#     def display_icecream(self):
#         print(f'Resturant Name:\t{self.restaurant_name}\nCusine Type: \t{self.cuisine_type}\n')
#         print(f'Icream list:')
#         for icecream in self.ice_cream_type:
#             print(f'\t{icecream}')
    
# ice_cream_list = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookie Dough", "Cookies and Cream", "Rocky Road", "Butter Pecan", "Salted Caramel", "Coffee"]

# iceme = IceCreamStand('Maila dai ko chatti', 'Newari',"Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookie Dough", "Cookies and Cream", "Rocky Road", "Butter Pecan", "Salted Caramel", "Coffee")

# iceme.display_icecream()
        



#  9-7. Admin: An administrator is a special kind of user. Write a class called Admin that
#  inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page
#  167). Add an attribute, privileges, that stores a list of strings like "can add post", "can
#  delete post", "can ban user", and so on. Write a method called show_privileges() that
#  lists the administrator’s set of privileges. Create an instance of Admin, and call your
#  method.
import sys
sys.path.append('F:\LearnToCode\Python-repo\Python_Crash_Course\chapter_9')
from classes import User

class Admin(User):
    def __init__(self,isAdmin,first_name,last_name,username,password,bio,*priviliege):
        self.IsAdmin = isAdmin
        super().__init__(first_name,last_name,username,password,bio)
        self.priviliege = priviliege
        
    def make_admin(self):
        print(f'{self.username} is admin')
        
    def show_priviliege(self):
        print(f'{self.priviliege} can {self.priviliege}')


superuser = Admin('ram','pandey','ramayan','sitaharan','I can do so I will do it','cpost','kick user','delete post','ban user', 'mute user')





#  9-8. Privileges: Write a separate Privileges class. The class should have one
#  attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the
#  show_privileges() method to this class. Make a Privileges instance as an attribute in
#  the Admin class. Create a new instance of Admin and use your method to show its
#  privileges.
#  9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a
#  method to the Battery class called upgrade_battery(). This method should check the
#  battery size and set the capacity to 65 if it isn’t already. Make an electric car with a
#  default battery size, call get_range() once, and then call get_range() a second time
#  after upgrading the battery. You should see an increase in the car’s range.



