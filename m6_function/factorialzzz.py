def factorial(a):
    total = 1
    for i in range(1, a + 1):
        total *= i
    return total

def main():
    x = eval(input('input a number:'))
    print('{0}! = {1}'.format(x, factorial(x)))

main()