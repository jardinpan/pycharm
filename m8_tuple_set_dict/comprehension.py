list1 = [i + 1 for i in range(52)]
print(list1)
list2 = [i * i for i in range(1, 11)]
print(list2)

set1 = {i * i for i in range(1, 11)}
print(set1) #因為是set 沒有順序 順序會亂

dict1 = {i:i * i for i in range(1, 11)}
print(dict1)

generator1 = (i * i for i in range(1, 11))
print(generator1) #<generator object <genexpr> at 0x000001F2BAF8B200>
for num in generator1:
    print(num, end = ' ')
print()

evans = [i for i in range(1, 51) if i % 2 == 0]
print(evans)
evans = [i for i in range(2, 51, 2)]
print(evans)
evans = [i for i in range(1, 51) if not i % 2]
print(evans)

print()
odds = [i for i in range(1, 51) if i % 2 == 1]
print(odds)
odds = [i for i in range(1, 51, 2)]
print(odds)
odds = [i for i in range(1, 51) if i % 2]
print(odds)

#一行找出100內質數
max = 101
primes = [prime for prime in range(2, max) if all(prime % num for num in range(2, prime))]
print(primes)
