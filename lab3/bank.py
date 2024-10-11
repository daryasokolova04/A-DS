def steal(mass, K, M):
    mass = sorted(mass, key=lambda x: x[1] / x[0], reverse=True) #сортировка по убыванию ценности
    len_mass = len(mass)
    i = 0 #индекс для прохода по вещам
    res_weight_price = []
    res_weight = 0 #счетчик украденного веса
    while i != len_mass and M != 0: #пока не закончились вещи и пока есть заходы
        weight, price = mass[i][0], mass[i][1] #вес и цена текущей вещи
        if res_weight + weight <= K:#пока украненный вес < максимально возможного
            res_weight += weight
            res_weight_price.append([weight, price])  #в результирующий массив добавляем украденную вещь
            i += 1
        else:
            if weight > K: #если вес 1 вещи > максимального веса, пропускаем эту вещь
                i += 1
            else:
                M -= 1 # -1 заход
                res_weight = 0
    return res_weight_price


N = int(input("Количество экспонатов: "))
M = int(input("Количество заходов: "))
K = int(input("Количество кг: "))
mass = [[0, 0]]*N
for i in range(N):
    weight, price = map(int, input("Введите вес и цену экспоната: ").split())
    mass[i] = [weight, price]

res = steal(mass, K, M)
if len(res) == 0:
    print("Ничего нельзя вынести")
else:
    for i in range(len(res)):
        print("Экспонат весом {} стоимостью {}".format(res[i][0], res[i][1]))
