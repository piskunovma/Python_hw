"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
"""
# # Первый вариант с помощью оператора **
# def my_func(x, y):
#     return x ** y
#
# print(my_func(2, -3))

# Вариант с помощью рекурсии
# def my_func(x, y):
#     y = y.__abs__()
#     if y == 0:
#         return 1
#     elif y == 1:
#         return 1 / x
#     elif y % 2 != 0:
#         return x * my_func(x, y - 1)
#     elif y % 2 == 0:
#         return my_func(x * x, y / 2)
#
# print(my_func(2, -4))

# Вариант с циклом
def my_func(x, y):
    y = y.__abs__()
    i = 1
    result = x
    if y == 0:
        return 1
    else:
        while i < y:
            result = result * x
            i += 1
    return 1 / result

print(my_func(2, -4))
