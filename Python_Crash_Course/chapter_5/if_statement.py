# car = 'subaru' 
# print("Is car == 'subaru'? I predict True.") 
# print(car == 'subaru') 
# print("\nIs car == 'audi'? I predict False.") 
# print(car == 'audi')


# Tests for equality and inequality with strings
def guest_varify():
    guest_list = ['amit','samna','usha','prashil']

    invited = False
    arrived_list = ''

    arrived_list =  input(f'What is your name: ')
    #C++ way
    # for guest in guest_list:
    #     if arrived_list == guest:
    #         invited = True
    #         break

    if arrived_list in guest_list:
        invited = True
        
    if invited:
            print(f"You are invited " + arrived_list)
    else:
            print(f"You are not invited "+ arrived_list)

    #  Tests using the lower() method

    caps_name = 'AMIT'

    if caps_name.lower() == arrived_list:
        print(f'Good')
    else:
        print(f'you are not capital guest as well')


#what if you have to pay age tax in this world

def age_tax_calc():
    tax = float(0)

    age = int(input('What is your age: '))

    if age <= 5:
        tax += 0
    elif age <= 12:
        tax += 5
    elif age <= 19:
        tax += 10
    elif age <= 55:
        tax = 50    #i did not forget to type + before = sign
    else:
        tax += 10

    print(f"ypur tax is " + str(tax)+ '$')
    print(f"your tax is {tax}$")


#username_checking
def check_username_repetition():
    current_user = ['amit','samna','usha','prashil']
    used = False
    new_user = ['sumit','sanjish','usha']

    current_user_lower = [user.lower() for user in current_user]

    for username in new_user:
        if username.lower() in current_user_lower:
            used = True
        if used:
            print(f'{username} username is already used')

check_username_repetition()