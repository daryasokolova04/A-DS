import time

mass = '11'
first, second = 1, 1
for i in range(500-2):
    first, second = second, first + second
    mass += str(second)
mass = list(mass)

start = time.time()

ch = dict()
for i in range(0, len(mass) - 1):
    value = mass[i] + mass[i+1]
    if value not in ch.keys():
        ch[value] = 0
        for j in range(i, len(mass) - 1):
            if value == mass[j] + mass[j+1]:
                ch[value] += 1
print("Результат работы наивного алгоритма: {}".format(max(ch.values())))

end = time.time()



#print(end - start) #0.647528886795044