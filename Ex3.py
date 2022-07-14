# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def create_float_list (n, pos_First, pos_Last):
    return [round(uniform(pos_First, pos_Last), 2) for i in range (n)]
    
n = 7
pos_First = 0
pos_Last = 15
float_list = create_float_list(n, pos_First, pos_Last)
print ('Список из вещественных чисел: ', float_list)

def find_difference(decimal_list):
    return max(decimal_list) % 1 - min(decimal_list) % 1

print ('Разница между максимальным и минимальным значением дробной части элементов =', round(find_difference(float_list), 2))
