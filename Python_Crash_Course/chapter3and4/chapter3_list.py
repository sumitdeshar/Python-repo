import random

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
message = f"My first bicycle was a {bicycles[0].title()}." 
print(message)

del bicycles[0] 
print(bicycles)

#try it yourself
friends = ['amit', 'prashil', 'saman', 'usha']
print(friends)

cannot_come_to_dinner = 'amit'
friends.remove('amit')
new_friends = friends
print(new_friends)

new_friends_who_joins = ['narendra', 'sichu', 'rojit', 'usha']
for newmate in new_friends_who_joins:
    new_friends.append(newmate) #new_friends.insert(3,newmate)
    print(new_friends)
    
for friend in new_friends:
    index = random.randint(0, len(new_friends)-1)
    new_friends.pop(index)
    print(new_friends)
    print(len(new_friends))
    if len(new_friends)<=2: # 
        print(len(new_friends))
        break
print('exited')
while len(new_friends) != 0:
    del new_friends[0]

print(new_friends)
    