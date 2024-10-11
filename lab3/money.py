def return_money(give_back, money):
    give_list = [[0, 0]] * len(money)  # список (длина = количество разных номиналов)
    money = sorted(money, reverse=True)  # сортировка по убыванию
    for pos, coin in enumerate(money):  # pos-индекс в списке money, coin-кортеж (номинал + кол-во)
        value, k = coin[0], coin[1]  # value-номинал, k-количество
        n = 0  # счетчик кол-ва монет, которые мы берем для сдачи
        while give_back >= value and k > 0:  # пока монеты для сдачи есть и номинал не превышает сдачу
            give_back -= value
            k -= 1
            n += 1
        give_list[pos] = [value, n]  #присваиваем списку с индексом pos кортеж(номинал, кол-во выбранных монет)
    return give_list, give_back #возвращаем итоговый список и сдачу


# money = [(10, 2), (5, 2), (2, 4), (1, 10)]
# give_back = 30
money = []
give_back = int(input("Сдача: "))
for i in range(4):
    m, s = map(int, input("Введите номинал и количество монет: ").split())
    money.append((m, s))
res_list, res_money = return_money(give_back, money)
for item in res_list:
    if item[1] != 0:
        print("Монет номиналом {} - {} шт.".format(item[0], item[1]))
if res_money != 0:
    print("{} руб. для сдачи не хватило".format(res_money))
