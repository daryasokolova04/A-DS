import time

mass = '11'
first, second = 1, 1
for i in range(500-2):
    first, second = second, first + second
    mass += str(second)
mass = list(mass)

start = time.time()

ch = dict()
for i in range(len(mass) - 1):
    template = mass[i] + mass[i+1]
    if template not in ch.keys():
        ch[template] = 1
        j = i + 1
        while j < len(mass) - 1:
            if mass[i+1] != mass[j+1] and mass[i] == mass[j+1]:
                j += 1
            elif mass[i+1] == mass[j+1] and mass[i] == mass[j]:
                ch[template] += 1
                j += 1
            else:
                j += 2
print("Результат работы алгоритма Бойера-Мура: {}".format(max(ch.values())))

end = time.time()

#print(end - start) #1.0275020599365234
