"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count, cycle
# # Задание a)
# def iter_func(number):
#     for i in count(number, 1):
#         print(i)
#
# start_prog = input("Запустить бесконечный итератор? (Y - да, N - нет)\n")
# start_prog = start_prog.lower()
# if start_prog == "y":
#     while True:
#         user_number = input("Введите начальное число: \n")
#         try:
#             iter_func(int(user_number))
#         except ValueError:
#             print("Введите число!")
# else:
#     print("Програма завершена.")

# Задание б)
start_list = [12, 1, 33, 5, 9]
for i in cycle(start_list):
    print(i)
