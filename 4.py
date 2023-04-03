import math

key = list(input("Введите ключ: "))
string = input("Введите данные: ")
n_string = [["" for i in range(len(key))] for i in range(math.ceil(len(string)/len(key)))]
for i in range(math.ceil(len(string)/len(key))):
    for j in range(len(key)):
        if len(string) > i*len(key)+j:
            n_string[i][j] = string[i*len(key)+j]
        else:
            n_string[i][j] = "-"

n_key = ["" for i in range(len(key))]
n = 0
alphabet = list(map(chr, range(1072, 1103)))
for i in alphabet:
    for j in range(len(key)):
        if i == key[j].lower():
            n_key[j] = n
            n+=1

f_string = []
for i in range(len(n_key)):
    for j in range(math.ceil(len(string)/len(key))):
        f_string.append(n_string[j][n_key.index(i)])
print(f_string)