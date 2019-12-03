"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""
# Первый вариант
# new_list = [1, 2, 7, 4, 12, 16]
#
# result_list = []
# i = 0
# for check in new_list:
#     if i < len(new_list):
#         i += 1
#         if len(new_list) == i:
#             if new_list[-1] < check:
#                 result_list.append(check)
#                 break
#             else:
#                 break
#         if new_list[i] > check:
#             result_list.append(new_list[i])
#
# print(result_list)

# Второй вариант
new_list = [0, 2, 7, 4, 12, 15]
result = [new_list[idx] for idx in range(1, len(new_list)) if new_list[idx] > new_list[idx - 1]]

print(result)