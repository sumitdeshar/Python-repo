my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get a sublist containing elements from index 2 to index 5 (exclusive)
sublist = my_list[2:5]
print(sublist)  # Output: [3, 4, 5]

# Get a sublist containing every second element starting from index 1
sublist = my_list[1::2]
print(sublist)  # Output: [2, 4, 6, 8, 10]

# Get a sublist containing the last 3 elements
sublist = my_list[-3:]
print(sublist)  # Output: [8, 9, 10]

# In the examples above, 
# my_list[2:5] retrieves elements from index 2 to index 4 (index 5 is exclusive), 
# my_list[1::2] retrieves elements starting from index 1 with a step of 2, 
# and my_list[-3:] retrieves the last three elements of the list.