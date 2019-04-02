import random
list1 = [67, 34, 27, 8, 87]
for i in range(len(list1)):
    print('list1[%d] = %d' %(i, list1[i]))

list2 = ['Python', 'C', 'Java']
for num in list2:
    print(num)
else:
    print('no item left')

list3 = []
for i in range(6):
    list3.append(random.randint(1, 50))
print(list3)