# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

# Изначальный способ создания списка 
# list = []
# n = 10
# for i in range (n):
#     list.append(random.randint(-n, n))
# print('Список: ', list)

# Способ с использованием включения

n = 10
list = [random.randint(-n, n) for i in range(n)]
print(list)

list_result = []

def multiplication_pairs (list):
    for i in range((n // 2) + n % 2):
        list_result.append(list[i] * (list[-(i + 1)]))
    return list_result

print (multiplication_pairs(list))