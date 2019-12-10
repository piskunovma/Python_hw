"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

my_f = open("text3.txt", "r", encoding="utf-8")

surname = 1
itm = 1
result_profit = int()
sum_collaborators = 0
for line in my_f:
    if surname == 1:
        print(line.split()[0])
        surname = 0
    surname += 1
    if itm == 1:
        income = int(line.split()[1])
        result_profit += income
        itm = 0
    itm += 1
    sum_collaborators += 1
print(f'Средняя величина дохода сотрудников - {result_profit / sum_collaborators}')
my_f.close()