x = 10
y = 11

def main():
    x = 20
    print(x)
    print(y)
main()
print(x)
print(y, end = "\n\n")

def outer():
    def inner1():
        print('Hello')
    def inner2():
        print('Maaya')
    inner1()
    inner2()
outer()
print()

def outer():
    def inner1():
        print('Hello')
        def inner2():
            print('Maaya')
        inner2()
    inner1()
outer()
print()

x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
    inner()
    print(x)
outer()
print(x, end = "\n\n")

x = 10
y = 11

def main():
    x = 20
    print(x)
    global y
    y = 22
    print(y)
main()
print(x)
print(y)

