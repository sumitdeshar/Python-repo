TIY = 'Try It Yourself'

# pg = 233 

#  8-12. Sandwiches: Write a function that accepts a list of items a person wants on a
#  sandwich. The function should have one parameter that collects as many items as the
#  function call provides, and it should print a summary of the sandwich that’s being
#  ordered. Call the function three times, using a different number of arguments each
#  time.

def toppings_choice(*toppings):
    # toppings_list = toppings dont need to do it, the varible look thing is list
    print(f'The topping that you decide are:')
    for topping in toppings:
        print(f'{topping}')
        
toppings_choice('peperoni','cheese','more cheese','no veggies')
# output
# The topping that you decide are:
# peperoni
# cheese
# more cheese
# no veggies


#  8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a profile of
#  yourself by calling build_profile(), using your first and last names and three other
#  key-value pairs that describe you.

def build_profile(first, last, *lang, **user_info): 
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    user_info['language'] = lang
    return user_info 
user_profile = build_profile('sumit', 'instance', 'python', 'C++', 'javascript',
                             location='chapagaon', 
                             field='engineer') 

print(user_profile) #{'location': 'chapagaon', 'field': 'engineer', 'first_name': 'sumit', 'last_name': 'instance', 'language': ('python', 'C++', 'javascript')}


#  8-14. Cars: Write a function that stores information about a car in a dictionary. The
#  function should always receive a manufacturer and a model name. It should then
#  accept an arbitrary number of keyword arguments. Call the function with the required
#  information and two other name-value pairs, such as a color or an optional feature.
#  Your function should work for a call like this one:
#  car = make_car('subaru', 'outback', color='blue', tow_package=True)
#  Print the dictionary that’s returned to make sure all the information was stored
#  correctly.

def make_car(manufacture, model_name, *price, **car_info):
    car_info['manufacture'] = manufacture
    car_info['model_name'] = model_name
    car_info['price'] = price
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car) #{'color': 'blue', 'tow_package': True, 'manufacture': 'subaru', 'model_name': 'outback', 'price': ()}