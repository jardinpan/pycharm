def sum_avg(n1 = 1, n2 = 100):
    total = 0
    for i in range(n1, n2 + 1):
        total += i
    avg = total / (n2 - n1 + 1)
    return total, avg

def main():
    total, avg = sum_avg()
    print("sum = {}, avg = {}".format(total, avg))
    total, avg = sum_avg(n2 = 50)
    print("sum = {}, avg = {}".format(total, avg))
    total, avg = sum_avg(50)
    print("sum = {}, avg = {}".format(total, avg))
    total, avg = sum_avg(101, 200)
    print("sum = {}, avg = {}".format(total, avg))


main()