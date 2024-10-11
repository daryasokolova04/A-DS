import math


def F(x, y, z):
    return (x and y) or ((not x) and z)


def G(x, y, z):
    return (x and z) or ((not z) and y)


def H(x, y, z):
    return x ^ y ^ z


def I(x, y, z):
    return y ^ ((not z) or x)


def choice(x, y, z, i):
    if i == 0:
        return F(x, y, z)
    elif i == 1:
        return G(x, y, z)
    elif i == 2:
        return H(x, y, z)
    else:
        return I(x, y, z)


def shift(x, m):
    x = x[m:] + x[:m]
    return x


s = [[7, 12, 17, 22],[5, 9, 14, 20],[4, 11, 16, 23],[6, 10, 15, 21]] # Значения дли сдвигов в каждом раунде


#перевод текста в двоичный код
text = input("Введите текст: ")
bin_text = ''
for letter in text:
    bin_text += bin(ord(letter))[2:]
#print("Изначальный текст в двоичной форме:", bin_text)
#print("Длина изначального текста:", len(bin_text))

#изначальная длина текста в 64-битном представлении
K = len(bin_text)
bin_length = ''
if K >= 2**64:
    K = K % 2**64
bin_length = bin(K)[2:]
while len(bin_length) < 64:
    bin_length = '0' + bin_length

#1 - выравнивание потока
bin_text += '1'
flag = True
while flag:
    size = (len(bin_text) - 448) / 512
    if size == int(size) and size >= 1:
        flag = False
    else:
        bin_text += '0'
#print("Текст с 1 и 0:", bin_text)
#print("Длина текста с 1 и 0:", len(bin_text))


#2 - добавление длины
bin_text += bin_length
#print("Текст с 0 и 1 + длина:", bin_text)
#print("Длина текста с 0 и 1 + длина:", len(bin_text))

#3 - инициализация буфера
buffer = {}
A = bin(int('01234567', 16))[2:]
buffer["A"] = '0' * (32 - len(A)) + A
B = bin(int('89ABCDEF', 16))[2:]
buffer["B"] = '0' * (32 - len(B)) + B
C = bin(int('FEDCBA98', 16))[2:]
buffer["C"] = '0' * (32 - len(C)) + A
D = bin(int('76543210', 16))[2:]
buffer["D"] = '0' * (32 - len(D)) + D
#print(buffer)

#4 - вычисление
T = [0]*64
for i in range(64):
    T[i] = (round(((2**32) * abs(math.sin(i + 1)))))
#print("T:", T)


for ind in range(0, len(bin_text), 512):
    block = bin_text[ind:(ind + 512)]
    buffer_copy = buffer.copy()
    X = []
    for i in range(0, 512, 32):
        X.append(block[i:(i + 32)]) #создание 32-битных блоков по 16 слов
    #print("массив 32-битных блоков по 16 слов:", X)
    index_T = 0
    for i in range(4):
        for k in range(16):
            A, B, C, D = buffer_copy["A"], buffer_copy["B"], buffer_copy["C"], buffer_copy["D"]
            res = bin(int(B, 2) + (int(A, 2) + choice(int(B, 2), int(C, 2),
                            int(D, 2), i) + int(X[k], 2) + T[index_T]))[2:]
            res = shift(res, s[i][k % 4])
            buffer_copy["B"] = res[(len(res) - 32):len(res)]
            buffer_copy["B"] = res[2:]
            buffer_copy["C"] = B
            buffer_copy["D"] = C
            buffer_copy["A"] = D
    for key in buffer.keys():
        buffer[key] = bin(int(buffer[key], 2) + int(buffer_copy[key], 2))[2:]
        buffer[key] = '0' * (32 - len(buffer[key])) + buffer[key]
      #  print(buffer[key])

ans = ''
for value in buffer.values():
    ans += hex(int(value, 2))[2:]
print("MD5 hash:", ans)

