# PEP-8 Общие правила оформления

# переменные

name_string = "строка"
CONSTANT = "Константа"
snake_case = 1 # Переменные и функции
CamelCase = 2 #  Классы
# kebab-case = 3


name = 'Mikhail'
surname = 'Piskunov'
age = 22

full_data = '{a} {b} - {c} age'.format(a = name, b = surname, c = age) # метод format (форматирование)
full_data1 = f'{name:>20} {surname + " - surname"} - {age} age' # f строки (форматирование)

print(full_data)
print(full_data1)