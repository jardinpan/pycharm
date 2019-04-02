# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    ans = 1
    A = sorted(A)
    for i in range(len(A)):
        if ans == A[i]:
            ans += 1
    print(ans)
    return ans
A = [1, 3, 8, 7, 4 ,2, 6 ,1 ,3, 4]
print(A)
solution(A)

