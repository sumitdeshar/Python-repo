
# alien = {'color': 'green', 'points': 5} 
# print(alien['color']) 
# print(alien['points'])

# new_points = alien['points'] 
# print(f"You just earned {new_points} points!")

# alien['x_postion'] = 0
# alien['y_postion'] = 25
# print(alien)
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 
# 'medium'} 
# print(alien_0)

#  del alien['points']  it deletes key not only the value



#When we try to print a key that is not available it return a key error so use get and provide a catch statement for error

# point_value = alien.get('points', 'No point value assigned.') 
# print(point_value)

# If you leave out the second argument in the call to get() and the key
#  doesn’t exist, Python will return the value None. The special value
#  None means “no value exists.” This is not an error: it’s a special
#  value meant to indicate the absence of a value.
 

# def alien():
# alien()

alien_0 = {'color': 'green', 'points': 5}
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 
# 'medium'} 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'slow'

print(f'{alien_0}')

if alien_0['speed'].lower() == 'slow':
    x_increment = 1
elif alien_0['speed'].lower() == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment


print(f'{alien_0["x_position"]}')

