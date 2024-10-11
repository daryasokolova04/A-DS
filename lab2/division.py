from itertools import islice
from random import randint


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n #yield позволяет не забыть значение переменной при следующем
                    #выполнении функции, тип полученного значения - генератор


array_of_primes = [x for x in islice(prime_generator(), 100)] #первые 100 простых чисел
M = array_of_primes[randint(0, 99)] #рандомное простое число из списка простых чисел
#print(M)

K = [int(x) for x in input("Массив чисел: ").split()]
res = []
for item in K:
    res.append(item % M)
print(res)