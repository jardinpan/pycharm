dict1 = {'name':'Tom', 'age':25, 'mobile':'0934111222'}
print(type(dict1))
print(dict1)
print(dict1['name'])
print(dict1.get('name'))
for key in dict1:
    print('%s : %s' %(key, dict1[key]))

print()
print(dict1.keys())
print(dict1.values())
print(dict1.items(), end = "\n\n")

print(tuple(dict1.keys()))
print(tuple(dict1.values()))
print(tuple(dict1.items()), end = "\n\n")

print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()), end = "\n\n")

for key, value in dict1.items():
    print('%s : %s' %(key, value))

print()
print("name" in dict1)
print("Tom" in dict1)
dict2 = {'mobile':'0934111222', 'age':25, 'name':'Tom'}
print(dict1 == dict2, end = "\n\n")

dict1['email'] = 'tom@gmail.com'
print(dict1)
del dict1['email']
print(dict1)
print(dict1.pop('age'))
print(dict1)
print(dict1.popitem())
print(dict1)
dict1.clear()
print(dict1)
dict1 = {'name':'Tom', 'age':25, 'mobile':'0934111222'}
dict2 = dict1.copy()
print(dict2)
dict2["name"] = "Maaya"; dict2["age"] = 29; dict2["email"] = "MayaaMyWife@gmail.com"
print(dict2)
dict1.update(dict2)
print(dict1)


