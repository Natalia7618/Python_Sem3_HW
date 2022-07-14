# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

# Вариант 1

def fibonacci_numbers(n):
    fibo_list = []
    f1, f2 = 1, 1
    for i in range (n):
        fibo_list.append(f1)
        f1, f2 = f2, f1 + f2
    f1, f2 = 0, 1
    for i in range (n + 1):
        fibo_list.insert(0, f1)
        f1, f2 = f2, f1 - f2
    return fibo_list

print (fibonacci_numbers(n))

# Вариант 2

# def fibonacci_list (n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return fibonacci_list (n - 1) + fibonacci_list(n - 2)
#     else:
#         return fibonacci_list (n + 2) - fibonacci_list(n + 1)


# for count in range(-n, n + 1):
#     print (fibonacci_list(count), end= ' ')
    