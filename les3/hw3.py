"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
# Первый вариант нахождение через поиск наибольшего числа два раза
# def my_func(var1, var2, var3):
#     var3 = [var1, var2, var3]
#     i = 0
#     result = var3[i + 1]
#     while i < len(var3):
#         if var3[i] > result:
#             result = var3[i]
#         elif var3[i] < result:
#             result = result
#         i += 1
#     else:
#         var3.remove(result)
#         a = 0
#         result2 = var3[a + 1]
#         while a < len(var3):
#             if var3[a] > result2:
#                 result2 = var3[a]
#             elif var3[a] < result2:
#                 result2 = result2
#             a += 1
#         return result + result2
#
# print(my_func(11, 25, 6))

# Второй вариант с нахождением наименьшего числа и его вычеркиванием из списка
def my_func(var1, var2, var3):
    var3 = [var1, var2, var3]
    min = var3[0]
    for i in var3:
        if i < min:
            min = i
    var3.remove(min)
    result = sum(var3)
    return result

print(my_func(3, 1, 54))

