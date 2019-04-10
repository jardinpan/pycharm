set1 = {56, 4.0, 'string', True}
print(set1)
set1 = set([1, 2 ,3 ,4 ,5])
print(set1)
set1 = set((1, 2, 3, 3, 5))
print(set1)
set2 = {12, 87, 16 ,98 ,12, 7, 87, 98}
print(set2)

set1.add(10)
print(set1)
set1.remove(3)
print(set1)

set1 = {1, 2, 3, 5, 8}
set2 = {1, 3, 5, 7, 9}
print(set1.union(set2))
print(set1 | set2) #set1.union(set2)
print(set1.intersection(set2))
print(set1 & set2) #set1.intersection(set2)
print(set1.difference(set2))
print(set1 - set2) #set1.difference(set2)
print(set2.difference(set1))
print(set2 - set1) #set2.difference(set1)
print(set1.symmetric_difference(set2))
print(set1 ^ set2) #set1.symmetric_difference(set2)

set1 = {1, 2, 3, 5, 8}
set2 = {1, 3, 5}
print(set2.issubset(set1))
print(set1.issuperset(set2))

print(set1 == set2)
print(set1 != set2)