# var_str = '111001'
# var_int = int(var_str, 2)
#
# var_int2 = -146
#
# var_str2 = 'это строка'

# for itm in var_str2:
#     print(itm)

# print(var_str2[0:7:2])
# print(var_str2[-1])
# print(var_str2[::-1])
# print(abs(var_int2))

# print(var_str2.split(' '))
# print(len(var_str2))
# print(var_str2.count('с'))
# print(var_str2.upper())
# print(var_str2.lower())
# print(var_str2.index('т', 2, 6))
# print(*reversed(var_str2))

# for idx, itm in enumerate(var_str2):
#     print(idx, itm)


# var_tuple = (1, 2, 3, 4, 5)
# var_list = [1, 2, 3]
# list()
# tuple()
#
#
#
# print(type(var_tuple))

# var1 = ([1, 2, 3], [4, 5, 6])
# var2 = var1
#
# var2[0].append(111)
#
# print(var1)

# user_data = (
#     {'name': 'Ваше имя?', 'type': str},
#     {'surname': 'Ваше фамилия?', 'type': str},
#     {'age': 'Сколько вам лет?', 'type': int}
# )

# try:
#     print(1)
# except ValueError as e:
#     print(2)

# people = dict()
# for quest in user_data:
#     while True:
#         tmp = input(quest[tuple(quest)[0]])
#         try:
#             tmp = quest['type'](tmp)
#             break
#         except ValueError as e:
#             print('Ошибка данных, повторите')
#             continue
#     people[tuple(quest)[0]] = tmp
#
# print(people)
#
# dict = {'Название': 'Введите название товара', 'Цена': 'Введите цену товара', 'Количество': 'Введите количество товара'}
#
# user_list = [(1, {'Название': 'iphone', 'Цена': '50000', 'Количество': '2'}), (2, {'Название': 'macbook', 'Цена': '150000', 'Количество': '1'})]
# analytics = {}
#
# for key in dict:
#     a = [itm[1][key] for itm in user_list]
#     print(a)
#     analytics[key] = a
# print(user_list)
# print(analytics)