def mojno(pole, strok, kol):
    for i in range(8):
        if pole[strok][i] == 1 or pole[i][kol] == 1:
            return False

    
    for i in range(8):
        for j in range(8):
            if (i + j == strok + kol) or (i - j == strok - kol):
                if pole[i][j] == 1:
                    return False
    return True

def razmesh(pole, strok, reshs):
    if strok == 8:
        resh = []
        for i in range(8):
            for j in range(8):
                if pole[i][j] == 1:
                    resh.append((i, j))
        reshs.append(resh)
        return

    
    for kol in range(8):
        if mojno(pole, strok, kol):
            pole[strok][kol] = 1
            razmesh(pole, strok + 1, reshs)
            pole[strok][kol] = 0


pole = [[0] * 8 for _ in range(8)]
reshs = []
razmesh(pole, 0, reshs)


for resh in reshs:
    print(resh)
