x = 10
def outer():
    x = 20
    def inner1():
        nonlocal x
        x = 30
        def inner2():
            nonlocal x
            print(x)
            x = 40
        inner2()
        print(x)
    inner1()
    print(x)
outer()
print(x, end = "\n\n")

def func():
    x = 10
    def get_x():
        return x
    def set_x(n):
        x = n
    return get_x, set_x
get, set = func()
print(get())
set(20)
print(get(), end = "\n\n")

def func():
    x = 10
    def get_x():
        return x
    def set_x(n):
        nonlocal x
        x = n
    return get_x, set_x
get, set = func()
print(get())
set(20)
print(get())

