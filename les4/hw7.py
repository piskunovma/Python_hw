"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce

def fibo_gen():
        fact = 1
        for itm in range(2, fact_number + 1):
            fact *= itm
            yield(fact)

while True:
    fact_number = input("Введите число, для расчета факториала числа: \n")
    try:
        fact_number = int(fact_number)
        break
    except ValueError:
        print("Введите число!")

for el in fibo_gen():
    if el > reduce(lambda x, y: x * y, range(1, 16)):
        break
    print(el)