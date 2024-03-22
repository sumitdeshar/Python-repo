# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def sit(self):
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
        
        
# my_dog = Dog('Willie', 6) 
# your_dog = Dog('Lucy', 3) 

# print(f"My dog's name is {my_dog.name}.") 
# print(f"My dog is {my_dog.age} years old.") 
# my_dog.sit() 

# print(f"\nYour dog's name is {your_dog.name}.") 
# print(f"Your dog is {your_dog.age} years old.") 
# your_dog.roll_over()

# output
# My dog's name is Willie.
# My dog is 6 years old.
# Willie is now sitting.

# Your dog's name is Lucy.
# Your dog is 3 years old.
# Lucy rolled over!

#Python Standard library
# from random import randint 
# randint(1, 6) 
# # 3
# #  Another useful function is choice(). This function takes in a list or tuple
# #  and returns a randomly chosen element:

# from random import choice 
# players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# first_up = choice(players) 
# first_up 
# 'florence'


#  9-3. Users: Make a class called User. Create two attributes called first_name and
#  last_name, and then create several other attributes that are typically stored in a user
#  profile. Make a method called describe_user() that prints a summary of the user’s
#  information. Make another method called greet_user() that prints a personalized
#  greeting to the user.
#  Create several instances representing different users, and call both methods for each
#  user.

class User:
    
    def __init__(self,first_name,last_name,username,password,bio):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.bio = bio
    
    def show_info(self):
        print(f"{self.first_name} {self.last_name} \n   your  username is: {self.username}\n\tpassword is: {self.password}")
        
    def  greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")
        
ram = User('ram','pandey','ramayan','lanka@ka$dhanka', 'Sita is my love.')
ram.show_info()
print(ram.bio)
ram.greet_user()

# output
# ram pandey 
#    your  username is: ramayan
#         password is: lanka@ka$dhanka
# Sita is my love.


#  9-5. Login Attempts: Add an attribute called login_attempts to your User class from
#  Exercise 9-3 (page 162). Write a method called increment_login_attempts() that
#  increments the value of login_attempts by 1. Write another method called
#  reset_login_attempts() that resets the value of login_attempts to 0.
#  Make an instance of the User class and call increment_login_attempts() several
#  times. Print the value of login_attempts to make sure it was incremented properly, and
#  then call reset_login_attempts(). Print login_attempts again to make sure it was reset
#  to 0.

# class User:
#     def __init__(self,login_attempts):
#         self.login_attempts = login_attempts
        
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         return self.login_attempts
    
#     def reset_login_attempts(self): 
#         self.login_attempts = 0
#         return self.login_attempts
    
    
# myuser = User(1)
# myuser.increment_login_attempts()
# myuser.increment_login_attempts()
# myuser.increment_login_attempts()
# myuser.increment_login_attempts()
# myuser.increment_login_attempts()
# myuser.increment_login_attempts()
# print(f'login attempts are: {myuser.login_attempts}')
# myuser.reset_login_attempts()
# print(f'login attempts are: {myuser.login_attempts}')

# login attempts are: 7
# login attempts are: 0

