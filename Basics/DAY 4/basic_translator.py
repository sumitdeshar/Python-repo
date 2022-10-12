#Giraffe Language
#vowels -> g
#eg
#dog -> dgg
'''
asdad
'''
'''
das
sadsad
sa
dsadsadassadas
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":  # it is done to get rid for writing long foramt of "AEIOUaeuio"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("give phrase :")))