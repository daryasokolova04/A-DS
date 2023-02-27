import time

mass = '11'
first, second = 1, 1
for i in range(500-2):
    first, second = second, first + second
    mass += str(second)
mass = list(mass)

#print(len(set(mass))) #проверка кол-ва различных чисел в массиве (10)

start = time.time()

index = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

ch = dict()
for i in range(len(mass) - 1):
    if mass[i] + mass[i+1] not in ch.keys():
        template = mass[i] + mass[i + 1]
        template_hash = index[mass[i]] * 10 + index[mass[i+1]] * 1
        ch[template] = 1
        for j in range(i + 1, len(mass) - 1):
            el_hash = index[mass[j]] * 10 + index[mass[j+1]] * 1
            if el_hash == template_hash:
                if template == mass[j] + mass[j+1]:
                    ch[template] += 1
print("Результат работы алгоритма Рабина-Карпа: {}".format(max(ch.values())))

end = time.time()


#print(end - start)#0.8979730606079102







