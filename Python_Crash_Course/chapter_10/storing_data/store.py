from pathlib import Path
import json

# numbers = [2, 3, 5, 7, 11, 13] 

# path = Path(r'chapter_10\storing_data\numbers.json')
# contents = json.dumps(numbers)
# print(contents)
# # [2, 3, 5, 7, 11, 13]

# path.write_text(contents)
# print(path)
# # chapter_10\storing_data\numbers.json

# contents = path.read_text() 
# numbers = json.loads(contents) 
# print(numbers)
# # [2, 3, 5, 7, 11, 13]

#Refactoring: Breaking down a part of coe into a function that have specfic job.
# def greet_user(): 
#     path = Path(r'chapter_10\storing_data\username.json') 
#     if path.exists(): 
#         contents = path.read_text() 
#         username = json.loads(contents) 
#         print(f"Welcome back, {username}!") 
#     else: 
#         username = input("What is your name? \n") 
#         contents = json.dumps(username) 
#         path.write_text(contents) 
#         print(f"We'll remember you when you come back, {username}!")
        
# greet_user()

#finally making it more like a real world process

from pathlib import Path
import json

def get_stored_name(path):
    if path.exists(): 
        contents = path.read_text() 
        username = json.loads(contents) 
    else:
        return None
    
def greet_user():
    path = Path(r'chapter_10\storing_data\username.json') 
    username = get_stored_name(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? \n") 
        contents = json.dumps(username) 
        path.write_text(contents) 
        print(f"We'll remember you when you come back, {username}!")      


# greet_user()
#Welcome back, sumit!
# What is your name?
# sumit
# We'll remember you when you come back, sumit!

#10-13.User Dictionary:
#  The remember_me.py example only stores one piece of
#  information, the username. Expand this example by asking for two more pieces of
#  information about the user, then store all the information you collect in a dictionary.
#  Write this dictionary to a file using json.dumps(), and read it back in using json.loads().
#  Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json

def get_stored_name(path):
    if path.exists(): 
        contents = path.read_text() 
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None
    
def greet_user():
    path = Path(r'chapter_10\storing_data\username.json') 
    userinfo = get_stored_name(path)
    if userinfo:
        print(f"{userinfo}")
        print(f"We'll remember you when you come back, {userinfo['username']}!")   
    else:
        username = input("What is your name? \n")
        address = input("What is your address? \n")
        password = input("What is your password? \n")
        contact =  input("What is your password? \n")
        data = {
            'username': username,
            'address': address,
            'contact': contact,
            'password': password,
        }
        contents = json.dumps(data) 
        path.write_text(contents) 
        print(f"We'll remember you when you come back, {data['username']}!")      
        
greet_user()



