def poisk(chis, elem):
    strok = len(chis)
    kolon = len(chis[0])

    str1 = 0
    kol = kolon - 1

    while str1 < strok and kol >= 0:
        if chis[str1][kol] == elem:
            return str1, kol  
        elif chis[str1][kol] < elem:
            str1 += 1  
        else:
            kol -= 1  

    return -1, -1  


n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))
chis=[]
for i in range(n):
    chis.append([])
    for j in range(m):
        chis[i].append(int(input(f"Введите элемент {i+1} строки: ")))
print(chis)

elem = int(input("Введите элемент, который необходимо найти: "))

str1_id, kol_id = poisk(chis, elem)

if str1_id == -1 and kol_id == -1:
    print("Элемент не найден")
else:
    print(f"Элемент найден на позиции ({str1_id+1}, {kol_id+1})")
