chis = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    chis[i][0], chis[i][1], chis[i][2] = input(f"Введите {i+1} строку: ").split()

log = False
for i in range(3):
    if (chis[i][0] == chis[i][1] == chis[i][2] == "x") or (chis[0][i] == chis[1][i] == chis[i][2] == "x"):
        log = True

if (chis[0][0] == chis[1][1] == chis[2][2] == "x") or (chis[0][2] == chis[1][1] == chis[2][0] == "x"):
    log = True

if log:
    print("Победа за крестиками!")
else:
    print("Победа за ноликами!")





