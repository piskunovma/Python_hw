"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_func(number1, number2):
    try:
        number1, number2 = int(number1), int(number2)
        if number2 == 0:
            print("Введите второе число не 0!")
        else:
            result = number1 / number2
            return round(result, 2)
    except ValueError:
        print("Вы ввели не число, введите число!")

number1 = input("Введите первое число: \n")
number2 = input("Введите второе число: \n")

print(my_func(number1, number2))