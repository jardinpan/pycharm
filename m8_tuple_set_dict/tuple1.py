list1 = [1, 2, 3, 4, 5]
tuple1 = tuple(list1)
print(tuple1)

tuple2 = tuple('python')
print(tuple2)

tuple1 = (67, 34, 27, 8, 87, 67, 92, 15, 55)
print(type(tuple1))
print(tuple1)
print('length =', len(tuple1))
print('max =', max(tuple1))
print('min =', min(tuple1))
print('sum =', sum(tuple1))
print('index(67) =', tuple1.index(67))
print('count(67) =', tuple1.count(67))
print(34 in tuple1)
print(34 not in tuple1)

tuple2 = (76, 38, 49)
print(tuple1 + tuple2)
print(tuple2 * 3)

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = ("Python", "C", "Java")

for i in range(len(tuple2)):
    print(i, tuple2[i])

for lang in tuple2:
    print(lang)

tuple2 +=(45,)
print(tuple2)
tuple2 +=(61, 58, 98)
print(tuple2)
