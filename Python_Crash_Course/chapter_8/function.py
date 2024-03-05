# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# #  Preventing a Function from Modifying a List
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

# # *args,**kwargs concept called arbitary arguments
# def make_pizza(*toppings): 
#     """Print the list of toppings that have been 
# requested.""" 
#     print(toppings) 
# make_pizza('pepperoni') 
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Some examples
# Summing Numbers:
# Suppose you want a function that can take any number of arguments and return their sum.

def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15


# Concatenating Strings:
# A function that concatenates an arbitrary number of strings.

def concatenate_strings(*args):
    return ' '.join(args)

result = concatenate_strings('Hello', 'World', 'Python')
print(result)  # Output: Hello World Python



# Arbitrary Keyword Arguments (**kwargs):
# Building a Profile:
# A function to build a user profile with arbitrary user information.

def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

user_profile = build_profile('Alice', 'Wonder', age=25, city='Wonderland', hobby='Reading')
print(user_profile)

# Styling HTML Elements:
# A function that generates an HTML element with arbitrary attributes.

def create_html_element(tag, content, **attributes):
    attribute_str = ' '.join([f'{key}="{value}"' for key, value in attributes.items()])
    return f'<{tag} {attribute_str}>{content}</{tag}>'

html_button = create_html_element('button', 'Click me', class_='btn', id='btn1')
print(html_button)
