lucky_num = [2,4,8,16,32]
friends = ["Amit","Usha","Prashil","Saman","MEE","MEE"]

friends.append("lool")
friends.insert(1, "sus")
friends.remove("Prashil")
friends.pop()
print(friends.index("MEE"))
print(friends.count("MEE"))
friends.sort()
friends.extend(lucky_num)
print(friends)
friends2 = friends.copy()
print(friends2)
friends.clear()
print(friends)
