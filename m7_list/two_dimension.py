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
