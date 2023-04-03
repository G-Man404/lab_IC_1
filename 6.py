import math
import random
n = 6

text = input('Введите текст: ')

str_arr = [["" for i in range(n)] for i in range(math.ceil(len(text)/n))]

for i in range(len(str_arr)):
    for j in range(n):
        try:
            str_arr[i][j] = text[i*n+j]
        except:
            str_arr[i][j] = "_"

cipher_table1 = [i for i in range(n)]
random.shuffle(cipher_table1)
cipher_table2 = [i for i in range(math.ceil(len(text)/n))]
random.shuffle(cipher_table2)

n_arr_str = ["" for i in range(math.ceil(len(text)/n)*n)]
g = 0
for j in cipher_table1:
    for i in cipher_table2:
        n_arr_str[g] = str_arr[i][j]
        g+=1

print(str_arr)
print(cipher_table1)
print(cipher_table2)
print(n_arr_str)