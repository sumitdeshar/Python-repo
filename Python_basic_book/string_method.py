str = 'yellow blue'
print(len(str)) #11

print(str.capitalize()) #Yellow blue
print(str.title()) #Yellow Blue
print(str.find('ow')) #4
print(str.count('l')) #3
print(str.startswith('ye')) #True
print(str.encode(encoding='utf32',errors='strict'))
# b'\xff\xfe\x00\x00y\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00w\x00\x00\x00 \x00\x00\x00b\x00\x00\x00l\x00\x00\x00u\x00\x00\x00e\x00\x00\x00'

str.isalnum() #Checks if all characters in the string are alphanumeric (letters or numbers).
#False
str.isalpha() #Checks if all characters in the string are alphabetic (letters).
#False
str.isdecimal() #Checks if all characters in the string are decimal characters (0-9).
#False
str.isdigit() #Checks if all characters in the string are digits.
 #False
str.isidentifier() #Checks if the string is a valid Python identifier.
#False
str.islower() #Checks if all characters in the string are lowercase letters.
#False
str.isnumeric() #Checks if all characters in the string are numeric characters.
#False
str.replace('h','p') #Replaces all occurrences of 'h' with 'p' in the string.
#'HARSH bpasin'

