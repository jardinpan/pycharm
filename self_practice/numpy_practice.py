import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
for i in range(2):
    for j in range(3):
        print(a[i, j])
print(a[0, 2])