x = 0
y = x
z = 0
print (x, y, z)
print(id(x), id(y), id(z))
x = 1
print (x, y, z)
print(id(x), id(y), id(z))

a, b = 123, 124
print(a, b)
print(id(a), id(b))
a = b = c =225
print(a, b, c)
print(id(a), id(b), id(c))
