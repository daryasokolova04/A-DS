import time

mass = '11'
first, second = 1, 1
for i in range(500-2):
    first, second = second, first + second
    mass += str(second)
mass = list(mass)

def prefix(s):
    p = [0]
    for i in range(1, len(s)):
        st = s[:(i + 1)]
        pref = 1
        res = 0
        for index in range(len(st) - 1, 0, -1):
            if st[:pref] == st[index:]:
                res = pref
            pref += 1
        p.append(res)
    return p

start = time.time()


ch = dict()
for i in range(len(mass) - 1):
    template = mass[i] + mass[i+1]
    if template not in ch.keys():
        ch[template] = 1
        template_prefix = prefix(str(template))
        j = i + 1
        while j < len(mass) - 1:
            if mass[j] + mass[j+1] == template:
                ch[template] += 1
                j += 1
            else:
                if mass[i] == mass[j] and mass[j+1] != mass[i]:
                    step = 1
                    elem_prefix = template_prefix[1]
                else:
                    step = 0
                    elem_prefix = template_prefix[0]
                j += step - elem_prefix + 1
print("Результат работы алгоритма Кнута-Морриса-Пратта: {}".format(max(ch.values())))

end = time.time()

#print(end - start) #1.8628828525543213
