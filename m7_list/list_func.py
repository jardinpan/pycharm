list1 = [67, 34, 27, 8, 87 ,67, 92, 15, 55]
print(type(list1))
print(list1)
print('length =', len(list1))
print('max =', max(list1))
print('min =', min(list1))
print('sum =', sum(list1))
print(34 in list1)
print(34 not in list1)

list2 = [76, 38, 49]
print(list1 + list2)
print(list2 * 2)

list1.append(66)
print(list1)
list1.insert(1, 22)
print(list1)
print(list1.pop())
print(list1)
print(list1.pop(1))
print(list1)
list1.remove(67)
print(list1)

list1 = [67, 34, 27, 8, 87 ,67, 92, 15, 55]
print('index(67) =', list1.index(67))
print('count(67) =', list1.count(67))
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)