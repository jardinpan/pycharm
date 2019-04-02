#1. BinaryGap
#Time Spent : 59 min

def solution(N):
    # write your code in Python 3.6
    a = []
    for i in range(30, -1, -1):
        x = N // 2 ** i
        N = N % 2 ** i
        a.append(x)
    print(a)
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

print(solution(65184321))