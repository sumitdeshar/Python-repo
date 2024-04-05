str = 'yellow blue'
print(len(str)) #11

print(str.capitalize()) #Yellow blue
print(str.title()) #Yellow Blue
print(str.find('ow')) #4
print(str.count('l')) #3
print(str.startswith('ye')) #True
print(str.encode(encoding='utf32',errors='strict'))
# b'\xff\xfe\x00\x00y\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00w\x00\x00\x00 \x00\x00\x00b\x00\x00\x00l\x00\x00\x00u\x00\x00\x00e\x00\x00\x00'

#different example
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

#str.isdigit()
# Valid Examples
# print("12345".isdigit())  # True
# print("007".isdigit())    # True
# print("999".isdigit())    # True

# Invalid Examples
# print("12.34".isdigit())  # False (contains a decimal point)
# print("abc123".isdigit()) # False (contains alphabetic characters)
# print("123abc".isdigit()) # False (contains alphabetic characters)


# str.isidentifier() is a method in Python that checks whether a given string is a valid Python identifier. A Python identifier is a name used to identify a variable, function, class, module, or other objects in Python programming.

# Here are some key rules for a valid Python identifier:
# It must start with a letter (a-z, A-Z) or an underscore (_).
# The remaining characters can be letters, underscores, or digits (0-9).
# It cannot contain any special characters such as spaces, punctuation marks, or symbols


#str.isnumeric()
# # Valid Examples
# print("12345".isnumeric())  # True
# print("007".isnumeric())    # True
# print("999".isnumeric())    # True
# print("½".isnumeric())      # True (Unicode fraction)

# # Invalid Examples
# print("12.34".isnumeric())  # False (contains a decimal point)
# print("abc123".isnumeric()) # False (contains alphabetic characters)
# print("123abc".isnumeric()) # False (contains alphabetic characters)

