import random

string = input("Введите текст: ")
block_len = int(input("Введите длину блока шифровке(Число должно быть кратно длине строки): "))

cipher_table = [i for i in range(block_len)]
random.shuffle(cipher_table)

new_string = [0 for i in range(len(string))]
for i in range(int(len(string)/block_len)):
    for j in range(block_len):
        new_string[i*block_len+j] = string[cipher_table[j]+i*block_len]

print(cipher_table)
print(new_string)