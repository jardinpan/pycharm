import numpy as np

list1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
list2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(list1)
print(list1[1])
print(list1[2][1])
print(list1[0][1][1], end='\n\n')
print(len(list1))
print(len(list1[0]))
print(len(list1[0][0]), end='\n\n')

print(list1[0][0][0], end=' ')
print(list1[0][0][1], end=' ')
print(list1[0][1][0], end=' ')
print(list1[0][1][1], end=' ')
print(list1[1][0][0], end=' ')
print(list1[1][0][1], end=' ')
print(list1[1][1][0], end=' ')
print(list1[1][1][1], end=' ')
print(list1[2][0][0], end=' ')
print(list1[2][0][1], end=' ')
print(list1[2][1][0], end=' ')
print(list1[2][1][1], end=' \n')

print(list1[0][0], end=' ')
print(list1[0][1], end=' ')
print(list1[1][0], end=' ')
print(list1[1][1], end=' ')
print(list1[2][0], end=' ')
print(list1[2][1], end=' \n')

print(list1[0], end=' ')
print(list1[1], end=' ')
print(list1[2], end=' \n\n')

for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1[i][j])):
            print(list1[i][j][k], end = ' ')

print("\n")
print(list2, end=' \n\n')
print(len(list2))
print(len(list2[0]))
print(len(list2[0][0]))