"""
4. Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

start_list = [0, 0, 2, 3, 4, 3, 6, 9, 0]
print(start_list)

result = [i for i in start_list if start_list.count(i) <= 1]
print(result)