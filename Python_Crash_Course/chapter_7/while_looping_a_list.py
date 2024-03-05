# #  Moving Items from One List to Another
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f'Verifing User: {current_user.title()}')
#     confirmed_users.append(current_user)
    
# print('\nThe following users hve been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
    
    
# Removing All Instances of Specific Values from a List
# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# while 'cat' in pets:
#     pets.remove('cat')
    
# print(pets)

# #  Filling a Dictionary with User Input
# responses = {}
# polling_active = True

# while polling_active:
#     name = input('\nWhat is your name: ')
#     response = input('Which mountain would you like to climb someday? ')
#     responses[name] = response
    
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
        
# for name, response in responses.items():
#     print(f'{name}:{response}\n')
# print('\n---------Poll Result---------')
# for name, response in responses.items():
#     print(f'{name} would like to climb {response}')
    

