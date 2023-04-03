import math
n = 6
text = input('Введите текст: ')

str_arr = [["" for i in range(n)] for i in range(math.ceil(len(text)/n))]

for i in range(len(str_arr)):
    for j in range(n):
        try:
            str_arr[i][j] = text[i*n+j]
        except:
            str_arr[i][j] = "_"

n_arr_str = ["" for i in range(math.ceil(len(text)/n)*n)]

for j in range(n):
    for i in range(len(str_arr)):
        n_arr_str[j*len(str_arr)+i] = str_arr[i][j]

print(n_arr_str)