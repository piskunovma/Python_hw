"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
# Вариант для ввода чисел от 0 до 9

number = int(input("Введите число n: \n"))

number1 = number * 10 + number
number2 = number * 100 + number1
result = number + number1 + number2

print(result)

# Вариант для ввода любых чисел

number = int(input("Введите число n: \n"))

result4 = str(number) + str(number)
result5 = str(number) + str(number) + str(number)

result_numbers = number + int(result4) + int(result5)

print(result_numbers)