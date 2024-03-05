
# einstein = { 
#         'first': 'albert', 
#         'last': 'einstein', 
#         'location': 'princeton', 
#         'achivement': 'E=mc^2' 
#         }
# curie = { 
#         'first': 'marie', 
#         'last': 'curie', 
#         'location': 'paris', 
#         'achivement': 'discovery of radium' 
#         }
# sumit = { 
#         'first': 'sumit', 
#         'last': 'deshar', 
#         'location': 'chapagaon', 
#         'achivement': 'discovery of how bad i am at python so start to learn again' 
#         }

# nominee_list = [einstein,curie,sumit]

# fav_list = ['paris', 'singapore', 'toronto']

# print(f'\n Here we are going to give award for the people with life changing achivement')
# print(f"\nPlease Join")
# print(f"\n List of nominee are")

# for i, info in enumerate(nominee_list):
#     print(f'\n ')
#     for key, value in info.items():
#         # info['favorite'] = f'{fav_list(i)}'
#         print(f"{key.capitalize()}: {value}")
        
# I faild it was gpt
einstein = { 
    'first': 'albert', 
    'last': 'einstein', 
    'location': 'princeton', 
    'achievement': 'E=mc^2' 
}
curie = { 
    'first': 'marie', 
    'last': 'curie', 
    'location': 'paris', 
    'achievement': 'discovery of radium' 
}
sumit = { 
    'first': 'sumit', 
    'last': 'deshar', 
    'location': 'chapagaon', 
    'achievement': 'discovery of how bad I am at python so start to learn again' 
}

nominee_list = [einstein, curie, sumit]

# List of favorite places
fav_list = [['berlin', 'vienna'], ['paris', 'vienna'], ['chapagaon', 'kathmandu']]

# Adding favorite places as lists to the corresponding nominee
for i, nominee in enumerate(nominee_list):
    nominee_name = nominee['first'].lower()
    
    nominee['favorite_places'] = fav_list[i]

# Print the updated nominee_list
print("Updated List of Nominees:")
for nominee in nominee_list:
    print("\nNominee Information:")
    for key, value in nominee.items():
        if isinstance(value, list):
            print(f"{key.capitalize()}: {', '.join(value)}")
        else:
            print(f"{key.capitalize()}: {value}")
