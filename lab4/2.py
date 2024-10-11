import sys


def func(values, left, right, saved):
    if right <= left + 1: #одна матрица
        return 0
    min_res = sys.maxsize #большое значение
    if saved[left][right] == 0: #если еще не было посчитано
        for k in range(left + 1, right):
            res = func(values, left, k, saved) #перемножение матриц в левой части
            res += func(values, k, right, saved) #перемножение матриц в правой части
            res += values[left] * values[k] * values[right] #кол-во вычислений для двух получившихся матриц
            if res < min_res: #запоминаем минимальное значение
                min_res = res
        saved[left][right] = min_res #сохраняем посчитанное значение
    return saved[left][right]


values = [10, 100, 5, 50] #матрица 10 × 30, матрица 30 × 5, матрица 5 × 60
saved = [[0 for i in range(len(values))] for j in range(len(values))] #таблица с посчитанными значениями
print(func(values, 0, len(values) - 1, saved))
