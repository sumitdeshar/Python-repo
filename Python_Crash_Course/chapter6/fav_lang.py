#looping thorugh dictionary
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }


# for name, language in favorite_languages.items(): 
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys(): 
#     print(name.title()) #title funtion is used to capitalize the front letter of the word

# for language in favorite_languages.values(): 
#     print(language.title())

# for name in sorted(favorite_languages.keys()): 
#     print(f"{name.title()}, thank you for taking the poll.")

# for language in set(favorite_languages.values()): #when wrapped with set it excludes any repetition in values of dictionary
#     print(language.title())


favorite_languages = { 
'jen': ['python', 'rust'], 
'sarah': ['c','c++'], 
    'edward': ['rust', 'go'], 
    'phil': ['python', 'haskell'], 
    } 

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite language are:")
    for language in languages:
        print(f"\n{language.title()}")
        
# Jen's favourite language are:

# Python

# Rust

# Sarah's favourite language are:

# C

# C++

# Edward's favourite language are:

# Rust

# Go

# Phil's favourite language are:

# Python