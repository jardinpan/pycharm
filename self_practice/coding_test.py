#Codility coding test
#Time Spent : 48 min

def factorial(a):
    total = 1
    for i in range(1, a+1):
        total *= i
    return total

def solution(S):
    vowels = list("AEIOU")
    vow = 0
    con = 0
    vowS = 0
    conS = 0
    for i in range(len(S)):
        if S[i] in vowels:
            vow += 1
        else:
            con += 1
    setS = list(set(S))
    if con >= vow and con != 0 and vow != 0:
        for j in range(len(setS)):
            if setS[j] in vowels:
                vowS += 1
            else:
                conS += 1
        ans = factorial(vowS) * factorial(conS)
    elif con == 0 or vow == 0:
        ans = 0
    else:
        ans = 0
    print(ans)
    return ans

solution("AAIIBQWR")