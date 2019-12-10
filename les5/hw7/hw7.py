"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

my_f = open("text7.txt", "r")

sum_pr = int()
i = 0
result_prof = float()
result_list = list()
result_dict = dict()
dict_average = dict()
loss = dict()

for line in my_f:
    res = list(line.split())
    res[2] = int(res[2])
    res[3] = int(res[3])
    profit = res[2] - res[3]

    if profit > 0:
        i += 1
        result_dict[res[0]] = profit
        sum_pr += profit
    elif profit < 0:
        loss[f"{res[0]} - not profit"] = profit

    result_prof = sum_pr / i
    dict_average["Average profit"] = result_prof

result_list.append(result_dict)
result_list.append(loss)
result_list.append(dict_average)
print(result_list)
my_f.close()

with open("my_file.json", "w") as write_f:
    json.dump(result_list, write_f)
