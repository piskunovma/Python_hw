"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
# Первый вариант с использованием строки
number = (input('Введите целое положительное число: \n'))

i = 0
result = number[i + 1]
while i < len(number):
    if number[i] > result:
        result = number[i]
    elif number[i] < result:
        result = result
    i += 1

print(result)

# Второй вариант с использованием целого числа
number = int(input('Введите целое положительное число: \n'))

number = str(number)
long_numbers = len(number)
number = int(number)

i = 0
check = 0
while i < long_numbers:
    i += 1
    number_1 = number // (10**(long_numbers - i))
    if number_1 <= check:
        check = check
    else:
        check = number_1
    # print(number, long_numbers, number_1) Использовал для проверки
    number = number - (number_1 * (10 ** (long_numbers - i)))

print(check)
