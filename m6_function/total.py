def total(x, y):
    z = x ** 2 + y ** 2
    return z

def main():
    a, b = eval(input('input two numbers:'))
    c = total(a, b)
    print('{0}^2+{1}^2={2}'.format(a, b, c))

main()

#alternative
def total(x, y):
    return x ** 2 + y ** 2

def main():
    a, b = eval(input('input two numbers:'))
    print('{0}^2+{1}^2={2}'.format(a, b, total(a, b)))

main()