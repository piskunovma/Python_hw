"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# list_1 = list(input("Введите элементы списка: "))
# list_result = []
#
# i = 0
# while True:
#     if i < len(list_1) and len(list_1) % 2 == 0:
#         i += 1
#         list_result.append(list_1[i])
#         i -= 1
#         list_result.append(list_1[i])
#         i += 2
#     elif len(list_1) % 2 != 0:
#         if i < len(list_1[:-1]):
#             i += 1
#             list_result.append(list_1[i])
#             i -= 1
#             list_result.append(list_1[i])
#             i += 2
#         else:
#             list_result.append(list_1[-1])
#             break
#     else:
#        break
# print(list_1, list_result)


list_1 = list(input("Введите элементы списка: "))
list_result = []

i = 1
while i < len(list_1):
    list_result.append(list_1[i])
    i -= 1
    list_result.append(list_1[i])
    i += 3
    if len(list_1) % 2 == 0:
        continue
    elif i < len(list_1[:-1]) and len(list_1) % 2 != 0:
        continue
    else:
        list_result.append(list_1[-1])
        break
print(list_1, list_result)