import random
row = eval(input('Enter the number of row: '))
col = eval(input('Enter the number of column: '))
list2 = []
for i in range(row):
    list2.append([])
    for j in range(col):
        list2[i].append(random.randint(1, 50))
print(list2)