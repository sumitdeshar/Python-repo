# # page = 176

# aliens= []

# for alien_number in range(30):
#     new_alien = {'color': 'green','points': 5,'speed':'slow'}
#     aliens.append(new_alien)
    
# # for i,alien in enumerate(aliens[:-5]):
# #     print(i)
# #     print(alien)
# # print(aliens)
    
# for alien in aliens[:3]: 
#     if alien['color'] == 'green': 
#         alien['color'] = 'yellow' 
#         alien['speed'] = 'medium' 
#         alien['points'] = 10 

# for alien in aliens[:5]:
#     print(alien)

print('...')

# print(f"Total number of aliens: {len(aliens)}")
# Store information about a pizza being ordered. 
pizza = { 
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'], 
    } 
# Summarize the order. 
print(f"You ordered a {pizza['crust']}-crust pizza " 
    "with the following toppings:") 
for topping in pizza['toppings']: 
    print(f"\t{topping}")
    

#Dictionary into dictionary 
users = { 
    'aeinstein': { 
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton', 
        }, 
    'mcurie': { 
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
        }, 
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    
    location = user_info['location']
    
    print(f'\nFull name: {full_name.title()}')
    print(f'\nFull name: {location.title()}')
    print(f'\n')