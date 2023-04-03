import random

string = input("Введите текст: ")

cipher_table = [i for i in range(len(string))]
random.shuffle(cipher_table)

new_string = [0 for i in range(len(string))]
for i in range(len(string)):
    new_string[i] = string[cipher_table[i]]

print(cipher_table)
print(new_string)