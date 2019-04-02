import m6_function.mymath

print(dir(m6_function.mymath))
print(m6_function.mymath.mypow(2, 3))
print(m6_function.mymath.myabs(-10))
print(m6_function.mymath.mysum(5, 7))

import m6_function.mymath as mymath
print(mymath.mypow(2, 3))
print(mymath.myabs(-10))
print(mymath.mysum(5, 7))

from m6_function.mymath import mypow
print(mypow(2, 3))

from m6_function.mymath import myabs as abs
print(abs(-10))
