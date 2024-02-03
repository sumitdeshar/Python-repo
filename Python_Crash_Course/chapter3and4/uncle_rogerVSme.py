#recipe storage app
def show_recipe():
    for contestant in contestants[:2]:
        print(f'List of {contestant}')
        if contestant == 'sumit':
            
            for recip in my_recipe:
                print(f'{recip}')
            print('\t')
        else:
            
            for recip in chef_recipe:
                print(f'{recip}')

def add_recipe(const_index):
    print('Add recipe:')
    add_on = input('Enter recipe to add: ')
    if const_index == 0:
        my_recipe.append(add_on)
    if const_index == 1:
        chef_recipe.append(add_on)

def case1():
    add_recipe(0)

def case2():
    add_recipe(1)

def switch_case(case_value):
    switch_dict = {
        1: case1,
        2: case2,
    }
    selected_case = switch_dict.get(case_value)
    
    return selected_case()

print('Recipe of Fried Rice')

contestants = ['sumit', 'uncle_roger', ['rice', 'egg', 'green onions']]
my_recipe = ['rice', 'egg', 'green onions']
chef_recipe = ['rice', 'egg', 'green onions']

# show_recipe()

while True:
    print('\nOptions:')
    print('1. Show Recipe')
    print('2. Add Recipe')
    print('3. Exit')

    choice = input('Enter your choice (1, 2, 3): \t')

    if choice == '1':
        show_recipe()
    elif choice == '2':
        inner_choice = int(input('Choose where to add recipe (1. Sumit, 2. Uncle Roger): \t'))
        switch_case(inner_choice)
    elif choice == '3':
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a valid option.')