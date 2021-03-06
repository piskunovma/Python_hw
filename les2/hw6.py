"""\
6. *Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}"""
idx = 1
dict = {'Название': 'Введите название товара', 'Цена': 'Введите цену товара', 'Количество': 'Введите количество товара'}
answer = 1

user_list = []
while answer:
    result_dict = {}
    for key, itm in dict.items():
        user_dict = input(f'{itm} \n')
        result_dict[key] = user_dict
    user_list.append((idx, result_dict))
    idx += 1

    while True:
        answer = int(input("Ввести новый товар?(0 - No; 1 - Yes)\n"))
        if answer == 1:
             break
        else:
            break

analytics = {}
for key in dict:
    analytics[key] = [itm[1][key] for itm in user_list]

print(user_list)
print(analytics)