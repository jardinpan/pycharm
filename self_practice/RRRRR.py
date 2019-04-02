def msg(name, age):
    print('{0} is {1} years old!'.format(name, age))

msg('Tom',30)
msg(name = 'Tom', age = 30)
msg(age = 30, name = 'Tom')
msg('Tom', age = 30)
#  msg(name = 'Tom', 30) 關鍵字引數不可至於位置引數的前面

#---
x = 10
y = 11

def main():
    x = 20
    print(x)
    print(y)
main()
print(x)
print(y)

#---
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
    inner()
    print(x)
outer()
print(x)

#---
def func(n):
    print("level", n)
    if n < 4:
        func(n + 1)
    print("LEVEL", n)
def main():
    func(1)

main()

#---
list1 = []
list2 = [56, 4.0, 'string', True]
list3 = [1, 2, 3, 4, 5, 6]
list4 = ['Python', 'C', 'Java']
print(list4[0])
print(list4[2])

#---
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

#---
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

#---
list1 = [67, 34, 27, 8, 87 ,67, 92, 15, 55]
print(list1[2:6])
print(list1[2:])
print(list1[-3:])
print(list1[:-3])
print(list1[:5])
print(list1[:])

#---
import random
list1 = [67, 34, 27, 8, 87]
for i in range(len(list1)):
    print('list1[%d] = %d' %(i, list1[i]))

list2 = ['Python', 'C', 'Java']
for s in list2:
    print(s)
else:
    print('no item left')

list3 = []
for i in range(6):
    list3.append(random.randint(1, 50))
print(list3)

#---
str1 = 'Python C Java'
list1 = str1.split()
print(list1)

str1 = 'Python, C, Java'
list1 = str1.split(', ')
print(list1)

#---
list1 = [[67, 34, 27], [92, 15, 55]]
print(list1)
print('row =', len(list1))
print('col =', len(list1[0]))
print(list1[0][1])
print(list1[1][2])

for i in range(len(list1)):
    print(list1[i])

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print('%-3d' %(list1[i][j]), end = ' ')
    print()

#---
import random
row = eval(input('Enter the number of row: '))
col = eval(input('Enter the number of column: '))
list2 = []
for i in range(row):
    list2.append([])
    for j in range(col):
        list2[i].append(random.randint(1, 50))
print(list2)

list3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(list3[0])
print(list3[0][1])
print(list3[0][1][0])
print(len(list3))
print(len(list3[0]))
print(len(list3[0][0]))

#---
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

#---
tuple1 = (1, 2, 3, 4, 5)
tuple1 += (6,)
tuple1 += (7, 8)
#del tuple1
print(tuple1)

#---
set1 = {56, 4.0, 'string', True}
print(set1)
set1 = set([1, 2 ,3 ,4 ,5])
print(set1)
set1 = set((1, 2, 3, 3, 5))
print(set1)

set1.add(10)
print(set1)
set1.remove(3)
print(set1)

set1 = {1, 2, 3, 5, 8}
set2 = {1, 3, 5, 7, 9}
print(set1 | set2) #set1.union(set2)
print(set1 & set2) #set1.intersection(set2)
print(set1 - set2) #set1.difference(set2)
print(set1 ^ set2) #set1.symmetric_difference(set2)

set1 = {1, 2, 3, 5, 8}
set2 = {1, 3, 5}
print(set2.issubset(set1))
print(set1.issuperset(set2))

print(set1 == set2)
print(set1 != set2)

#---
dict1 = {'name':'Tom', 'age':25, 'mobile':'0934111222'}
print(dict1)
print(dict1['name'])
print(dict1.get('name'))
for key in dict1:
    print('%s : %s' %(key, dict1[key]))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

print(tuple(dict1.keys()))
print(tuple(dict1.values()))
print(tuple(dict1.items()))

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
dict2 = dict1.copy()
print(dict2)
dict1.update(dict2)
print(dict1)

#---



