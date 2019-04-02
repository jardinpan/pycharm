import random


layer = eval(input('enter the number of layer:'))
row = eval(input('enter the number of row:'))
column = eval(input('enter the number of column:'))
list1 = []
for i in range(layer):
    list1.append([])
    for j in range(row):
        list1[i].append([])
        for k in range(column):
            list1[i][j].append(random.randint(1, 100))
print(list1)