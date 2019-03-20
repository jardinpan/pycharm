a = 123
b = 12345.678
c = 'python'

print('/' + format(a, '5d') + '/')
print('/' + format(b, 'f') + '/')
print('/' + format(b, '10.2f') + '/')
print('/' + format(b, '10,.2f') + '/')
print('/' + format(b, '10.2e') + '/')
print('/' + format(b, '10.2E') + '/')
print('/' + format(c, '10s') + '/')

print('/' + format(a, '<5d') + '/')
print('/' + format(b, '<10.2f') + '/')
print('/' + format(c, '>10s') + '/')
print('/' + format(c, '^10s') + '/')
print('/' + format(c, '*^10s') + '/')

print('/' + format(a, '5X') + '/')
print('/' + format(a, '#5X') + '/')
print('/' + format(a, '#5o') + '/')
print('/' + format(a, '#5b') + '/')
print('/' + format(a, '05d') + '/')
print('/' + format(a, '+5d') + '/')

