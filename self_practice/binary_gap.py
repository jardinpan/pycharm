import numpy as np

max = 2147483647
def solution(N):
    # write your code in Python 3.6
    a = np.array([])
    for i in range(30, -1, -1):
        x = N // 2 ** i
        N = N % 2 ** i
        a = np.append(a, x)
    gap = 0
    position = 0
    subtraction = 0
    for j in range(31):
        if a[j] == 1 and position == 0:
            position = j
        elif a[j] == 1:
            subtraction = j - position - 1
            position = j
        if subtraction > gap:
            gap = subtraction
    return gap
    pass

print(solution(159874))