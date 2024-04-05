def print_pattern(n):
    pattern= ''
    for i in range(1,n+1):
        pattern= ''
        # print(f'{i}')
        for j in range(i):
            pattern += '*'
        print(f'{pattern}')
    return pattern
# print_pattern(5)

# *
# **
# ***
# ****
# *****

def print_pattern_number(n):

    for i in range(1,n+1):
        for j in range(i):
            print(f'{i}', end= ' ')
        print()
    return 0
# print_pattern_number(5)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def print_pattern_ascending_number(n):

    for i in range(1,n+1):
        for j in range(i):
            print(f'{j+1}', end= ' ')
        print()
    return 0
# print_pattern_ascending_number(5)
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def print_pattern_increasing_forever(n):
    number = 0
    for i in range(1,n+1):
        for j in range(i):
            number += 1
            print(f'{number}', end= ' ')
        print()
    return 0
# print_pattern_increasing_forever(5)
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def print_triangular_pattern(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(' ', end='')
        for j in range(0,2*i+1):
            print('*', end='')
        print()
    
print_triangular_pattern(5)
#     *
#    ***
#   *****
#  *******
# *********

