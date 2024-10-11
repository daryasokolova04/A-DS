def rukz(vesh: list, ves: int):
    tabl = [[["", 0] for i in range(ves)] for j in range(len(vesh))]
    for i in range(len(tabl)):
        for j in range(ves):
            if i == 0 and vesh[i][1] <= j + 1:
                tabl[i][j] = [vesh[i][0], vesh[i][2]]
            else:
                shift = j + 1 - vesh[i][1]
                if vesh[i][1] > j + 1:
                    tabl[i][j] = tabl[i-1][j]
                elif j == 0 or shift == 0:
                    tabl[i][j] = max(tabl[i-1][j], [vesh[i][0], vesh[i][2]], key=lambda x: x[1])
                else:
                    tabl[i][j] = max(tabl[i - 1][j], [vesh[i][0] + " " + tabl[i-1][shift - 1][0],
                                                        vesh[i][2] + tabl[i-1][shift-1][1]], key=lambda x: x[1])
    res = tabl[len(vesh)-1][ves-1]
    return res[0].split(), res[1]


def forres(vesh: list, kolvo: int, ves: int):
    for n in range(kolvo):
        res = rukz(vesh, ves)
        print(res)
        vesh = [i for i in vesh if i[0] not in res[0]]
        
predmet = [
    ["статуэтка", 2, 6000],
    ["картина", 2, 3000],
    ["фотоаппарат", 3, 2000],
    ["подушка", 1, 3000],
    ["пылесос", 3, 8000]
]

forres(predmet, 2, 4)
